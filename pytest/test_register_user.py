import pytest
from playwright.sync_api import sync_playwright
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage

faker = Faker()

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

def test_register_user(page):
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

    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    account_page = AccountPage(page)

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
    account_page.delete_account()
    account_page.verify_account_deleted_visible()
    account_page.click_continue_after_delete()

def test_register_user_with_existing_email(page):
    # Test data
    email, password, username = create_user(page)

    # Page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    # Steps
    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # 4. Click on 'Signup / Login' button
    home_page.click_signup_login()

    # 5. Verify 'New User Signup!' is visible
    login_page.verify_new_user_signup_visible()

    # 6. Enter name and already registered email address
    login_page.enter_name_and_email(username, email)

    # 7. Click 'Signup' button
    login_page.click_signup()

    # 8. Verify error 'Email Address already exist!' is visible
    signup_page.verify_email_exists_error()

    