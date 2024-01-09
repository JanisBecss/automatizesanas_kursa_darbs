import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import search
import translate


edieni=[]
svars_g=[]


kalorijas, tauki, oglhidrati, proteini = search.mekletajs("apple") # g uz 100g produkta 


while True:
    ediens_lv = str(input("Ko ēdāt: "))
    if ediens_lv.lower() == "x":   
        break
    edieni.append(ediens_lv)
    svars = float(input("Cik g apēdāt: "))
    svars_g.append(svars) # ēdienu svari (g) saglabāti List

edieni_eng = translate.tulkosana(edieni) # ēdinu angļu tulkojumi saglabāti list





