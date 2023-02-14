import time

from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SignInPage(BasePage):
    EMAIL_FIELD = (By.XPATH, '//input[@type="text"]')
    PASS_FIELD = (By.XPATH, '//input[@type="password"]')
    PASS_ERROR = (By.XPATH, '//div/p')
    LOGIN_BTN = (By.XPATH, '//div/button')
    SIGN_UP_LINK = (By.XPATH, '//a[@href="/sign-up"]')

    def sign_in_input_email(self, email):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys(
            email)

    def sign_in_input_pass(self, password):
        field = self.chrome.find_element(*self.PASS_FIELD)
        field.send_keys(password)

    def sign_in_clear_pass(self):
        self.chrome.find_element(*self.PASS_FIELD).send_keys(Keys.BACKSPACE)

    def pass_error_display(self):
        WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.PASS_ERROR))
        error = self.chrome.find_element(*self.PASS_ERROR)
        assert error.is_displayed(), f"Error: Password error message not displayed"

    def check_button_status(self):
        btn_enabled = self.chrome.find_element(*self.LOGIN_BTN).is_enabled()
        assert btn_enabled == False, f"Error, button is enabled, should be disabled"

    def click_sign_up_link(self):
        self.click_elem(self.SIGN_UP_LINK)
