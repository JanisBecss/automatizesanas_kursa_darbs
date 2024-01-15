import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import search_2
import translate
import pandas as pd
from datetime import datetime

edieni=[]
svars_g=[]
kalorijas = tauki = oglhidrati = proteini = 36
# kalorijas, tauki, oglhidrati, proteini = search.mekletajs("apple") # g uz 100g produkta 

# while True:
#     ediens_lv = str(input("Ko ēdāt: "))
#     if ediens_lv.lower() == "x":   
#         break
#     edieni.append(ediens_lv)
#     svars = float(input("Cik g apēdāt: "))
#     svars_g.append(svars) # ēdienu svari (g) saglabāti list

# edieni_eng = translate.tulkosana(edieni) # ēdienu angļu tulkojumi saglabāti list

# for i in range(len(edieni_eng)):
#     kalorijas, tauki, oglhidrati, proteini = search.mekletajs(edieni_eng[i]) # g uz 100g produkta 
#     kalorijas += kalorijas
#     tauki += tauki
#     oglhidrati += oglhidrati
#     proteini += proteini 


# print(kalorijas, tauki, oglhidrati, proteini)
data = {
    'Date': [datetime.now().strftime('%Y-%m-%d')],
    'Kalorijas': [kalorijas],
    'Tauki': [tauki],
    'Oglhidrati': [oglhidrati],
    'Proteini': [proteini]
}

# DataFrame
df = pd.DataFrame(data)

# File path
excel_file_path = 'results.xlsx'

# Check if the file exists
try:
    existing_data = pd.read_excel(excel_file_path, engine='openpyxl')
    # Append new data to existing DataFrame
    df = pd.concat([existing_data, df], ignore_index=True)
except FileNotFoundError:
    # File doesn't exist, create a new DataFrame
    df = pd.DataFrame(data)

# Save the DataFrame to Excel
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Data saved to {excel_file_path}")


