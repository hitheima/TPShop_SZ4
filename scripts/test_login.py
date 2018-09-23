from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name

import pytest

class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login"))
    def test_login(self, args):
        phone = args["phone"]
        password = args["password"]
        expect = args["expect"]

        self.page.home.click_mine()
        self.page.mine.click_sign_up_and_login()
        # 输入用户名
        self.page.sign_up_and_login.input_phone(phone)
        # 输入密码
        self.page.sign_up_and_login.input_password(password)
        # 点击登录
        self.page.sign_up_and_login.click_login()
        # 判断toast是否存在
        # if self.page.sign_up_and_login.is_toast_exits("登录成功"):
        #     assert True
        # else:
        #     assert False

        assert self.page.sign_up_and_login.is_toast_exits(expect)
