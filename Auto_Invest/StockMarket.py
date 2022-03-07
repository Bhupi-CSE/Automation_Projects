import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from requests import ConnectionError
import time
import urllib.request

def fetchStockMarketPrice(ticker):
    driver = webdriver.Chrome()
    driver.get("http://finance.yahoo.com/quote/" + stockTicker + "?p=" + stockTicker + "")
    driver.maximize_window()
    stock_info = driver.find_element(by=By.XPATH, value="//div[@id = 'quote-header-info']")
    stock_Price = stock_info.find_element(by=By.XPATH,
                                      value="//fin-streamer[@data-field='regularMarketPrice'][@data-symbol='AMZN']")
    stock_price_change = stock_info.find_element(by=By.XPATH,
                                             value="//fin-streamer[@data-field='regularMarketChangePercent']["
                                                   "@data-symbol='AMZN']")
# print("price for " + stockTicker + " is: " + stock_info.text)
    print("price for " + stockTicker + " is: " + stock_Price.text)
    print("percentage price change for " + stockTicker + "is:" + stock_price_change.text)

# calling main method
if __name__ == "__main__":
    stockTicker = "AMZN"
    fetchStockMarketPrice(stockTicker)




