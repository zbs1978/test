from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Мой ответ")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Мой ответ")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("Мой ответ")
        input4 = browser.find_element(By.CLASS_NAME, "first")
        input4.send_keys("Мой ответ")
        input5 = browser.find_element(By.CLASS_NAME, "second")
        input5.send_keys("Мой ответ")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Мой ответ")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Мой ответ")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("Мой ответ")
        input4 = browser.find_element(By.CLASS_NAME, "first")
        input4.send_keys("Мой ответ")
        input5 = browser.find_element(By.CLASS_NAME, "second")
        input5.send_keys("Мой ответ")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()