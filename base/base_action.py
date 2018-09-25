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
        """
        通过toast上的部分文字，获取全部的内容
        :param key_word:
        :return:
        """
        message = By.XPATH, "//*[contains(@text,'%s')]" % key_word
        return self.find_element(message, timeout=5, poll=0.1).text

    def is_toast_exist(self, key_word):
        """
        通过toast的部分文字，获取这个toast是否存在
        :return:
        """
        try:
            self.find_toast(key_word)
            return True
        except:
            return False

    def is_feature_enabled(self, feature):
        return self.find_element(feature).get_attribute("enabled") == "true"

        # if self.find_element(feature).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False
