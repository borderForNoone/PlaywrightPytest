import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage
from pages.home_page import HomePage
from faker import Faker

faker = Faker()

def test_verify_subscription_visible(page):
    email, password, username = create_user(page)
    
    home_page = HomePage(page)

    # Step 1: Launch browser
    home_page.navigate_to_homepage()

    # Step 2: Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # Step 3: Click 'Cart' button
    home_page.click_cart_button()

    # Step 4: Scroll down to footer
    home_page.scroll_to_footer()

    # Step 5: Verify 'Subscription' text is visible
    home_page.verify_subscription_text_visible()

    # Step 6: Enter email address and click arrow button
    home_page.enter_email_and_subscribe(email)

    # Step 7: Verify success message is visible
    home_page.verify_subscription_success()

def create_user(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    account_page = AccountPage(page)  

    name = faker.name()
    email = faker.email()
    password = faker.password()
    first_name = faker.first_name()
    last_name = faker.last_name()
    company = faker.company()
    address = faker.address().split('\n')[0]
    state = faker.state()
    city = faker.city()
    zipcode = faker.zipcode()
    mobile_number = faker.phone_number()

    home_page.navigate_to_homepage()
    assert "Automation Exercise" in page.title()
    home_page.click_signup_login()
    login_page.verify_new_user_signup_visible()
    login_page.enter_name_and_email(name, email)
    login_page.click_signup()
    signup_page.verify_account_information_visible()
    signup_page.fill_account_information(password)
    signup_page.fill_personal_details(first_name, last_name, company, address, state, city, zipcode, mobile_number)
    signup_page.submit_account_creation()
    signup_page.verify_account_created_visible()
    signup_page.click_continue()
    account_page.verify_logged_in_as(name)

    account_page.click_logout()

    return email, password, name