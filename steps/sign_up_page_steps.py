from behave import *


@given('SignUp Page: I am on the jules.app sign up page')
def step_impl(context):
    context.sign_up_page_object.navigate_sign_up_page()


@when('SignUp Page: I select the "Personal" option')
def step_impl(context):
    context.sign_up_page_object.account_option_selection()


@when('SignUp Page: I click continue')
def step_impl(context):
    context.sign_up_page_object.click_continue()


@when('SignUp Page: I input correct first name')
def step_impl(context):
    context.sign_up_page_object.input_info("Ramona")


@given('SignUp Page: I input correct last name')
def step_impl(context):
    context.sign_up_page_object.input_info("Gherasim")


@when('SignUp Page: I input an invalid email address')
def step_impl(context):
    context.sign_up_page_object.input_info("Ramona@gmail")


@when('SignUp Page: I clear the email input')
def step_impl(context):
    context.sign_up_page_object.clear_input()


@when('SignUp Page: I input a valid email address')
def step_impl(context):
    context.sign_up_page_object.input_info("Ramona@gmail.com")


@when('SignUp Page: I click on the "Log in" link')
def step_impl(context):
    context.sign_up_page_object.click_login_link()


@then('SignUp Page: "Please enter a valid email address." error is no longer displayed')
def step_impl(context):
    error = context.sign_up_page_object.invalid_email_error_display()
    assert error == False, f"Error is still displayed"


@then('SignUp Page: "Please enter a valid email address." error is displayed')
def step_impl(context):
    context.sign_up_page_object.invalid_email_error_display()


@then('SignUp Page: I am taken to the sign up page')
def step_impl(context):
    context.sign_up_page_object.verify_url('https://jules.app/sign-up')
