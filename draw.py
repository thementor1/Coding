from selenium import webdriver
from bs4 import BeautifulSoup
import time

instagramUrl = "https://www.youtube.com/watch?v=zrCLRC3Ci1c"


browser = webdriver.Firefox()

browser.get(instagramUrl)
html = browser.page_source
time.sleep(10)

soup = BeautifulSoup(html, 'html.parser')
messages = soup.find_all("style-scope ytd-comment-renderer")

for message in messages:
    print(message)

browser.close()

