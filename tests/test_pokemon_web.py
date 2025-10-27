import pytest
import requests
from loguru import logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://pokemonbattle-stage.ru'

def test_browser(browser):
   
    browser.get(URL)


   # ищем по селектору инпут "Email", кликаем по нему и вводим значение 
    email_input = WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ' [id="k_email"]')))
    email_input.click()
    email_input.send_keys('EMAIL')

    # ищем по селектору инпут "Password", кликаем по нему и вводим значение пароля
    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[id="k_password"]')
    password_input.click()
    password_input.send_keys('PASSWORD')

	# ищем по селектору кнопку "Войти" и кликаем по ней
    enter = browser.find_element(by=By.CSS_SELECTOR, value='[class*="k_form_send_auth"]')
    enter.click()


    # ищем элемент на странице, который содержит ID тренера
    trainer_id = WebDriverWait(browser, timeout=10, poll_frequency=2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="header_card_trainer_id_num"]')))


    # сравниваем полученный ID из кода теста с ID   тренера
    assert trainer_id.text == '3237', 'Unexpected ID trainer' 

    assert True, ''


CASES = [
    ('1', 'EMAIL', 'PASSWORD', 'Введите корректную почту'),
    ('2', 'EMAIL', 'PASSWORD', 'Неверные логин или пароль'),
    ('3', 'EMAIL', 'PASSWORD', 'Введите корректную почту'),
    ('4', '', 'PASSWORD', 'Введите почту'),
    ('5', 'EMAIL', '', 'Введите пароль'),
]

@pytest.mark.parametrize('case_number, email, password, alerts', CASES)
def test_negative_case(case_number, email, password, alerts, browser):
   
    logger.info(f'CASE : {case_number}')
    browser.get(URL)
   

   # ищем по селектору инпут "Email", кликаем по нему и вводим значение 
    email_input = browser.find_element(by=By.CSS_SELECTOR, value=' [id="k_email"]')
    email_input.click()
    email_input.send_keys(email)

    # ищем по селектору инпут "Password", кликаем по нему и вводим значение пароля
    password_input = browser.find_element(by=By.CSS_SELECTOR, value='[id="k_password"]')
    password_input.click()
    password_input.send_keys(password)

	# ищем по селектору кнопку "Войти" и кликаем по ней
    enter = browser.find_element(by=By.CSS_SELECTOR, value='[class*="k_form_send_auth"]')
    enter.click()

    alerts_message = WebDriverWait(browser, timeout=1, poll_frequency=2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="auth__error"]'))
)
    alert_text = alerts_message.text
  
    assert alert_text == alerts, 'Unexpected alerts'
 
