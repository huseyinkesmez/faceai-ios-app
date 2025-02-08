from pages.base import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.accessibility_ids = {
            'close_button': 'closeDark'
        }
        
        self.xpath_elements = {
            'discover': '//XCUIElementTypeStaticText[@name="Discover"]',
            'movie_characters': '//XCUIElementTypeStaticText[@name="Movie Characters"]',
            'first_movie_character': '//XCUIElementTypeCollectionView/XCUIElementTypeScrollView[4]/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]',
            'swap_faces': '//XCUIElementTypeStaticText[@name="Swap Faces For a Year!"]'
        }

    def verify_all_elements(self) -> bool:
        success = True
        failed_elements = []

        for key in self.accessibility_ids:
            if not self.find_element(self.accessibility_ids[key], key):
                failed_elements.append(f"Accessibility ID: {key}")
                success = False

        for key in self.xpath_elements:
            if not self.find_element(self.xpath_elements[key], key):
                failed_elements.append(f"XPath: {key}")
                success = False
        
        if not success:
            print(f"\nFailed to verify elements: {', '.join(failed_elements)}")
        
        return success

    def click_by_accessibility(self, element_key: str) -> bool:
        locator = self.accessibility_ids.get(element_key)
        return self.click_element(locator, element_key)

    def click_by_xpath(self, element_key: str) -> bool:
        locator = self.xpath_elements.get(element_key)
        return self.click_element(locator, element_key)

    def verify_text_visible(self, text_key: str) -> bool:
        locator = self.xpath_elements.get(text_key)
        return self.find_element(locator, text_key)

    def scroll_to_text(self, text_key: str) -> bool:

        locator = self.xpath_elements.get(text_key)
        return self.scroll_to_element(locator, text_key)

