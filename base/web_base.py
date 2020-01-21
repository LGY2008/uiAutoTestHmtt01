from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class WebBase(Base):
    """以下为你web项目专属方法"""

    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        log.info("正在调用web专属点击封装方法")
        # 1. 点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2. 暂停
        sleep(1)
        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        log.info("正在调用查找页面是否存在指定元素：{} 方法".format(text))
        # 1. 组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2. 找元素
        try:
            # 1. 找元素 修改查找元素时间 3
            self.base_find(loc, timeout=3)
            # 2. 输出找到信息
            print("找到：{} 元素啦！".format(loc))
            # 3. 返回 True
            return True
        except:
            # 1. 输出未找到信息
            print("没有找到：{} 元素！".format(loc))
            # 2. 返回False
            return False