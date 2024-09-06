import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_verify_all_products_and_detail_page(page):
    product_page = ProductPage(page)
    home_page = HomePage(page)

    # Step 1: Launch browser and navigate to the URL
    home_page.navigate_to_homepage()
        
    # Step 2: Verify that home page is visible
    home_page.verify_homepage_visible()

    # Step 3: Click on 'Products' button
    product_page.click_products_button()

    # Step 4: Verify user is navigated to ALL PRODUCTS page successfully
    product_page.verify_all_products_page_visible()

    # Step 5: Verify that products list is visible
    product_page.verify_products_list_visible()

    product_name, product_price = product_page.get_first_product_details()

    # Step 6: Click on 'View Product' of first product
    product_page.click_first_product_view()

    # Step 7: Verify user is landed on the product detail page and all details are visible
    product_page.verify_product_detail_visible(product_name, product_price)