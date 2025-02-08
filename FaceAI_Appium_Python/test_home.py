import unittest
import HtmlTestRunner
from appium import webdriver
from appium.options.common import AppiumOptions
from setup.capabilities import AppConfig
from pages.home_page import HomePage


class TestHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            AppConfig.APPIUM_URL,
            options=AppiumOptions().load_capabilities(AppConfig.get_capabilities())
        )
        self.home = HomePage(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_home_screen_navigation(self):
        # Close paywall
        self.assertTrue(self.home.click_by_accessibility('close_button'),
                       "Could not close paywall screen")

        # Verify discover screen
        self.assertTrue(self.home.verify_text_visible('discover'),
                       "Could not verify Discover text")

        # Scroll to movie characters
        self.assertTrue(self.home.scroll_to_text('movie_characters'),
                       "Could not scroll to Movie Characters section")

        # Click first movie character
        self.assertTrue(self.home.click_by_xpath('first_movie_character'),
                       "Could not click first movie character")

        # Verify swap faces screen
        self.assertTrue(self.home.verify_text_visible('swap_faces'),
                       "Could not verify Swap Faces text. Check console for details.")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name="home_test_report",
        report_title="Home Screen Test Report"
    )) 