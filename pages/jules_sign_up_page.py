from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SignUpPage(BasePage):
    PERSONAL_OPTION = (By.XPATH, '//input[@value="personal"]')
    CONTINUE_BTN = (By.XPATH, '//div/button')
    INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div')
    INVALID_EMAIL_ERROR = (By.XPATH, '//div/p')
    LOG_IN_LINK = (By.XPATH, '//a[@href="/sign-in"]')

    def account_option_selection(self, option=PERSONAL_OPTION):
        self.chrome.find_element(*option).click()

    def click_continue(self):
        WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.CONTINUE_BTN))
        self.click_elem(self.CONTINUE_BTN)

    def input_info(self, info):
        WebDriverWait(self.chrome, 10).until(
            EC.presence_of_element_located(self.INPUT))
        input_field = self.chrome.find_element(*self.INPUT)
        input_field.send_keys(info)
        input_field.send_keys(Keys.ENTER)

    def invalid_email_error_display(self):
        WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.INVALID_EMAIL_ERROR))
        error = self.chrome.find_element(*self.INVALID_EMAIL_ERROR)
        assert error.is_displayed(), f"Error: Invalid email error message not displayed"

    def clear_input(self):
        self.chrome.find_element(*self.INPUT).clear()

    def click_login_link(self):
        self.click_elem(self.LOG_IN_LINK)
