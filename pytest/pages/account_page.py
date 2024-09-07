import allure
from playwright.sync_api import expect

class AccountPage:
    def __init__(self, page):
        self.page = page
        self.account_deleted_title_locator = "h2[data-qa='account-deleted']"

    @allure.step("Verify logged in as {name}")
    def verify_logged_in_as(self, name):
        expect(self.page.locator(f"a:has-text('Logged in as {name}')")).to_be_visible()
        allure.attach(self.page.screenshot(), name=f"Logged In As {name}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click 'Delete Account' button")
    def delete_account(self):
        self.page.click("a:has-text('Delete Account')")
        allure.attach(self.page.screenshot(), name="Delete Account Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify account deleted")
    def verify_account_deleted_visible(self):
        expect(self.page.locator("h2:has-text('Account Deleted!')")).to_be_visible(timeout=10000)
        allure.attach(self.page.screenshot(), name="Account Deleted Visibility", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click 'Continue' button after account deletion")
    def click_continue_after_delete(self):
        self.page.click("a:has-text('Continue')")
        allure.attach(self.page.screenshot(), name="Continue After Delete Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click 'Logout' button")
    def click_logout(self):
        self.page.click('a[href="/logout"]')
        allure.attach(self.page.screenshot(), name="Logout Button Clicked", attachment_type=allure.attachment_type.PNG)

    def verify_account_deleted(self):
        self.page.wait_for_selector(self.account_deleted_title_locator, state="visible", timeout=10000)
        account_deleted_title = self.page.locator(self.account_deleted_title_locator).text_content().strip()
        assert account_deleted_title == "Account Deleted!", "Account deletion message not found"
