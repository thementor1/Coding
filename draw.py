from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://avivawholesale.com/")
html = browser.page_source
time.sleep(5)
print(html)

browser.close()

