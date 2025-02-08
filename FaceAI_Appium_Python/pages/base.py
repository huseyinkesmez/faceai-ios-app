from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from typing import Tuple

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _get_locator(self, locator: str) -> Tuple[str, str]:
        if locator.startswith('//'):
            return (AppiumBy.XPATH, locator)
        else:
            return (AppiumBy.ACCESSIBILITY_ID, locator)

    def wait_for_screen(self, locator: str, timeout: int = 10) -> bool:
        try:
            locator_type, locator_value = self._get_locator(locator)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            print(f"Screen loaded within {timeout} seconds")
            return True
        except TimeoutException:
            print(f"Screen did not load within {timeout} seconds")
            return False

    def find_element(self, locator: str, description: str) -> bool:
        try:
            locator_type, locator_value = self._get_locator(locator)
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            print(f"{description} found")
            return True
        except TimeoutException:
            print(f"Error: {description} not found using {locator}!")
            return False

    def click_element(self, locator: str, description: str) -> bool:
        try:
            locator_type, locator_value = self._get_locator(locator)
            element = self.wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            element.click()
            print(f"Clicked on {description}")
            return True
        except TimeoutException:
            print(f"Error: Could not click {description} using {locator}!")
            return False

    def scroll_to_element(self, locator: str, description: str, max_scrolls: int = 10) -> bool:
        locator_type, locator_value = self._get_locator(locator)
        
        for _ in range(max_scrolls):
            try:
                element = self.driver.find_element(locator_type, locator_value)
                if element.is_displayed():
                    print(f"Found {description} after scrolling")
                    return True
            except:
                pass
            
            self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        
        print(f"Error: Could not find {description} after {max_scrolls} scrolls")
        return False