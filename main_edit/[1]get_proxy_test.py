from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook
from selenium import webdriver
import time

URL = "https://free-proxy-all_items_list.net"

def get_proxys():

    all_items_list = []
    all_proxy_dict = {}

    driver = webdriver.Edge()

    driver.get(URL)
    time.sleep(10)
    contents = BeautifulSoup(driver.page_source, "html.parser")

    all_items = contents.find_all("td")

    for i in all_items:
        all_items_list.append(i.text)


    print(len(all_items_list))
    print(all_items_list)







get_proxys()



