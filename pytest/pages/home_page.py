import allure
from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        # Define locators
        self.products_button_locator = "a[href='/products']"
        self.homepage_title_locator = "title"
        self.signup_login_locator = "a[href='/login']"
        self.test_cases_locator = "a:has-text('Test Cases')"

    @allure.step("Navigate to homepage")
    def navigate_to_homepage(self):
        self.page.goto("http://automationexercise.com")
        allure.attach(self.page.screenshot(), name="Homepage", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on 'Signup/Login' link")
    def click_signup_login(self):
        self.page.click(self.signup_login_locator)
        allure.attach(self.page.screenshot(), name="Signup/Login Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify homepage is visible")
    def verify_homepage_visible(self):
        assert "Automation Exercise" in self.page.title()
        allure.attach(self.page.screenshot(), name="Homepage Title Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on 'Test Cases' link")
    def click_test_cases(self):
        self.page.click(self.test_cases_locator)
        allure.attach(self.page.screenshot(), name="Test Cases Page", attachment_type=allure.attachment_type.PNG)
