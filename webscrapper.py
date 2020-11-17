from selenium import webdriver
import urllib.request
import time
import os
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
#mobn=input('enter ur no')
chrome_path = r"C:\Users\Ananya\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)

driver.get('https://www.myntra.com/my/orders')

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div[2]/div[1]/input").send_keys(8318561801)
logn="/html/body/div[2]/div/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div[2]/div[2]"
driver.find_element_by_xpath(logn).click()
f=int(input("no1"))
driver.find_element_by_xpath("//*[@id='reactPageContent']/div/div[2]/div[1]/input[1]").send_keys(f)
g=int(input("no2"))
driver.find_element_by_xpath("//*[@id='reactPageContent']/div/div[2]/div[1]/input[2]").send_keys(g)
h=int(input("no3"))
driver.find_element_by_xpath("//*[@id='reactPageContent']/div/div[2]/div[1]/input[3]").send_keys(h)
i=int(input("no4"))
driver.find_element_by_xpath("//*[@id='reactPageContent']/div/div[2]/div[1]/input[4]").send_keys(i)

time.sleep(5)
print(driver.page_source.encode('utf-8'))
WebDriverWait(driver,3)
ps=driver.page_source
f=open('file.txt', 'a')
soup = BeautifulSoup(ps)
f.writelines('\n')
for tag in soup.find_all('span',class_="Text-Text"):
    print (tag.text)
    f.writelines(tag.text+'\n')

p="/html/body/div[2]/div/div/div[3]/div[2]"
driver.find_element_by_xpath(p).click()
time.sleep(5)
print(driver.page_source.encode('utf-8'))
WebDriverWait(driver,3)
ps=driver.page_source
s = BeautifulSoup(ps)
f.writelines('\n')
for tag in s.find_all('span',class_="Text-Text"):
    print (tag.text)
    f.writelines(tag.text+'\n')

x="/html/body/div[2]/div/div/div[3]/div[2]/span[2]"
driver.find_element_by_xpath(x).click()
time.sleep(5)
print(driver.page_source.encode('utf-8'))
WebDriverWait(driver,3)
ps=driver.page_source
v = BeautifulSoup(ps)
f.writelines('\n')
for tag in v.find_all('span',class_="Text-Text"):
    print (tag.text)
    f.writelines(tag.text+'\n')

for i in range(9):
    y = "/html/body/div[2]/div/div/div[3]/div[2]/span[3]"
    driver.find_element_by_xpath(y).click()
    time.sleep(5)
    print(driver.page_source.encode('utf-8'))
    WebDriverWait(driver, 3)
    ps = driver.page_source
    v = BeautifulSoup(ps)
    f.writelines('\n')
    for tag in v.find_all('span',class_="Text-Text"):
        print(tag.text)
        f.writelines(tag.text+'\n')
    time.sleep(2)
