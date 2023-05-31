from appium.webdriver.common.appiumby import AppiumBy
import time

class Login:
    def __init__(self, driver, logging):
        self.driver = driver
        self.logging = logging

    def alert_pop(self):
        try:
          allowBtn = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
          allowBtn.click()
          self.logging.debug("**** Alert button was clicked successfully ****") 
        except:
            self.logging.debug(f"**** Alert button was not found. ****") 

    
    def phone_input(self, phone):
        try:
            input_field = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText")
            input_field.clear()
            input_field.send_keys(phone)
            self.logging.debug("**** Phone number was entered successfully ****")
        except:
            self.logging.debug(f"**** Phone number was not entered. ****")


    def phone_input_clear(self):
        try:
            input_field = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.EditText")
            input_field.clear()
            self.logging.debug("**** Phone number field was cleared successfully ****")
        except:
            self.logging.debug(f"**** Phone number was not entered. ****")


    
    def password_input(self, password):
        try:
            input_field = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.EditText")
            input_field.clear()
            input_field.send_keys(password)
            self.logging.debug("**** Password was entered successfully ****")
        except:
            self.logging.debug(f"**** Password was not entered. ****")



    def login_btn(self):
        try:
            btn = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[4]")
            btn.click()
            self.logging.debug("**** Login button was clicked successfully ****")
        except:
            self.logging.debug(f"**** Login button was not found. ****")


    def error_msg(self):
        try:
            msg = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
            txt = msg.text
            self.logging.debug("**** Error message was found successfully ****")
            return txt
        except:
            self.logging.debug(f"**** Error message was not found. ****")
            return

    def forgot_password(self):
        try:
            forgot_link = self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView")
            forgot_link.click()
            self.logging.debug("**** Forgot password link was clicked successfully ****")
        except:
            self.logging.debug(f"**** Forgot password link was not found. ****")


    def info_btn(self):
        try:
          info = self.driver.find_element(AppiumBy.ID, "android:id/button1")
          info.click()
          self.logging.debug("**** Important info button was clicked successfully ****")
        except:
            self.logging.debug(f"**** Important info button was not found. ****")

    
    def using_app(self):
        try:
            usingApp = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            usingApp.click()
            self.logging.debug("**** Permission controller button was clicked successfully ****")
        except:
            self.logging.debug(f"**** Permission controller button was not found.")

    def all_time(self):
        try:
            allTime = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/allow_always_radio_button")
            allTime.click()
            self.logging.debug("*** All time button was clicked successfully ****")
        except:
            self.logging.debug(f"**** All time button was not found.")


    def back_btn(self):
        try:
            back = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
            back.click()
            self.logging.debug("**** Back button was clicked successfully ****")
        except:
            self.logging.debug(f"**** Back button was not found. ****")