from pages.base import BasePage


class PaywallPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.accessibility_ids = {
            'popular': 'POPULAR',
            'week': '1  Week',
            'weekly_price': '₺349,99',
            'yearly_price': '₺2.299,99 Per Year',
            'best_value': 'BEST VALUE',
            'one_year': '1  Year',
            'top_choice': 'TOP CHOICE',
            'infinity': '∞',
            'subscription_view': '_TtGCVV12SevenAppsKit3SAK7POLYIAP37PolymorphicSubscriptionView'
        }
        
        self.xpath_elements = {
            'try_now': '//XCUIElementTypeStaticText[@name="Try Now"]',
            'privacy_policy': '//XCUIElementTypeStaticText[@name="Privacy Policy"]',
            'restore': '//XCUIElementTypeStaticText[@name="Restore"]',
            'terms': '//XCUIElementTypeStaticText[@name="Terms of Use"]'
        }

    def verify_all_elements(self) -> bool:
        success = True
        failed_elements = []

        main_elements = ['try_now', 'privacy_policy', 'restore', 'terms']
        for key in main_elements:
            if not self.find_element(self.xpath_elements[key], key):
                failed_elements.append(f"XPath: {key}")
                success = False
        

        pricing_elements = [
            'popular',
            'week',
            'weekly_price',
            'yearly_price',
            'best_value',
            'one_year',
            'top_choice',
            'infinity'
        ]
        for key in pricing_elements:
            if not self.find_element(self.accessibility_ids[key], key):
                failed_elements.append(f"Accessibility ID: {key}")
                success = False
        
        if not success:
            print(f"\nFailed to verify elements: {', '.join(failed_elements)}")
        
        return success