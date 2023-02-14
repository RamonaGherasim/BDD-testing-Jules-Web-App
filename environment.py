from browser import Browser
from pages.jules_sign_in_page import SignInPage
from pages.jules_sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.sign_in_page_object = SignInPage()
    context.sign_up_page_object = SignUpPage()


def after_all(context):
    context.browser.close()