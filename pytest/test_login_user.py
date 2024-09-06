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

def test_login_user_with_correct_credentials(page):
    email, password, username = create_user(page)

    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    home_page.navigate_to_homepage()
    home_page.verify_homepage_visible()
    home_page.click_signup_login()
    login_page.verify_login_to_your_account_visible()
    login_page.login(email, password)
    account_page.verify_logged_in_as(username)
    account_page.delete_account()
    account_page.verify_account_deleted_visible()

def test_login_user_with_incorrect_credentials(page):
    # Test data
    incorrect_email = faker.email()
    incorrect_password = faker.password()

    # Page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Steps
    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # 4. Click on 'Signup / Login' button
    home_page.click_signup_login()

    # 5. Verify 'Login to your account' is visible
    login_page.verify_login_to_your_account_visible()

    # 6. Enter incorrect email address and password
    login_page.login(incorrect_email, incorrect_password)

    # 7. Click 'login' button (already done within login method)

    # 8. Verify error 'Your email or password is incorrect!' is visible
    login_page.verify_incorrect_login_error()

def test_logout_user(page):
    # Test data
    email, password, username = create_user(page)

    # Page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    # Steps
    # 1. Launch browser and 2. Navigate to url 'http://automationexercise.com'
    home_page.navigate_to_homepage()

    # 3. Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # 4. Click on 'Signup / Login' button
    home_page.click_signup_login()

    # 5. Verify 'Login to your account' is visible
    login_page.verify_login_to_your_account_visible()

    # 6. Enter correct email address and password
    login_page.login(email, password)

    # 7. Click 'login' button (already done within login method)

    # 8. Verify that 'Logged in as username' is visible
    account_page.verify_logged_in_as(username)

    # 9. Click 'Logout' button
    account_page.click_logout()

    # 10. Verify that user is navigated to login page
    login_page.verify_login_to_your_account_visible()