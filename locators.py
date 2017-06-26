# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    login_button = (By.ID, 'mailbox__auth__button')
    login_mail = (By.XPATH, ".//div[@id='js-mailbox-auth']"
                           "/form/div/div/select[@name='Domain']/option")
    login_choose_mail = (By.XPATH, ".//option[@value='mail.ru']")

    login_label = (By.ID, 'mailbox__login')
    password_label = (By.ID, 'mailbox__password')

    login_text = "amurgashev"
    password_text = "753dfxms"

class MailPageLocators(object):
    new_email_button = (By.XPATH, "//div[@class='b-toolbar__item']/a[@href]")

class NewEmailLocators(object):
    address_label = (By.XPATH, "//div[@class='compose-head__field']/div/div")
    theme_label = (By.XPATH, "//div[@class='compose-head__cell']/div/input[@class='b-input']")
    email_place = (By.XPATH, "//tr[@class='mceFirst mceLast']/td/iframe")
    email_label = (By.XPATH, "//body[@id='tinymce']")
    send_button = (By.XPATH, "//div[@data-name='send']")

    email_address = " aderter66@yandex.ru"
    email_theme = u"Тестовое письмо"
    email = u"Отправка тестового письма"
