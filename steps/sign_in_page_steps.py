from behave import *


@given('SignIn Page: That I am on the jules.app sign in page')
def step_impl(context):
    context.sign_in_page_object.navigate_sign_in_page()


@when('SignIn Page: I input a correct email')
def step_impl(context):
    context.sign_in_page_object.sign_in_input_email("ramona@yahoo.com")


@when('SignIn Page: I leave the password field empty')
def step_impl(context):
    context.sign_in_page_object.sign_in_input_pass("1")
    context.sign_in_page_object.sign_in_clear_pass()


@when('SignIn Page: I click on the "Sign up" link')
def step_impl(context):
    context.sign_in_page_object.click_sign_up_link()


@then('SignIn Page: "Please enter your password!" error is displayed')
def step_impl(context):
    context.sign_in_page_object.pass_error_display()


@then('SignIn Page: The log in button is disabled')
def step_impl(context):
    context.sign_in_page_object.check_button_status()
