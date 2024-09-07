import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from faker import Faker

faker = Faker()

def test_verify_subscription_in_cart(page):
    email, password, username = create_user(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)

    # Step 1: Launch browser and navigate to homepage
    home_page.navigate_to_homepage()

    # Step 2: Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # Step 3: Click 'Cart' button
    home_page.click_cart_button()

    # Step 4: Verify Cart page is visible
    cart_page.verify_cart_page_visible()

    # Step 5: Scroll down to footer (if needed, depending on where the subscription section is located)
    home_page.scroll_to_footer()

    # Step 6: Verify 'Subscription' text is visible on Cart page
    cart_page.verify_subscription_text_visible()

    # Step 7: Enter email address and click arrow button
    cart_page.enter_email_and_subscribe(email)

    # Step 8: Verify success message is visible on Cart page
    cart_page.verify_subscription_success()

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