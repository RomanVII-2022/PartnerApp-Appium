from appium.webdriver.common.appiumby import AppiumBy


class PartnersPage:
    def __init__(self, driver, logging):
        self.driver = driver
        self.logging = logging


    def navigation_bar(self):
        try:
            menuBtn = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button/android.widget.ImageView")
            menuBtn.click()
            self.logging.debug("**** Menu button was clicked successfully ****")
        except:
            self.logging.debug("**** Menu button was not found. Error: Something went wrong")

    
    def partners(self):
        try:
            partnersBtn = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.Button/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")
            partnersBtn.click()
            self.logging.debug("**** Partners link button was clicked successfully ****")
        except:
            self.logging.debug("**** Partners link button was not clicked. Something went wrong ****")