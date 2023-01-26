from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.maximize_window()
    driver.get("https://testpages.herokuapp.com/styled/index.html")
    yield driver
    driver.quit()