from selenium import webdriver
from time import sleep



driver = webdriver.Chrome("/Applications")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://tr.tradingview.com/chart/?symbol=BITSTAMP%3ABTCUSD")
driver.implicitly_wait(10)
while True:
    fiyat_Bilgisi = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]").text
    print(fiyat_Bilgisi)
    sleep(10)