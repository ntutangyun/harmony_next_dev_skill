# 使用Hypium实现ArkWeb自动化测试

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-hypium-autotests_

Selenium主要用于Web应用程序的自动化测试，核心功能是模拟用户在浏览器中的操作，例如点击按钮、输入文本、导航页面等。

pip install selenium

3.集成ChromeDriver驱动

ChromeDriver充当了Selenium WebDriver和Web页面之间的中介。通过Selenium发送命令时，ChromeDriver会将这些命令转换为Web内核能够理解的协议，并将响应返回给Selenium。ArkWeb基于谷歌Chromium内核开发，系统版本与Chromium版本的对应关系参考：ArkWeb简介约束与限制。访问ChromeDriver官方网站ChromeDriver下载|Chrome for Developers，获取与Chromium版本对应的ChromeDriver。

首先将ChromeDriver集成到测试工程的resource文件夹下，然后调用WebDriverSetupTool类中的set_chromedriver_exe_path方法指定chromedriver文件的存放路径或者调用set_chromedriver_exe_search_path方法指定chromedriver所在文件夹的路径。

self.web_tools = WebDriverSetupTool(self.driver)
# 使用set_chromedriver_exe_path指定chromedriver路径，需指定到对应版本的可执行chromedriver文件
self.web_tools.set_chromedriver_exe_path(r"D:\WebAutoTest\resource\web_debug_tools\chromedriver_132\chromedriver.exe")
self.web_tools = WebDriverSetupTool(self.driver)
# 使用set_chromedriver_exe_search_path方法指定chromedriver所在文件夹，Hypium在指定的文件夹寻找对应版本的chromedriver文件
self.web_tools.set_chromedriver_exe_search_path(r"D:\WebAutoTest\resource\web_debug_tools")
说明

使用set_chromedriver_exe_search_path方法指定chromedriver所在文件夹的路径时，下层文件夹命名规则为chromedriver_版本号，参考下图。

示例代码

参考以下代码完成ArkWeb页面的自动化测试，先初始化Selenium的webdriver，后通过webdriver与Web页面交互的API，实现导航页面、查找页面元素操作。

webdriver更多使用方法参考Selenium官方文档：驱动会话 | Selenium。

from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import UiDriver, BY
from hypium.webdriver.webdriver_setup_tool import WebDriverSetupTool


class ArkWeb_AutoTests(TestCase):
    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()
        self.web_tools = WebDriverSetupTool(self.driver)
        # 设置chromedriver存放路径
        self.web_tools.set_chromedriver_exe_search_path(r"D:\WebAutoTest\resource\web_debug_tools")
        # 使用应用包名连接到指定应用的webview页面
        self.web_tools.connect("com.huawei.hmos.browser")
        # 初始化Selenium的webdriver
        self.web_driver = self.web_tools.driver


    def setup(self):
        pass
        
    def process(self):
        # 导航页面：使用Selenium的webdriver访问https://developer.huawei.com/网站
        self.web_driver.get("https://developer.huawei.com/")
        # 查找页面元素：使用Selenium的webdriver查找页面ID为th的元素
        self.web_driver.find_element(BY.ID, "th")


    def teardown(self):
        # 使用结束需要调用webdriver_setup_tool中的close方法关闭web_tools建立的连接
        self.web_tools.close()
定位与解决Web白屏问题
Background Tasks Kit（后台任务开发服务）
