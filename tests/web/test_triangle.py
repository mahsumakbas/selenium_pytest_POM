from pages.page_triangle import PageTriangle
import pytest
import time

@pytest.fixture
def triangle_page(driver):
    tp = PageTriangle(driver)
    return tp

class TestTriangle:

    def test_scalene(self, triangle_page):
        triangle_page.open_app_page()
        triangle_page.write_side_one("5")
        triangle_page.write_side_two("6")
        triangle_page.write_side_three("7")
        triangle_page.click_identify_button()
        assert "Scalene" == triangle_page.get_result_text()

    def test_isosceles(self, triangle_page):
        triangle_page.open_app_page()
        triangle_page.write_side_one("6")
        triangle_page.write_side_two("6")
        triangle_page.write_side_three("7")
        triangle_page.click_identify_button()
        assert "Isosceles" == triangle_page.get_result_text()

    def test_equilateral(self, triangle_page):
        triangle_page.open_app_page()
        triangle_page.write_side_one("6")
        triangle_page.write_side_two("6")
        triangle_page.write_side_three("6")
        triangle_page.click_identify_button()
        assert "Equilateral" == triangle_page.get_result_text()

    def test_invalid_triangle(self, triangle_page):
        triangle_page.open_app_page()
        triangle_page.write_side_one("5")
        triangle_page.write_side_two("6")
        triangle_page.write_side_three("11")
        triangle_page.click_identify_button()
        assert "Error: Not a Triangle" == triangle_page.get_result_text()
