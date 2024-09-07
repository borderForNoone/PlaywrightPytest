import allure
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        # Define locators
        self.cart_page_locator = "//li[@class='active' and text()='Shopping Cart']"
        self.subscription_section_locator = "h2:has-text('Subscription')"
        self.subscription_arrow_button_locator = "button#subscribe"
        self.email_input_locator = "input#susbscribe_email"
        self.subscription_success_locator = "#success-subscribe"
        self.product_locator = "tr[id^='product-']"
        self.price_locator = ".cart-price"
        self.quantity_locator = ".cart-quantity"
        self.total_price_locator = ".cart-total"

    @allure.step("Verify Cart page is visible")
    def verify_cart_page_visible(self):
        expect(self.page.locator(self.cart_page_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Cart Page Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify 'Subscription' text is visible on Cart page")
    def verify_subscription_text_visible(self):
        expect(self.page.locator(self.subscription_section_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Subscription Text Verified on Cart Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Enter email and subscribe on Cart page")
    def enter_email_and_subscribe(self, email):
        self.page.fill(self.email_input_locator, email)
        self.page.click(self.subscription_arrow_button_locator)
        allure.attach(self.page.screenshot(), name="Subscribed with Email on Cart Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify subscription success message on Cart page")
    def verify_subscription_success(self):
        expect(self.page.locator(self.subscription_success_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Subscription Success Message Verified on Cart Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify products in cart")
    def verify_products_in_cart(self, expected_products: list):
        # Wait for cart products to be visible
        self.page.wait_for_selector(self.product_locator, timeout=10000)
        
        # Fetch all product rows
        product_rows = self.page.locator(self.product_locator).all()

        # Extract text from each product row
        products = []
        for row in product_rows:
            # Locate the product name within the <h4> tag
            product_name = row.locator(".cart_description h4 a").text_content().strip()
            # Normalize product name by replacing non-breaking spaces with regular spaces
            normalized_product_name = product_name.replace('\xa0', ' ')
            products.append(normalized_product_name)

        # Print or log the products for debugging
        print(f"Products in Cart: {products}")
        print(f"Expected Products: {expected_products}")

        # Check if the expected products are a subset of the products in the cart
        assert set(expected_products).issubset(set(products)), "Some products are missing from the cart"
        
        allure.attach(self.page.screenshot(), name="Products in Cart", attachment_type=allure.attachment_type.PNG)


    @allure.step("Verify product details")
    def verify_product_details(self, product_index: int, expected_price: str, expected_quantity: str):
        product_locator = f"{self.product_locator}:nth-of-type({product_index})"
        price_locator = f"{product_locator} .cart_price p"
        quantity_locator = f"{product_locator} .cart_quantity button"

        # Check price
        price_element = self.page.locator(price_locator)
        assert price_element.is_visible(), f"Price element not visible: {price_locator}"
        actual_price = price_element.text_content().strip()
        assert actual_price == expected_price, f"Expected price: {expected_price}, but got: {actual_price}"

        # Check quantity
        quantity_element = self.page.locator(quantity_locator)
        assert quantity_element.is_visible(), f"Quantity element not visible: {quantity_locator}"
        actual_quantity = quantity_element.text_content().strip()
        assert actual_quantity == expected_quantity, f"Expected quantity: {expected_quantity}, but got: {actual_quantity}"

        allure.attach(self.page.screenshot(), name="Product Details Verified", attachment_type=allure.attachment_type.PNG)

    def verify_total_price(self, expected_total: str):
        assert self.page.locator(self.total_price_locator).text_content() == expected_total

    def verify_product_quantity(self, expected_quantity: int):
        # Updated locator to target button inside cart_quantity cell
        quantity_locator = "td.cart_quantity button"

        # Locate the element and wait for it to be visible
        locator = self.page.locator(quantity_locator)
        locator.wait_for(state='visible')

        # Get the text content and strip extra spaces
        actual_quantity = locator.text_content().strip()

        # Assert that the actual quantity matches the expected quantity
        assert actual_quantity == str(expected_quantity), f"Expected quantity: {expected_quantity}, but got: {actual_quantity}"

    def click_checkout_button(self):
        self.page.click("a.check_out")

    def click_register_login_button(self):
        self.page.click("[href='/login'] u")