from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, set_driver) -> None:
        self.driver = set_driver

    def click_element(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def type_element(self, locator, text_to_type):
        self.driver.find_element(By.XPATH, locator).send_keys(text_to_type)

    def clear_element(self, locator):
        self.driver.find_element(By.XPATH, locator).clear()

    def get_element_text(self, locator):
        elem_text = self.driver.find_element(By.XPATH, locator).text
        return elem_text

    def get_current_url(self):
        page_url = self.driver.current_url
        return page_url

    def get_page_title(self):
        page_title = self.driver.title
        return page_title

    def get_element_attribute(self, locator, attribute):
        elem_attr = self.driver.find_element(
            By.XPATH, locator).get_attribute(attribute)
        return elem_attr

    def get_number_of_elements(self, locator):
        num_of_elem = len(self.driver.find_elements(By.XPATH, locator))
        return str(num_of_elem)

    def check_element_exist(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_enabled(self, locator):
        enable_status = self.driver.find_element(
            By.XPATH, locator).is_enabled()
        return enable_status

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_to_be_invisible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def wait_for_text_to_be_present_in_element(self, locator, text_to_be_visible):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, locator), text_to_be_visible))

    def select_dropbox_by_visible_text(self, locator, visible_text):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_visible_text(visible_text)

    def select_dropbox_by_value(self, locator, value):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_value(value)

    def select_dropbox_by_index(self, locator, index):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_value(index)

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView()", self.driver.find_element(By.XPATH, locator))

    def set_window_size_to(self, width, height):
        self.driver.set_window_size(width, height)
