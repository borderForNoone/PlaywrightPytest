from playwright.sync_api import expect

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def click_contact_us(self):
        self.page.click("a:has-text('Contact us')")

    def verify_get_in_touch_visible(self):
        expect(self.page.locator("h2:has-text('Get In Touch')")).to_be_visible()

    def fill_contact_form(self, name, email, subject, message, file_path):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='subject']", subject)
        self.page.fill("textarea[name='message']", message)
        self.page.set_input_files("input[type='file']", file_path)

    def click_submit(self):
        self.page.click("[value='Submit']")

    def click_ok(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def verify_success_message(self):
        expect(self.page.locator("div.status.alert.alert-success")).to_be_visible()

    def click_home(self):
        self.page.click("a:has-text('Home')")
    