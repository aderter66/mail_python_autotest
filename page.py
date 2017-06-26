from locators import *

class Page(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(Page):
    def is_writing_login(self):
        self.driver.find_element(*MainPageLocators.login_label)\
            .send_keys(*MainPageLocators.login_text)

    def is_choosing_mail(self):
        self.driver.find_element(*MainPageLocators.login_mail).click()
        self.driver.find_element(*MainPageLocators.login_choose_mail).click()

    def is_writing_pass(self):
        self.driver.find_element(*MainPageLocators.password_label)\
            .send_keys(*MainPageLocators.password_text)

    def is_click_login_button(self):
        self.driver.find_element(*MainPageLocators.login_button).click()

    def is_login_mail(self):
        self.is_writing_login()
        self.is_choosing_mail()
        self.is_writing_pass()
        self.is_click_login_button()
        return MailPage(self.driver)

class MailPage(Page):

    def is_click_button_new_email(self):
        self.driver.find_element(*MailPageLocators.new_email_button).click()
        return EmailPage(self.driver)

class EmailPage(Page):
    def is_write_address(self):
        self.driver.find_element(*NewEmailLocators.address_label)\
            .send_keys(*NewEmailLocators.email_address)

    def is_write_theme(self):
        self.driver.find_element(*NewEmailLocators.theme_label)\
            .send_keys(*NewEmailLocators.email_theme)

    def is_write_text(self):
        self.driver.switch_to_default_content()
        frame = self.driver.find_element(*NewEmailLocators.email_place)
        self.driver.switch_to_frame(frame)
        self.driver.find_element(*NewEmailLocators.email_label).send_keys(*NewEmailLocators.email)

    def is_push_send_button(self):
        self.driver.switch_to_default_content()
        self.driver.find_element(*NewEmailLocators.send_button).click()

    def is_send_new_email(self):
        self.is_write_address()
        self.is_write_theme()
        self.is_write_text()
        self.is_push_send_button()
        return SuccesPage(self.driver)

class SuccesPage(Page):
    pass