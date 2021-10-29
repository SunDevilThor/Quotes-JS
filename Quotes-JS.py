# Scrape Javascript 
# Tutorial from John Watson Rooney YouTube channel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True

driver = webdriver.Chrome('/Users/thor/Downloads/chromedriver', options=options)

url = 'http://quotes.toscrape.com'
driver.get(url)

html = driver.page_source

# with open('Quotes-OFFLINE.html', 'w') as file: 
#    file.write(str(html))
#    print('Offline file saved.')

soup = BeautifulSoup(driver.page_source, 'html.parser')

quotes = soup.find_all('div', class_= 'quote')

for item in quotes: 
    print(item.find('span', class_='text').text)