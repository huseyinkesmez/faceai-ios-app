import unittest
import HtmlTestRunner
from appium import webdriver
from appium.options.common import AppiumOptions
from setup.capabilities import AppConfig
from pages.paywall_page import PaywallPage
import time


class TestPaywall(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            AppConfig.APPIUM_URL,
            options=AppiumOptions().load_capabilities(AppConfig.get_capabilities())
        )
        self.paywall = PaywallPage(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_paywall_screen_verification(self):
        time.sleep(3)

        self.assertTrue(self.paywall.wait_for_screen('//XCUIElementTypeStaticText[@name="Try Now"]', 10),
                       "Paywall screen did not load within 10 seconds")

        self.assertTrue(self.paywall.verify_all_elements(),
                       "Some paywall elements could not be verified. Check console for detaşl.")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name="paywall_test_report",
        report_title="Paywall Screen Test Report"
    ))





    
    