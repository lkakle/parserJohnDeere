import JohnDeereCard 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent as UA
import time

#Обход защиты
UA = UA.random

#настройки окна
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")  # Отключаем GPU для стабильности
options.add_argument("--window-size=1920,1080")  # Размер окна
options.add_argument(f"user-agent={UA}")

#пусть до драйвера хром, создание игрока
driver = webdriver.Chrome( options=options)

Completed = 13

#Основной Скрипт

links = ["https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=17&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=18&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=19&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=20&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=21&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=22&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=23&sort=RELEVANCE", "https://shop.deere.com/us/Mowing-Cutting-Parts/Cutterhead-Parts/c/2485/?page=24&sort=RELEVANCE"]

for link in links:
    driver.get(link)
    time.sleep(7)
    for i in range(4):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)

    elements = driver.find_elements(By.XPATH, '//a[@data-testid="productCardName"]')

    JohnDeereCard.card(elements)
    time.sleep(120)
    Completed += 1
    print(f"Завершено! {Completed} из 24.")

print("Конец.")