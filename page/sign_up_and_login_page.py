from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class SignUpAndLoginPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="登录/注册-输入手机号")
    def input_phone(self, text):
        allure.attach("输入内容：", text)
        self.input(self.phone_edit_text, text)

    @allure.step(title="登录/注册-输入密码")
    def input_password(self, text):
        allure.attach("输入内容：", text)
        self.input(self.password_edit_text, text)

    @allure.step(title="登录/注册-点击登录")
    def click_login(self):
        self.click(self.login_button)

    def is_login_button_enabled(self):
        return self.is_feature_enabled(self.login_button)
