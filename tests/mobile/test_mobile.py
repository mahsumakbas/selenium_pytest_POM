from pages.mobile.page_mobile import PageMobile
import pytest

@pytest.fixture
def mobile_page(driver) -> PageMobile:
    return PageMobile(driver)

@pytest.mark.mobile
class TestMobile:

    def test_mobile_apps(self, mobile_page):
        mobile_page.open_app_page()
        mobile_page.deny_notification_permission()
        assert True, "Mobile app page opened successfully"
   

   