import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpArticle:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3. 获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4. 获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 2. 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3. 测试发布文章方法
    @pytest.mark.parametrize("title,content,expect,channel", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect, channel):
        print("发布文章所属频道为：", channel)
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        try:
            # 断言
            assert expect == self.article.page_get_info()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise
