from selenium import webdriver
from appium import webdriver as mobile_driver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pytest import fixture
import pytest
from _pytest.config import UsageError

VALID_PLATFORMS = {"web", "mobile"}
VALID_BROWSERS = {"chrome", "firefox"}

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="web",
                     help="platform that to be tested, could be 'web' or 'mobile'. Default is web")
    parser.addoption("--browser", action="store", default="chrome",
                     help="browser to run test on, could be 'chrome' or 'firefox'. Default is chrome")

def pytest_configure(config):
    platform = config.getoption("--platform")
    if platform and platform.lower() not in VALID_PLATFORMS:
        pytest.exit(f"Invalid --platform '{platform}'. Valid options are {VALID_PLATFORMS}.", returncode=1)

    browser = config.getoption("--browser")
    if browser and browser.lower() not in VALID_BROWSERS:
        pytest.exit(f"Invalid --browser '{browser}'. Valid options are {VALID_BROWSERS}.", returncode=1)

@fixture(scope='session')
def platform(request):
    return request.config.getoption("--platform")

@fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

"""
#This hook modifies the collection of tests based on the platform specified.
#If a platform is specified, only tests with the corresponding marker will be executed.
def pytest_collection_modifyitems(config, items):
    platform = config.getoption("--platform")
    if not platform:
        return  # no platform specified, run everything

    selected_items = []
    deselected_items = []

    for item in items:
        if item.get_closest_marker(platform):
            selected_items.append(item)
        else:
            deselected_items.append(item)

    if deselected_items:
        config.hook.pytest_deselected(items=deselected_items)
        items[:] = selected_items
"""

@fixture
def driver(platform, browser):
    if platform is None or platform == "web":
        if browser is None or browser == "chrome":
            options = ChromeOptions()
            # options.binary_location = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            # options.add_argument("--headless")
            drvr = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            #options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            drvr = webdriver.Firefox(options=options)
        else:
            raise UsageError("Please enter a valid value for --browser (chrome/firefox)")
    elif platform == "mobile":
        options = AppiumOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('platformVersion', '10.2')
        options.set_capability('newCommandTimeout', '60')
        options.set_capability('automationName', 'UiAutomator2')
        drvr = mobile_driver.Remote(
            command_executor='http://localhost:4723/wd/hub', options=options)
        drvr.implicitly_wait(30)
    else:
        raise UsageError("Please enter a valid value for --platform (web/mobile)")
    drvr.implicitly_wait(30)
    drvr.set_page_load_timeout(30)
    drvr.set_script_timeout(30)
    drvr.maximize_window()
    
    # Attach metadata to driver
    #setattr(drvr, "test_platform", platform)
    #setattr(drvr, "test_browser", browser)
    yield drvr
    drvr.quit()


# to add screenshot for failed steps
@pytest.hookimpl(hookwrapper=True)
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
    report.extras = extra
