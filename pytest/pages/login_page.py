import allure
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Verify 'New User Signup!' is visible")
    def verify_new_user_signup_visible(self):
        expect(self.page.locator("h2:has-text('New User Signup!')")).to_be_visible()
        allure.attach(self.page.screenshot(), name="New User Signup Visibility", attachment_type=allure.attachment_type.PNG)

    @allure.step("Enter name and email")
    def enter_name_and_email(self, name, email):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[data-qa='signup-email']", email)

    @allure.step("Click 'Signup' button")
    def click_signup(self):
        self.page.click("button:has-text('Signup')")
        allure.attach(self.page.screenshot(), name="Signup Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Login with email and password")
    def login(self, email, password):
        self.page.fill("input[data-qa='login-email']", email)
        self.page.fill("input[data-qa='login-password']", password)
        self.page.click("button[data-qa='login-button']")
        allure.attach(self.page.screenshot(), name="Login Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify 'Login to your account' is visible")
    def verify_login_to_your_account_visible(self):
        expect(self.page.locator("h2:has-text('Login to your account')")).to_be_visible()
        allure.attach(self.page.screenshot(), name="Login Page Visibility", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify incorrect login error")
    def verify_incorrect_login_error(self):
        expect(self.page.locator("p:has-text('Your email or password is incorrect!')")).to_be_visible()
        allure.attach(self.page.screenshot(), name="Incorrect Login Error", attachment_type=allure.attachment_type.PNG)
