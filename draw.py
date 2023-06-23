from selenium import webdriver
from bs4 import BeautifulSoup
import time

ytLiveChatUrl = "https://www.youtube.com/live_chat?v=mxTiT2igK7A"


browser = webdriver.Firefox()

browser.get(ytLiveChatUrl)
html = browser.page_source
time.sleep(10)

soup = BeautifulSoup(html, 'html.parser')
messages = soup.find_all("style-scope ytd-comment-renderer")

for message in messages:
    print(message)


for message in messages:
    print(message)

browser.close()

