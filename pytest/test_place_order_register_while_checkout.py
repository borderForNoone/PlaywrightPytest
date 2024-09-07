import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from faker import Faker

faker = Faker()

def create_user(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

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

    return email, password, name

def test_place_order_register_while_checkout(page):
    # Initialize page objects
    home_page = HomePage(page)
    cart_page = CartPage(page)
    signup_page = SignupPage(page)
    checkout_page = CheckoutPage(page)
    account_page = AccountPage(page)  

    # Step 1-2: Launch browser
    home_page.navigate_to_homepage()

    # Step 3: Verify home page visibility
    home_page.verify_homepage_visible()

    # Step 4: Add products to cart
    home_page.hover_over_and_add_to_cart(1)

    # Step 5: Click 'Cart' button
    home_page.click_popup_cart_button()

    # Step 6: Verify cart page is displayed
    cart_page.verify_cart_page_visible()

    # Step 7: Click 'Proceed To Checkout'
    cart_page.click_checkout_button()

    # Step 8: Click 'Register / Login' button
    cart_page.click_register_login_button()

    # Step 9: Fill all details in Signup and create account
    email, password, username = create_user(page)

    # Step 10: Verify 'ACCOUNT CREATED!' and click 'Continue' button
    signup_page.verify_account_created_visible()
    signup_page.click_continue()

    # Step 11: Verify 'Logged in as username'
    account_page.verify_logged_in_as(username)

    # Step 12: Click 'Cart' button
    home_page.click_cart_button()

    # Step 13: Click 'Proceed To Checkout' button
    cart_page.click_checkout_button()

    # Step 14: Verify Address Details and Review Your Order
    checkout_page.verify_address_and_order()

    # Step 15: Enter description in comment text area and click 'Place Order'
    description = faker.sentence()
    checkout_page.place_order(description)

    # Step 16: Enter payment details: Name on Card, Card Number, CVC, Expiration date'
    checkout_page.enter_payment_details(
        name_on_card=faker.name(),
        card_number=faker.credit_card_number(),
        cvc=faker.credit_card_security_code(),
        expiry_month=faker.month(),
        expiry_year=faker.year()
    )

    # Step 17: Click 'Pay and Confirm Order' button
    checkout_page.confirm_order()

    # Step 18: Verify success message 'Your order has been placed successfully!'
    checkout_page.verify_order_placed()

    # Step 19: Click 'Delete Account' button
    account_page.delete_account()  # Update selector if needed

    # Step 20: Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_page.verify_account_deleted()
    account_page.click_continue_after_delete()