from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):
    def verify_url(self, expected_url):
        actual_url = self.chrome.current_url
        assert actual_url == expected_url, f"Error: actual url {actual_url}," \
                                           f"expected url {expected_url}"

    def navigate_sign_up_page(self):
        self.chrome.get("https://jules.app/sign-up")

    def navigate_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def click_elem(self, element):
        self.chrome.find_element(*element).click()
