# https://zoon.by/minsk/restaurants/
import time
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox

url = 'https://zoon.by/minsk/restaurants'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

catalogTitle = soup.find('h1', class_='new_filters_block__title js-page-title')

filtersBlockCount = soup.find('span', class_='new_filters_block__count js-place-count')

links = soup.findAll('a', class_='button button34 button-filter')
browser = Firefox()


# for link in links:
# browser.get(link['href'])
browser.get(url)
browser.execute_script("window.scrollTo(0, 200)")
y = 1000
for timer in range(0, 100):
     browser.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 500
     time.sleep(0.5)

li = browser.find_elements_by_class_name("minicard-item")
print(len(li))

browser.close()
quit()
