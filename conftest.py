import sys
from selenium import webdriver
from appium import webdriver as mobile_driver
from appium.options.common import AppiumOptions
from pytest import fixture, mark


def pytest_addoption(parser):
    parser.addoption("--platform", action="store",
                     help="platform that to be tested, could be 'web' or 'mobile'. Default is web")
    parser.addoption("--browser", action="store",
                     help="browser to run test on, could be 'chrome' or 'firefox'. Default is chrome")


@fixture(scope='session')
def platform(request):
    return request.config.getoption("--platform")


@fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@fixture
def driver(platform, browser):
    if platform is None or platform == "web":
        if browser is None or browser == "chrome":
            drvr = webdriver.Chrome()
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            drvr = webdriver.Firefox(options=options)
        else:
            print("Please enter valid value for --browser parameter")
    elif platform == "mobile":
        options = AppiumOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('platformVersion', '10.2')
        options.set_capability('newCommandTimeout', '60')
        options.set_capability('automationName', 'UiAutomator2')
        drvr = mobile_driver.Remote(
            command_executor='http://localhost:4723/wd/hub', options=options)
        drvr.implicitly_wait()
    else:
        print("Please enter valid value for --platform parameter")
        sys.exit()
    drvr.implicitly_wait(30)
    drvr.set_page_load_timeout(30)
    drvr.set_script_timeout(30)
    drvr.maximize_window()
    drvr.get("https://testpages.herokuapp.com/styled/index.html")
    yield drvr
    drvr.quit()


# to add screenshot for failed steps
@mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail_state = hasattr(report, 'wasxfail')
        if (report.skipped and xfail_state) or (report.failed and not xfail_state):
            mydriver = item.funcargs['driver']
            screenshot = mydriver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
    report.extra = extra
