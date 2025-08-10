from wrappers.base_page import BasePage
from selenium.webdriver.common.by import By


class PageMobile(BasePage):

    def __init__(self, set_driver):
        super().__init__(set_driver)

    btn_click_login= (By.XPATH, "//android.widget.Button[@content-desc='Login']")
    btn_allow_notification_permission= (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    btn_deny_notification_permission= (By.ID, "com.android.permissioncontroller:id/permission_deny_button")

    def open_app_page(self):
        print("Opening mobile app page")
        self.wait_for_element_to_be_visible(self.btn_allow_notification_permission)

    def allow_notification_permission(self):
        print("Allowing notification permission")
        self.click_element_two(self.btn_allow_notification_permission)

    def deny_notification_permission(self):
        print("Denying notification permission")
        self.click_element_two(self.btn_deny_notification_permission)
   