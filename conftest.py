import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_context():
    # Launch browser and create context once for the session
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        # Close the context after the session ends
        context.close()

@pytest.fixture(scope="function")
def page(playwright_context):
    # Create a new page for each test function
    page = playwright_context.new_page()
    yield page
    # Close the page after the test function ends
    page.close()
