import allure
from playwright.sync_api import expect

class ProductPage:
    def __init__(self, page):
        self.page = page
        # Define locators
        self.products_button_locator = "a[href='/products']"
        self.all_products_header_locator = "h2:has-text('All Products')"
        self.products_list_locator = ".features_items"
        self.product_info_locator = ".features_items .productinfo"
        self.search_input_locator = "input[id='search_product']"
        self.search_button_locator = "button#submit_search"
        self.searched_products_header_locator = "h2:has-text('Searched Products')"
        self.continue_shopping_button_locator = ".btn-success"
        self.view_cart_button_locator = "a[href='/view_cart'] u"

    @allure.step("Click on 'Products' button")
    def click_products_button(self):
        self.page.click(self.products_button_locator)
        allure.attach(self.page.screenshot(), name="Products Button Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify ALL PRODUCTS page is visible")
    def verify_all_products_page_visible(self):
        expect(self.page.locator(self.all_products_header_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="All Products Page Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify products list is visible")
    def verify_products_list_visible(self):
        expect(self.page.locator(self.products_list_locator)).to_be_visible()
        allure.attach(self.page.screenshot(), name="Products List Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click on the first product view")
    def click_first_product_view(self):
        self.page.click("a[href='/product_details/1']")  # Adjust as necessary
        allure.attach(self.page.screenshot(), name="First Product View Clicked", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify product detail visibility")
    def verify_product_detail_visible(self, expected_name, expected_price):
        product_name_locator = ".product-information h2"
        price_locator = ".product-information span > span"
        expect(self.page.locator(product_name_locator)).to_have_text(expected_name)
        expect(self.page.locator(price_locator)).to_have_text(expected_price)
        allure.attach(self.page.screenshot(), name="Product Detail Verified", attachment_type=allure.attachment_type.PNG)

    @allure.step("Get details of the first product")
    def get_first_product_details(self):
        product_price = self.page.locator(".productinfo h2").first.text_content()
        product_name = self.page.locator(".productinfo p").first.text_content()
        return product_name, product_price

    @allure.step("Get details of the second product")
    def get_second_product_details(self):
        # Locator for the second product
        product_locator = ".col-sm-4:nth-of-type(3)"
        
        # Get product name and price for the second product
        product_name = self.page.locator(f"{product_locator} .productinfo p").text_content()
        product_price = self.page.locator(f"{product_locator} .productinfo h2").text_content()
        
        return product_name, product_price

    @allure.step("Search for a product")
    def search_product(self, search_term):
        self.page.fill(self.search_input_locator, search_term)
        self.page.click(self.search_button_locator)
        allure.attach(self.page.screenshot(), name="Search Executed", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verify searched products are visible")
    def verify_searched_products_visible(self, search_term):
        expect(self.page.locator(self.searched_products_header_locator)).to_be_visible()
        search_results = self.page.locator(self.product_info_locator)
        product_count = search_results.count()
        print(f"Found {product_count} products")

        for i in range(product_count):
            product = search_results.nth(i)
            expect(product.locator("p")).to_contain_text(search_term)
        allure.attach(self.page.screenshot(), name="Searched Products Verified", attachment_type=allure.attachment_type.PNG)

    def hover_over_and_add_to_cart(self, product_index: int):
        product_locator = f"[data-product-id='{product_index}']"
        self.page.hover(product_locator)
        self.page.click(product_locator)

    def click_continue_shopping(self):
        self.page.click(self.continue_shopping_button_locator)

    @allure.step("Click 'View Cart' button")
    def click_view_cart_button(self):
        # Attempt to click the button with force option
        self.page.click(self.view_cart_button_locator)
        allure.attach(self.page.screenshot(), name="View Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

    def set_quantity(self, quantity):
        quantity_input = self.page.locator('input[name="quantity"]')
        quantity_input.fill(str(quantity))

    def click_add_to_cart(self):
        self.page.locator('button.cart').click()

    def product_details_visible(self):
        assert self.page.locator('.product-information h2').is_visible(), "Product title is not visible"

