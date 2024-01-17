import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url_2 = "https://www.livofy.com/fitness-health-calculators/food-calorie-calculator"
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


def uzturvertiba(tips, food):
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, f"{tips}0"))
        )
        return round(float(element.text)*100, 2)
    except:
        mekletajs(food[:-1]) if len(food) > 1 else None


def mekletajs(food): # string kā arguments
    driver.get(url_2)
    find_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "keywordsearch")) # atrod search lauciņu
    )
    find_2.clear() # notīra lauku
    find_2.send_keys(f"{food}") # ievada ēdina nosaukumu
    button = driver.find_element(By.ID, "searchbutton") # atrod search pogu
    button.click() # nospiež search pogu
    kalorijas = uzturvertiba("Calories", food) # izsauc funkciju kas nolasīs uzturvērtību 100g produkta
    tauki = uzturvertiba("Fat", food)
    oglhidrati = uzturvertiba("Carbs", food)
    proteini = uzturvertiba("Protein", food)
    kalorijas = uzturvertiba("Calories", food) # izsauc funkciju vēlreiz, lai kalorijas nebūtu None
    return [kalorijas, tauki, oglhidrati, proteini]

