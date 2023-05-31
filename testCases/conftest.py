import pytest
from appium import webdriver

@pytest.fixture()
def setup():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='emulator-5554',
        appPackage='com.quatrixglobal.partner',
        appActivity='com.quatrixglobal.partner.MainActivity',
        noReset=True
    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, capabilities)

    driver.implicitly_wait(10)

    return driver