from selenium import webdriver
from time import sleep
import openpyxl


workbook = openpyxl.Workbook()
worksheet = workbook.active

driver = webdriver.Chrome("/Applications")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://tr.tradingview.com/chart/?symbol=BITSTAMP%3ABTCUSD")
driver.implicitly_wait(10)
while True:
    BTC_fiyat = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
    worksheet.append([BTC_fiyat.text ])
    workbook.save('BTC.xlsx')
    sleep(10)