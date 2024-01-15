import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url_2 = "https://caloriecontrol.org/healthy-weight-tool-kit/food-calorie-calculator/"
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


def uzturvertiba(tips):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f'[data-title="{tips}"]'))
    )
    return element.text

def mekletajs(food): # string kā arguments
    driver.get(url_2)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'cky-btn-accept')) # akceptē cookies
    )
    button.click() 
    find_2 = driver.find_element(By.ID, "keyword") # atrod search lauciņu
    find_2.clear() # notīra lauku
    find_2.send_keys(f"{food}") # ievada ēdina nosaukumu
    button = driver.find_element(By.ID, "btnsearch") # atrod search lauciņu
    button.click()
    time.sleep(3)
    kalorijas = uzturvertiba("Calories")
    tauki = uzturvertiba("Fat")
    oglhidrati = uzturvertiba("Carbs*")
    proteini = uzturvertiba("Protein")
    return kalorijas, tauki, oglhidrati, proteini