from typing import Dict, Any

class AppConfig:
    @staticmethod
    def get_capabilities() -> Dict[str, Any]:
        return {
            "platformName": "iOS",
            "automationName": "XCUITest",
            "deviceName": "KESMEZ's iPhone 13",
            "udid": "00008110-000A03A8020A801E",
            "bundleId": "co.koiapps.faceai",
            "xcodeOrgId": "xxxxxxxxxxxxxxx", # not necessary
            "xcodeSigningId": "iPhone Developer"
        }

    APPIUM_URL = 'http://localhost:4723/wd/hub' 