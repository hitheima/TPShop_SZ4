from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name

import pytest

class TestLogin:

    def setup(self):
        self.driver = init_driver()

        self.page = Page(self.driver)

    # @pytest.mark.skipif(True, reason="")
    # @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login"))
    # def test_login(self, args):
    #     phone = args["phone"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     self.page.home.click_mine()
    #     self.page.mine.click_sign_up_and_login()
    #     # 输入用户名
    #     self.page.sign_up_and_login.input_phone(phone)
    #     # 输入密码
    #     self.page.sign_up_and_login.input_password(password)
    #     # 点击登录
    #     self.page.sign_up_and_login.click_login()
    #     # 判断toast是否存在
    #     # if self.page.sign_up_and_login.is_toast_exits(expect):
    #     #     assert True
    #     # else:
    #     #     assert False
    #
    #     assert self.page.sign_up_and_login.is_toast_exits(expect)

    @pytest.mark.parametrize("args", analyze_with_file_name("login", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        """
        只输入用户名或脚本
        :return:
        """
        phone = args["phone"]
        password = args["password"]

        self.page.home.click_mine()
        self.page.mine.click_sign_up_and_login()

        self.page.sign_up_and_login.input_phone(phone)
        self.page.sign_up_and_login.input_password(password)

        assert not self.page.sign_up_and_login.is_login_button_enabled()

        # # 判断登录按钮的状态
        # if self.page.sign_up_and_login.is_login_button_enabled() == False:
        #     assert True
        # else:
        #     assert False

        # # 按钮状态如果为真
        # if true == False:
        #     assert True
        # else:
        #     assert False
        #
        # # 按钮状态如果为假
        # if false == False:
        #     assert True
        # else:
        #     assert False
        #
        #     按钮为 true 返回 为 false
        #     按钮为 false 返回 为 True





