import allure
from faker import Faker
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage

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
    signup_page.fill_account_information(password)
    signup_page.fill_personal_details(first_name, last_name, company, address, state, city, zipcode, mobile_number)
    signup_page.submit_account_creation()
    signup_page.verify_account_created_visible()

    return email, password, name

@allure.title("Test Case 15: Place Order: Register before Checkout")
def test_place_order_register_before_checkout(page: Page):
    # Initialize page objects
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    account_page = AccountPage(page)

    # Step 1: Launch browser (Playwright does it automatically when test starts)

    # Step 2: Navigate to the homepage
    home_page.navigate_to_homepage()

    # Step 3: Verify that home page is visible successfully
    home_page.verify_homepage_visible()

    # Step 4: Click 'Signup / Login' button
    home_page.click_signup_login()

    # Step 5: Fill all details in Signup and create account
    email, password, username = create_user(page)

    # Step 6: Verify 'ACCOUNT CREATED!' and click 'Continue' button
    signup_page.verify_account_created_visible()
    signup_page.click_continue()

    # Step 7: Verify 'Logged in as username' at the top
    account_page.verify_logged_in_as(username)

    # Step 8: Add products to cart
    home_page.hover_over_and_add_to_cart(1)

    # Step 9: Click 'Cart' button
    home_page.click_popup_cart_button()

    # Step 10: Verify that cart page is displayed
    cart_page.verify_cart_page_visible()

    # Step 11: Click 'Proceed To Checkout'
    cart_page.click_checkout_button()

    # Step 12: Verify Address Details and Review Your Order
    checkout_page.verify_address_and_order()

    # Step 13: Enter description in comment text area and click 'Place Order'
    description = faker.sentence()
    checkout_page.place_order(description)

    # Step 14: Enter payment details: Name on Card, Card Number, CVC, Expiration date
    checkout_page.enter_payment_details(
        name_on_card=faker.name(),
        card_number=faker.credit_card_number(),
        cvc=faker.credit_card_security_code(),
        expiry_month=faker.month(),
        expiry_year=faker.year()
    )

    # Step 15: Click 'Pay and Confirm Order' button
    checkout_page.confirm_order()

    # Step 16: Verify success message 'Your order has been placed successfully!'
    checkout_page.verify_order_placed()

    # Step 17: Click 'Delete Account' button
    account_page.delete_account()

    # Step 18: Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_page.verify_account_deleted()
    account_page.click_continue_after_delete()
