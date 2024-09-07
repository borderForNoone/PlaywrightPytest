import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage
from playwright.sync_api import expect

@allure.title("Search Product and Verify Results")
@allure.description("This test case searches for a product and verifies the search results.")
def test_search_product(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)

    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # 4. Click on 'Products' button
    home_page.click_products_button()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    product_page.verify_all_products_page_visible()

    # 6. Enter product name in search input and click search button
    search_term = "Top"  # Replace with actual product name to search
    product_page.search_product(search_term)

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    product_page.verify_searched_products_visible(search_term)

