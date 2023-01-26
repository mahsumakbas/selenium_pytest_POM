from wrappers.base_page import BasePage

class PageTriangle(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver)

    link_triangle_app = "//a[@id='triangleapp']"
    btn_identify_type = "//button[@id='identify-triangle-action']"
    input_side1 = "//input[@id='side1']"
    input_side2 = "//input[@id='side2']"
    input_side3 = "//input[@id='side3']"
    text_result = "//p[@id='triangle-type']"

    def open_app_page(self):
        self.click_element(self.link_triangle_app)
        self.wait_for_element_to_be_visible(self.btn_identify_type)
    
    def write_side_one(self, num):
        self.type_element(self.input_side1, num)

    def write_side_two(self, num):
        self.type_element(self.input_side2, num)

    def write_side_three(self, num):
        self.type_element(self.input_side3, num)

    def click_identify_button(self):
        self.click_element(self.btn_identify_type)

    def get_result_text(self):
        result = self.get_element_text(self.text_result)
        return result
