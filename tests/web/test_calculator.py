from pages.page_calculator import PageCalculator
import pytest

@pytest.fixture
def calc_page(driver):
    cp = PageCalculator(driver)
    return cp

class TestCalculator:

    def test_addition_positive_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("plus")
        calc_page.write_numbers(13, 47)
        calc_page.click_calculate_button()
        assert "60" == calc_page.get_result_text()

    def test_addition_negative_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("plus")
        calc_page.write_numbers(-13, -47)
        calc_page.click_calculate_button()
        assert "-60" == calc_page.get_result_text()

    def test_multiplication_positive_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("times")
        calc_page.write_numbers(47, 13)
        calc_page.click_calculate_button()
        assert "611" == calc_page.get_result_text()

    def test_multiplication_negative_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("times")
        calc_page.write_numbers(-47, -13)
        calc_page.click_calculate_button()
        assert "611" == calc_page.get_result_text()

    def test_subtraction_positive_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("minus")
        calc_page.write_numbers(47, 13)
        calc_page.click_calculate_button()
        assert "34" == calc_page.get_result_text()

    def test_subtraction_negative_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("minus")
        calc_page.write_numbers(-47, -13)
        calc_page.click_calculate_button()
        assert "-34" == calc_page.get_result_text()

    def test_division_positive_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("divide")
        calc_page.write_numbers(42, 6)
        calc_page.click_calculate_button()
        assert "7" == calc_page.get_result_text()

    def test_division_negative_integers(self, calc_page):
        calc_page.open_app_page()
        calc_page.select_calculate_operation("divide")
        calc_page.write_numbers(-42, -6)
        calc_page.click_calculate_button()
        assert "7" == calc_page.get_result_text()
