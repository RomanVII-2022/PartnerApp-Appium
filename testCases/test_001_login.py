from appium.webdriver.common.appiumby import AppiumBy
from utilities.customLog import custom_log
from PageObjects.loginPage import Login


class Test_001_login:
    logging = custom_log()

    def test_login_wrong_number(self, setup):
        login = Login(setup, self.logging)
        login.phone_input('71125425')
        login.password_input('123')
        login.login_btn()
        msg = login.error_msg()
        if msg == "That account doesn’t exist.":
            self.logging.debug("**** Expected message matched the actual meassage ***")
            assert True
        else:
            self.logging.debug("**** Expected message did not match the actual message ****")
            setup.save_screenshot('../Screenshots/wrongnumber.png')
            assert False


    def test_login_wrong_password(self, setup):
        login = Login(setup, self.logging)
        login.phone_input_clear()
        login.phone_input('711254254')
        login.password_input('1237557')
        login.login_btn()
        msg = login.error_msg()
        if msg == "Your account and/or password is incorrect.":
            self.logging.debug("**** Expected message matched the actual meassage ***")
            assert True
        else:
            self.logging.debug("**** Expected message did not match the actual message ****")
            setup.save_screenshot('../Screenshots/wrongpassword.png')
            assert False


    def test_login_wrong_credentials(self, setup):
        login = Login(setup, self.logging)
        login.phone_input_clear()
        login.phone_input('71125425')
        login.password_input('12335456')
        login.login_btn()
        msg = login.error_msg()
        if msg == "That account doesn’t exist.":
            self.logging.debug("**** Expected message matched the actual meassage ***")
            assert True
        else:
            self.logging.debug("**** Expected message did not match the actual message ****")
            setup.save_screenshot('../Screenshots/wrongcredentials.png')
            assert False


    def test_login(self, setup):
        login = Login(setup, self.logging)
        login.phone_input_clear()
        login.phone_input('711254254')
        login.password_input('123')
        login.login_btn()
        try:
            setup.find_element(AppiumBy.ID, "android:id/button1")
            self.logging.debug("**** Login was successfull ****")
            assert True
        except:
            self.logging.debug("**** Something went wrong. Login was not successful ****")
            setup.save_screenshot('../Screenshots/login.png')
            assert False
        else:
            login.info_btn()
            login.using_app()
            login.all_time()
            login.back_btn()
            login.info_btn()
            login.info_btn()
            self.logging.debug("**** Access to the home page was successfull ****")

    








