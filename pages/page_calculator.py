from wrappers.base_page import BasePage


class PageCalculator(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver)

    link_calc_app = "//a[@id='calculatetest']"
    btn_calculate = "//input[@id='calculate']"
    input_num1 = "//input[@id='number1']"
    input_num2 = "//input[@id='number2']"
    select_calc_op = "//select[@id='function']"
    text_answer = "//span[@id='answer']"

    def open_app_page(self):
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
        result = self.get_element_text(self.text_answer)
        return result

