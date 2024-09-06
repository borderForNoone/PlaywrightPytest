from playwright.sync_api import expect

class CasesForTestingPage:
    def __init__(self, page):
        self.page = page

    def verify_test_cases_page_visible(self):
        expect(self.page.locator("h2.title.text-center")).to_be_visible()
