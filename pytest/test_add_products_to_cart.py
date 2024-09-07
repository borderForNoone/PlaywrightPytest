import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from faker import Faker

faker = Faker()

def test_add_products_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Step 1-2: Launch browser and navigate to homepage
    home_page.navigate_to_homepage()

    # Step 3: Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # Step 4: Click 'Products' button
    home_page.click_products_button()

    product_name1, product_price1 = product_page.get_first_product_details()
    product_name2, product_price2 = product_page.get_second_product_details()

    # Normalize product names to remove any non-breaking spaces
    normalized_product_name1 = product_name1.replace('\xa0', '')
    normalized_product_name2 = product_name2.replace('\xa0', '')

    # Step 4: Hover over first product and click 'Add to Cart'
    product_page.hover_over_and_add_to_cart(1)

    # Step 6: Click 'Continue Shopping' button
    product_page.click_continue_shopping()

    # Step 7: Hover over second product and click 'Add to Cart'
    product_page.hover_over_and_add_to_cart(2)

    # Step 8: Click 'View Cart' button
    product_page.click_view_cart_button()

    # Step 9: Verify both products are added to Cart
    cart_page.verify_products_in_cart([normalized_product_name1, normalized_product_name2])

    # Step 10: Verify their prices, quantity, and total price
    cart_page.verify_product_details(1, product_price1, "1")
    cart_page.verify_product_details(2, product_price2, "1")
