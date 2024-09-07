from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.order_placed_title_locator = "h2[data-qa='order-placed']"
        self.comment_textarea = ".form-control"
        self.place_order_button = "a.check_out"
        self.name_on_card_input = "input[name='name_on_card']"
        self.card_number_input = "input[name='card_number']"
        self.cvc_input = "input[name='cvc']"
        self.expiry_month_input = "input[name='expiry_month']"
        self.expiry_year_input = "input[name='expiry_year']"
        self.pay_and_confirm_button = ".submit-button"

    def verify_address_and_order(self):
        assert self.page.locator("h2:has-text('Address Details')").is_visible()
        assert self.page.locator("h2:has-text('Review Your Order')").is_visible()

    def place_order(self, description):
        self.page.fill(self.comment_textarea, description)
        self.page.click(self.place_order_button)

    def verify_order_placed(self):
        self.page.wait_for_selector(self.order_placed_title_locator, state="visible", timeout=10000)
        order_placed_title = self.page.locator(self.order_placed_title_locator).text_content().strip()
        assert order_placed_title == "Order Placed!", f"Expected 'Order Placed!', but got '{order_placed_title}'"

    def confirm_order(self):
        self.page.click(self.pay_and_confirm_button)

    def enter_payment_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self.page.fill(self.name_on_card_input, name_on_card)
        self.page.fill(self.card_number_input, card_number)
        self.page.fill(self.cvc_input, cvc)
        self.page.fill(self.expiry_month_input, expiry_month)
        self.page.fill(self.expiry_year_input, expiry_year)
