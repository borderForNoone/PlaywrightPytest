import pytest
from playwright.sync_api import sync_playwright
from pages.cases_for_testing_page import CasesForTestingPage
from pages.home_page import HomePage

def test_verify_test_cases_page(page):
    home_page = HomePage(page)
    test_cases_page = CasesForTestingPage(page)

    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # 4. Click on 'Test Cases' button
    home_page.click_test_cases()

    # 5. Verify user is navigated to test cases page successfully
    test_cases_page.verify_test_cases_page_visible()
