from base.web_base import WebBase
from time import sleep
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    # 文章id
    article_id = None

    # 1. 点击信息管理
    def page_click_info_manage(self):
        # 1. 暂停时间
        sleep(1)
        # 2. 点击信息管理
        self.base_click(page.mis_info_manage)

    # 2. 点击内容审核
    def page_click_content_audit(self):
        # 1. 暂停时间
        sleep(1)
        # 2. 点击内容审核
        self.base_click(page.mis_content_audit)

    # 3. 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    # 4. 输入文章频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 5. 选择状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    # 6. 点击查询按钮
    def page_click_find(self):
        # 1. 点击查询按钮
        self.base_click(page.mis_find)
        # 2. 暂停时间
        sleep(2)

    # 7. 获取文章id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 8. 点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 9. 点击确认
    def page_click_confirm_pass(self):
        # 1. 暂停时间
        sleep(1)
        # 点击确认
        self.base_click(page.mis_confirm_pass)

    # 10. 组合发布文章业务方法
    def page_mis_audit(self, title, channel):
        log.info("正在调用审核文章业务方法，title: {} channel：{}".format(title, channel))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取的文章id为：", self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 11. 组装断言业务操作方法
    def page_assert_audit(self):
        log.info("正在调用断言业务操作方法")
        # 1. 暂停3秒
        sleep(3)
        # 2. 修改状态 ->审核通过
        self.page_click_status(click_text="审核通过")
        # 3. 点击查询按钮
        self.page_click_find()
        # 4. 判断当前页面是否存在指定元素 并 返回结果
        return self.web_base_is_exist(self.article_id)



