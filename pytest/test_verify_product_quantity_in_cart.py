import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_verify_product_quantity_in_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Step 1-2: Launch browser and navigate to homepage
    home_page.navigate_to_homepage()

    # Step 3: Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # Step 4: Click 'View Product' for any product on home page
    home_page.click_view_product()

    # Step 5: Verify product detail is opened
    product_page.product_details_visible()

    # Step 6: Increase quantity to 4
    product_page.set_quantity(4)

    # Step 7: Click 'Add to cart' button
    product_page.click_add_to_cart()

    # Step 8: Click 'View Cart' button
    product_page.click_view_cart_button()

    # Step 9: Verify that product is displayed in cart page with exact quantity
    cart_page.verify_product_quantity(4)
