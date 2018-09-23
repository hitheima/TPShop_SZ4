from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class MinePage(BaseAction):

    sign_up_and_login_button = By.XPATH, "//*[@text='登录/注册']"

    @allure.step(title="我的-点击登录/注册")
    def click_sign_up_and_login(self):
        self.click(self.sign_up_and_login_button)
