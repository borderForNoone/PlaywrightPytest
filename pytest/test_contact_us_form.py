import pytest
from faker import Faker
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from playwright.sync_api import sync_playwright
import os
import time

faker = Faker()

def test_contact_us_form(page):
    contact_us_page = ContactUsPage(page)
    home_page = HomePage(page)

    # Test data
    name = faker.name()
    email = faker.email()
    subject = faker.sentence(nb_words=3)
    message = faker.paragraph()
    file_path = os.path.abspath("img.jpg")  

    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    assert "Automation Exercise" in page.title()

    # 4. Click on 'Contact Us' button
    contact_us_page.click_contact_us()

    # 5. Verify 'GET IN TOUCH' is visible
    contact_us_page.verify_get_in_touch_visible()

    # 6. Enter name, email, subject and message
    contact_us_page.fill_contact_form(name, email, subject, message, file_path)

    # 7. Upload file
    # (Done within fill_contact_form method)

    # 8. Click 'Submit' button
    contact_us_page.click_submit()

    # 9. Click OK button
    contact_us_page.click_ok()
    contact_us_page.click_submit()

    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    contact_us_page.verify_success_message()

    # 11. Click 'Home' button and verify that you landed on the home page
    contact_us_page.click_home()
    home_page.verify_homepage_visible()