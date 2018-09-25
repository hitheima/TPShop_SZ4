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

    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False

    # -------- 以下仅仅是这个项目会用到

    def is_login(self):
        """
        需要点击齿轮后进行验证
        :return:
        """
        title_feature = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

        is_user_login = None

        if self.find_element(title_feature).text == "登录":
            is_user_login = False
        else:
            is_user_login = True

        self.driver.press_keycode(4)

        return is_user_login
