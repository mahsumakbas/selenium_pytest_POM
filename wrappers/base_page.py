from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.urls import URLS


class BasePage():
    def __init__(self, set_driver, homepage_url: str = None) -> None:
        self.driver = set_driver
        self.DEFAULT_WAIT_TIMEOUT = 30
        if homepage_url:
            self.go_to(homepage_url)
        
    def go_to(self, homepage_url: str):
        url = URLS.get(homepage_url)
        if not url:
            raise ValueError(f"No URL found for key: {homepage_url}")
        self.driver.get(url)

    def _wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or self.DEFAULT_WAIT_TIMEOUT)

    """
    def log_info(self, msg):
        print(f"[{self.driver.test_platform.upper()} / {self.driver.test_browser.upper()}] {msg}")
    """

    def _find_element(self, locator: tuple[By, str]) -> WebElement:
        return  self.driver.find_element(*locator)

    def click_element(self, locator: tuple):
        self._find_element(locator).click()

    def type_element(self, locator: tuple, text_to_type: str):
        self._find_element(locator).send_keys(text_to_type)

    def clear_element(self, locator: tuple):
        self._find_element(locator).clear()

    def get_element_text(self, locator: tuple):
        elem_text = self._find_element(locator).text
        return elem_text

    def get_current_url(self):
        page_url = self.driver.current_url
        return page_url

    def get_page_title(self):
        page_title = self.driver.title
        return page_title

    def get_element_attribute(self, locator: tuple, attribute: str):
        elem_attr = self._find_element(locator).get_attribute(attribute)
        return elem_attr

    def get_number_of_elements(self, locator: tuple):
        num_of_elem = len(self.driver.find_elements(*locator))
        return str(num_of_elem)

    def check_element_exist(self, locator: tuple):
        try:
            self._find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_enabled(self, locator: tuple):
        enable_status = self._find_element(locator).is_enabled()
        return enable_status

    def is_element_displayed(self, locator: tuple) -> bool:
        return self.driver._find_element(locator).is_displayed()

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_element_to_be_visible(self, locator: tuple):
        self._wait().until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator: tuple):
        self._wait().until(EC.invisibility_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator: tuple, text_to_be_visible: str):
        #define custom timeout if needed self._wait(timeout=15)...
        self._wait().until(EC.text_to_be_present_in_element(locator, text_to_be_visible))

    def select_dropbox_by_visible_text(self, locator: tuple, visible_text: str):
        select = Select(self._find_element(locator))
        select.select_by_visible_text(visible_text)

    def select_dropbox_by_value(self, locator: tuple, value: str):
        select = Select(self._find_element(locator))
        select.select_by_value(value)

    def select_dropbox_by_index(self, locator: tuple, index: int):
        select = Select(self._find_element(locator))
        select.select_by_index(index)

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_element(self, locator: tuple):
        self.driver.execute_script(
            "arguments[0].scrollIntoView()", self._find_element(locator))

    def set_window_size_to(self, width: int, height: int):
        self.driver.set_window_size(width, height)

    def js_click(self, locator: tuple):
        self.driver.execute_script("arguments[0].click();", self._find_element(locator))
