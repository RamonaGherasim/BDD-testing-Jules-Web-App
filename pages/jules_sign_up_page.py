import time

from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SignUpPage(BasePage):
    PERSONAL_OPTION = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BTN = (By.XPATH, '//div/button')
    INPUT = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    INVALID_EMAIL_ERROR = (By.XPATH, '//div/p')
    LOG_IN_LINK = (By.XPATH, '//a[@href="/sign-in"]')

    def account_option_selection(self):
        self.click_elem(self.PERSONAL_OPTION)

    def click_continue(self):
        WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.CONTINUE_BTN))
        self.click_elem(self.CONTINUE_BTN)

    def input_info(self, info):
        WebDriverWait(self.chrome, 10).until(
            EC.presence_of_element_located(self.INPUT))
        input_field = self.chrome.find_element(*self.INPUT)
        input_field.send_keys(info)

    def enter(self):
        self.input_info(Keys.ENTER)

    def invalid_email_error_display(self):
        try:
            WebDriverWait(self.chrome, 5).until(
                EC.presence_of_element_located(self.INVALID_EMAIL_ERROR))
            error = self.chrome.find_element(*self.INVALID_EMAIL_ERROR).text
        except:
            return False
        assert error == "Please enter a valid email address.", f"Error: {error}"

    def clear_input(self):
        time.sleep(3)
        self.input_info(Keys.CONTROL + 'a')
        self.input_info(Keys.BACKSPACE)

    def click_login_link(self):
        self.click_elem(self.LOG_IN_LINK)
