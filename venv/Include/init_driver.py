from selenium import webdriver
import requests
import sys
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from browsermobproxy import Server

server = Server("C:\\Users\\Administrator\Downloads\\browsermob-proxy-2.0-beta-6\\bin\\browsermob-proxy.bat")
server.start()
proxy=server.create_proxy()

def getServer():
    return server
def getProxy():
    return proxy

def init_driver(url):
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('--proxy-server={0}'.format(proxy.proxy))
    option.add_argument('--window-size=1366,768')
    #option.add_argument('--disable-gpu')
    chrome = webdriver.Chrome(chrome_options=option)
    chrome.get(url)
    print(chrome.page_source)
    proxy.new_har(url)
    
    for i in range(2,500):
        js="var q=document.documentElement.scrollTop={}".format(i*100)
        chrome.execute_script(js)
    return chrome