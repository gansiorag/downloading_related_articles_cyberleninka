'''
 This module collects 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2023/10/10
Ending 2023//
    
'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import sys
import os
from termcolor import cprint
import inspect

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
sys.path.append(file_dir.split(nameProjectStart)[0] + nameProjectStart)
base_path = file_dir.split(nameProjectStart)[0] + nameProjectStart + '/'

from db_modules import WDB

def zero_data():
    data={"questions":"", 
          "level_link":"", 
          "href":"", 
          "file":"", 
          "name_art":"", 
          "autor":"", 
          "year":""}
    return data    

def step_one(fraza:str):    
    # start page
    driver = webdriver.Chrome('/home/al/Projects_My/downloading_related_articles_cyberleninka/config/chromedriver')
    driver.get('https://cyberleninka.ru')
    db = WDB('/home/al/Projects_My/downloading_related_articles_cyberleninka/dataset/db_all_info.db')

    # get first page on ask
    in_ask = driver.find_element(By.XPATH, '//fieldset//input')
    in_ask.send_keys(f'{fraza}')
    butt = driver.find_element(By.XPATH, '//fieldset//button')
    butt.click()
    sleep(3)

    # get number pagination
    puginators = driver.find_elements(By.XPATH, '//ul[@class="paginator"]//li//a')
    print('puginators = ', len(puginators))
    href_pag_b = puginators[0].get_attribute("href")[:-2]
    print('href_pag_b == ', href_pag_b)
    npag = 1
    while npag <=(len(puginators)+2):
        
        # get next partishion articls
        first_articles = driver.find_elements(By.XPATH, '//ul[@id="search-results"]//li//h2[@class="title"]')
        print(len(first_articles))
        for el in first_articles:
            dd = el.find_element(By.XPATH, './a')
            print(f'page = {npag} href ==>> {dd.get_attribute("href")}')
            data_str = zero_data()
            data_str["href"] = dd.get_attribute("href")
            data_str["level_link"] = '1'
            data_str["questions"] = fraza
            db.add_str_all_info_articles(data_str)
        # href_pag = puginators[npag].get_attribute("href")
        print()
        cprint(f'href_pag_b + str(npag) == {href_pag_b + str(npag)}', 'red', attrs=['bold'])
        driver.get(href_pag_b + str(npag))
        npag += 1
        sleep(3)
    driver.close()

if __name__ == '__main__':
    fraza = "зрение роботов"
    step_one(fraza)
