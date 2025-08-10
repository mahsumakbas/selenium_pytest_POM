from time import sleep
from wrappers.base_page import BasePage
from selenium.webdriver.common.by import By


class PageCalculator(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver, homepage_url="qa")

    link_calc_app = (By.XPATH, "//a[@id='calculatetest']")
    btn_calculate = (By.XPATH, "//input[@id='calculate']")
    input_num1 = (By.XPATH, "//input[@id='number1']")
    input_num2 = (By.XPATH, "//input[@id='number2']")
    select_calc_op = (By.XPATH, "//select[@id='function']")
    text_answer = (By.XPATH, "//span[@id='answer']")

    def open_app_page(self):
        # print("Opening calculator app page with following information: "
        #       f"Platform: {self.driver.test_platform}, Browser: {self.driver.test_browser}")
        self.click_element(self.link_calc_app)
        self.wait_for_element_to_be_visible(self.btn_calculate)

    def write_numbers(self, num1, num2):
        self.type_element(self.input_num1, num1)
        self.type_element(self.input_num2, num2)

    def select_calculate_operation(self, op_name):
        self.select_dropbox_by_visible_text(self.select_calc_op, op_name)

    def click_calculate_button(self):
        self.click_element(self.btn_calculate)

    def get_result_text(self):
        sleep(1)  # Wait for the result to be displayed
        result = self.get_element_text(self.text_answer)
        return result

