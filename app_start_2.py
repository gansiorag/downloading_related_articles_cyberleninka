'''
 This module collects images from different sources on request
 Sources:
 1. https://yandex.ru/images/ - realized
 2. https://swisscows.com/ru/images?query=фото+пчелы&size=Large
 2. https://www.google.com/search
 3. https://images.search.yahoo.com/search/images
 4. https://duckduckgo.com/
 5. https://www.startpage.com/sp/search
 6. https://www.bing.com/images/
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2023/06/20
Ending 2023//
    
'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import sys
import os


'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
    
    
Shows which module is currently running
cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
'''


nameProjectStart = 'downloading_related_articles_cyberleninka'
file_dir = os.path.dirname(__file__)
print(file_dir)
sys.path.append(file_dir.split(nameProjectStart)
                [0] + nameProjectStart)
base_path = file_dir.split(nameProjectStart)[0] + nameProjectStart + '/'

driver = webdriver.Chrome('/home/al/Projects_My/downloading_related_articles_cyberleninka/config/chromedriver')
driver.get('https://cyberleninka.ru')
in_ask = driver.find_element(By.XPATH, '//fieldset//input')
fraza = "зрение роботов"
in_ask.send_keys(f'{fraza}')
butt = driver.find_element(By.XPATH, '//fieldset//button')
butt.click()
first_articles = driver.find_elements(By.XPATH, '//ul[@id="search-results"]//li//h2[@class="title"]')
print(len(first_articles))
for el in first_articles:
    dd = el.find_element(By.XPATH, './a')
    print(dd.get_attribute("href"))

sleep(600)
driver.close()