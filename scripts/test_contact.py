import allure
import pytest


class TestContact:

    # 添加严重级别
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step('登录的测试脚本')
    def test_login(self):
        allure.attach('输入用户名', '测试输入了：hello,1,str')
        print('输入用户名')
        allure.attach('输入密码', '输入密码的描述')
        print('输入密码')
        allure.attach('登录', '登录的描述')
        print('点击登录')

        assert 1
