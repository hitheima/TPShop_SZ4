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

    def scroll_page_one_time(self, direction="up"):
        """

        :param direction:
            up：从下往上
            down：从上往下
            left：从右往左
            right：从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        down_x = center_x
        down_y = screen_height * 0.75
        up_x = center_x
        up_y = screen_height * 0.
        left_x = screen_width * 0.25
        left_y = center_y
        right_x = screen_width * 0.75
        right_y = center_y

        if direction == "up":
            self.driver.swipe(down_x, down_y, up_x, up_y, 3000)
        elif direction == "down":
            self.driver.swipe(up_x, up_y, down_x, down_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("您输入的参数有误，请检查，direction参数必须是up/down/left/right")

    def is_feature_exist_scroll_page(self, feature):
        """
        根据特征，先找，如果没有找到，滑动，如果找到直接返回True，如果到底部还没有找到，则返回false
        :param feature:
        :return:
        """
        page_source = ""
        while True:
            if self.driver.page_source == page_source:
                return False
            try:
                self.find_element(feature)
                return True
            except Exception:
                page_source = self.driver.page_source
                self.scroll_page_one_time()


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
