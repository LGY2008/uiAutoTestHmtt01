
from base.web_base import WebBase
import page
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入 标题
    def page_input_title(self, title):
        sleep(1)
        self.base_input(page.mp_title, title)

    # 输入 内容
    def page_input_content(self, content):
        # 1. 切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        sleep(1)
        # 2. 输入内容
        self.base_input(page.mp_content, content)
        # 3. 回到默认目录
        self.driver.switch_to.default_content()

    # 选择 封面
    def page_click_cover(self):
        sleep(1)
        self.base_click(page.mp_cover)

    # 选择 频道
    def page_click_channel(self):
        # 调用WebBase封装方法
        self.web_base_click_element(placeholder_text="请选择", click_text=page.channle)

    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取 发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合审核文章业务方法
    def page_mp_article(self, title, content):
        log.info("正在调用发布文章业务方法，文章标题：{} 文章内容：{}".format(title,content))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
