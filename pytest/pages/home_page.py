import allure
import re
from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        # Define locators
        self.products_button_locator = "a[href='/products']"
        self.homepage_title_locator = "title"
        self.signup_login_locator = "a[href='/login']"
        self.test_cases_locator = "a:has-text('Test Cases')"
        self.subscription_section_locator = "h2:has-text('Subscription')"
        self.subscription_arrow_button_locator = "button#subscribe"
        self.email_input_locator = "input#susbscribe_email"
        self.subscription_success_locator = "#success-subscribe"
        self.popup_cart_button_locator = "a[href='/view_cart'] u"
        self.cart_button_locator = "a[href='/view_cart']"

    @allure.step("Navigate to homepage")
    def navigate_to_homepage(self):
        self.page.goto("http://automationexercise.com", timeout=60000) 
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

    @allure.step("Scroll down to footer")
    def scroll_to_footer(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(self.page.screenshot(), name="Scrolled to Footer", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify 'Subscription' text is visible")
    def verify_subscription_text_visible(self):
        expect(self.page.locator(self.subscription_section_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Subscription Text Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Enter email and subscribe")
    def enter_email_and_subscribe(self, email):
        self.page.fill(self.email_input_locator, email)
        self.page.click(self.subscription_arrow_button_locator)
        allure.attach(self.page.screenshot(), name="Subscribed with Email", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify subscription success message")
    def verify_subscription_success(self):
        # Wait for the success message element to be visible
        expect(self.page.locator(self.subscription_success_locator)).to_have_class(re.compile(r'\b(?:alert-success|)\b'))
        expect(self.page.locator(self.subscription_success_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Subscription Success Message Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on 'Cart' button")
    def click_cart_button(self):
        self.page.click(self.cart_button_locator)
        allure.attach(self.page.screenshot(), name="Cart Page", attachment_type=allure.attachment_type.PNG)

    def click_popup_cart_button(self):
        self.page.click(self.popup_cart_button_locator)
        allure.attach(self.page.screenshot(), name="Cart Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on 'Products' button")
    def click_products_button(self):
        self.page.click(self.products_button_locator)
        allure.attach(self.page.screenshot(), name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    def click_view_product(self):
        self.page.locator('a[href*="/product_details/"]').first.click()

    def hover_over_and_add_to_cart(self, product_index: int):
        product_locator = f"[data-product-id='{product_index}']"
        self.page.hover(product_locator)
        self.page.click(product_locator)
