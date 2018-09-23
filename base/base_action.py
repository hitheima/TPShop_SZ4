from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def click(self, feature):
        self.find_element(feature).click()

    def find_toast(self, key_word):
        feature = By.XPATH, "//*[contains(@text,'" + key_word + "')]"
        return self.find_element(feature, timeout=5, poll=0.1).text


