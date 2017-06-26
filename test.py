import unittest
from page import *
from selenium import webdriver

class TestMail (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.mail.ru")

    def test_input_login(self):
        main_page = MainPage(self.driver)
        main_page.is_login_mail()

        mail_page = MailPage(self.driver)
        mail_page.is_click_button_new_email()

        email_page = EmailPage(self.driver)
        email_page.is_send_new_email()

if __name__ == "__main__":
    unittest.main()
