from PageObjects.accountPage import AccountPage
from utilities.customLog import custom_log
import time


class Test_002_Account:
    logging = custom_log()
    
    def test_edit_account(self, setup):
        account = AccountPage(setup, self.logging)
        account.navigation_bar()
        account.account_link()
        account.scroll_screen()
        account.edit_btn()
        account.national_id("123456789")
        account.kra_pin('1234455677778')
        account.box("01000")
        account.city("Nairobi")
        account.postal_code("01000")
        account.street("Adams Archade")
        account.save_btn()