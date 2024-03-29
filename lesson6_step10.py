
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, input.first[required])
        input1.send_keys("Мой ответ")
    input2 = browser.find_element(By.CSS_SELECTOR, input.second[required])
        input2.send_keys("Мой ответ")
    input3 = browser.find_element(By.CLASS_NAME, "first")
        input3.send_keys("Мой ответ")
    input4 = browser.find_element(By.CLASS_NAME, "second")
        input4.send_keys("Мой ответ")
    input5 = browser.find_element(By.CLASS_NAME, "third")
        input5.send_keys("Мой ответ")
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()