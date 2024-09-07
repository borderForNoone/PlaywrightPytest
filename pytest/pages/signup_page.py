import allure
from playwright.sync_api import expect

class SignupPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Verify account information section is visible")
    def verify_account_information_visible(self):
        expect(self.page.locator("h2:has-text('Enter Account Information')")).to_be_visible(timeout=10000)
        allure.attach(self.page.screenshot(), name="Account Information Section", attachment_type=allure.attachment_type.PNG)

    @allure.step("Fill account information")
    def fill_account_information(self, password):
        self.page.check("input[id='id_gender1']")  # Select Title 'Mr'
        self.page.fill("input[name='password']", password)
        self.page.select_option("select[name='days']", "1")
        self.page.select_option("select[name='months']", "1")
        self.page.select_option("select[name='years']", "2000")

    @allure.step("Fill personal details")
    def fill_personal_details(self, first_name, last_name, company, address, state, city, zipcode, mobile_number):
        self.page.fill("input[name='first_name']", first_name)
        self.page.fill("input[name='last_name']", last_name)
        self.page.fill("input[name='company']", company)
        self.page.fill("input[name='address1']", address)
        self.page.fill("input[name='address2']", "Apt 456")
        self.page.select_option("select[name='country']", "United States")
        self.page.fill("input[name='state']", state)
        self.page.fill("input[name='city']", city)
        self.page.fill("input[name='zipcode']", zipcode)
        self.page.fill("input[name='mobile_number']", mobile_number)

    @allure.step("Submit account creation")
    def submit_account_creation(self):
        self.page.click("button:has-text('Create Account')")
        allure.attach(self.page.screenshot(), name="Account Creation Submitted", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify account created visibility")
    def verify_account_created_visible(self):
        expect(self.page.locator("h2:has-text('Account Created!')")).to_be_visible()
        allure.attach(self.page.screenshot(), name="Account Created Visibility", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click 'Continue' button")
    def click_continue(self):
        self.page.click("a:has-text('Continue')")
        allure.attach(self.page.screenshot(), name="Continue Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify email exists error")
    def verify_email_exists_error(self):
        expect(self.page.locator("p:has-text('Email Address already exist!')")).to_be_visible()
        allure.attach(self.page.screenshot(), name="Email Exists Error", attachment_type=allure.attachment_type.PNG)

    def verify_logged_in(self, username):
        assert self.page.locator(f"span.logged-in-as:has-text('{username}')").is_visible()
