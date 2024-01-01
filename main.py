import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
url = "https://www.google.com/search?q=tulkot%C4%81js&sca_esv=594646980&sxsrf=AM9HkKkT8UtYVNOtVlqEq8j6qPwYofAl0Q%3A1703974912971&ei=AJiQZYP4Os-OwPAPqLOUiAY&udm=&ved=0ahUKEwiD-JKbmbiDAxVPBxAIHagZBWEQ4dUDCBE&uact=5&oq=tulkot%C4%81js&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnR1bGtvdMSBanMyChAjGIAEGIoFGCcyChAjGIAEGIoFGCcyBRAAGIAEMgUQABiABDILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMggQABiABBjLATIFEAAYgAQyBRAAGIAEMgUQABiABEiAA1AAWABwAHgBkAEAmAFBoAFBqgEBMbgBA8gBAPgBAeIDBBgAIEGIBgE&sclient=gws-wiz-serp"
driver.get(url)
time.sleep(1)
maltite = {}  # izveido tukšu dictionarie


# while True:
#     ediens = str(input("Ko ēdāt: "))
#     if ediens.lower() == "x":
#         break
#     svars = float(input("Cik g apēdāt: "))
#     maltite[ediens] = svars # saglabā ēdienus un gramus dictionarie


find = driver.find_element(By.ID, "L2AGLb") # piekrīt noteikumiem
find.click() 
find = driver.find_element(By.ID, "tw-sl") # atver izvēles lapu
find.click()

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "language_list_item"))) # sagaida kamēr visi parādās 
lang_list = driver.find_elements(By.CLASS_NAME, "language_list_item")
new_list=[]

for l in lang_list: 
    if l.text != '':
        new_list.append(l.text)
        if l.text =="Latvian": 
            latvian = l

latvian.click() # izvēlas Latviešu valodu

find_2 = driver.find_element(By.ID, "tw-tl") # atver izvēles lapu
find_2.click()

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "language_list_item"))) # sagaida kamēr visi parādās 
lang_list = driver.find_elements(By.CLASS_NAME, "language_list_item")

for l in lang_list: 
    if l.text != '':
        new_list.append(l.text)
        if l.text =="English": 
            english = l

find = driver.find_element(By.ID, "tw-source-text-ta") 
find.clear() # ievads text loga
find.send_keys("ābols") # ievads text loga

english.click() # izvēlas Angļu valodu







time.sleep(10)


