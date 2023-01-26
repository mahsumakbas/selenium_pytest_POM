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

    def get_element_text(self, locator):
        elem_text = self.driver.find_element(By.XPATH, locator).text
        return elem_text

    def get_current_url(self):
        page_url = self.driver.current_url
        return page_url

    def get_page_title(self):
        page_title = self.driver.title
        return page_title

    def check_element_exist(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except NoSuchElementException:
            return False

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH,locator)))

    def wait_for_element_to_be_invisible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.invisibility_of_element_located((By.XPATH,locator)))

    def select_dropbox_by_text(self, locator, visible_text):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_visible_text(visible_text)
