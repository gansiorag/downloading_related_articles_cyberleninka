'''
 This module collects 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2023/10/10
Ending 2023//
    
'''
from db_modules import WDB
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import sys
import os
from termcolor import cprint
import inspect
import wget

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


def zero_data():
    data = {"questions": "",
            "level_link": "",
            "href": "",
            "file": "",
            "name_art": "",
            "autor": "",
            "year": ""}
    return data


def step_one(fraza: str):
    # start page
    driver = webdriver.Chrome(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/config/chromedriver')
    driver.get('https://cyberleninka.ru')
    db = WDB(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/dataset/db_all_info.db')

    # get first page on ask
    in_ask = driver.find_element(By.XPATH, '//fieldset//input')
    in_ask.send_keys(f'{fraza}')
    butt = driver.find_element(By.XPATH, '//fieldset//button')
    butt.click()
    sleep(3)

    # get number pagination
    puginators = driver.find_elements(
        By.XPATH, '//ul[@class="paginator"]//li//a')
    print('puginators = ', len(puginators))
    href_pag_b = puginators[0].get_attribute("href")[:-2]
    print('href_pag_b == ', href_pag_b)
    npag = 1
    list_href = []
    while npag <= (len(puginators)+2):
        # get next partishion articls
        first_articles = driver.find_elements(
            By.XPATH, '//ul[@id="search-results"]//li//h2[@class="title"]')
        print(len(first_articles))
        for el in first_articles:
            dd = el.find_element(By.XPATH, './a')
            # print(f'page = {npag} href ==>> {dd.get_attribute("href")}')
            list_href.append(dd.get_attribute("href"))
        print()
        cprint(
            f'href_pag_b + str(npag) == {href_pag_b + str(npag)}', 'red', attrs=['bold'])
        driver.get(href_pag_b + str(npag))
        npag += 1
        sleep(3)
    set_href = set(list_href)
    for hh in set_href:
        data_str = zero_data()
        data_str["href"] = hh
        data_str["level_link"] = '1'
        data_str["questions"] = fraza
        db.add_str_all_info_articles(data_str)
    driver.close()


def get_all_info_articles(href: str):
    # start page
    driver = webdriver.Chrome(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/config/chromedriver')
    driver.get(href)
    name_art = driver.find_element(By.XPATH, '//i[@itemprop="headline"]')
    name_art = name_art.text
    print()
    print(name_art)
    spec_art = driver.find_element(By.XPATH, '//i[@itemprop="articleSection"]')
    spec_art = spec_art.text
    print()
    print(spec_art)
    
    name_mag = driver.find_element(By.XPATH, '//div[@class="half"]//span//a[1]')
    name_mag_text = name_mag.text
    print()
    print(name_mag_text)
    
    name_mag_href = name_mag.get_attribute('href')
    print()
    print(name_mag_href)
        
    year_art = driver.find_element(By.XPATH, '//div[@class="half"]//div[@class="labels"]//div[@class="label year"]')
    year_art = year_art.text
    print()
    print('year_art = ', year_art)

    vak_art = driver.find_element(By.XPATH, '//div[@class="half"]//div[@class="labels"]//div[@class="label vak"]')
    vak_art = vak_art.text
    print()
    print('vak_art = ', vak_art)
        
    area_sciens = driver.find_elements(By.XPATH, '//div[@class="half-right"]//ul//li//a')
    area_sciens_f = ''
    for area in area_sciens:
        area_sciens_f += (area.text + ',')
        area_sciens_f += (area.get_attribute('href') + ',')
    print()
    print(area_sciens_f)
    
    key_words = driver.find_elements(By.XPATH, '//div[@class="infoblock visible"]//i[@itemprop="keywords"]//span')
    key_words_f = ''
    for word in key_words:
        key_words_f += (word.text + ',')
    print()
    print(key_words_f)
    
    ann_art = driver.find_elements(By.XPATH, '//div[@class="full abstract"]//p[@itemprop="description"]')
    ann_art_rus = ann_art[0].text
    ann_art_eng = ann_art[1].text
    print()
    print('ann_art_rus = ', ann_art_rus)
    print()
    print('ann_art_eng = ', ann_art_eng)
    names_art = driver.find_elements(By.XPATH, '//div[@class="full abstract"]//h2')
    name_art_eng = names_art[1].text
    print()
    print('name_art_eng = ', name_art_eng)
    
    link_arts = driver.find_elements(By.XPATH, '//div[@class="full"]//ul//li')
    link_arts_f = ''
    for link in link_arts:
        link_arts_href = link.find_element(By.XPATH, './a[@class="similar"]').get_attribute('href')
        print()
        print(link_arts_href)
        link_arts_name = link.find_element(By.XPATH, './a[@class="similar"]//div[@class="title"]').text
        print()
        print('link_arts_name = ', link_arts_name)
        autors_link_arts = link.find_element(By.XPATH, './a[@class="similar"]//span').text.split('/')
        print()
        print('link_arts_year = ', autors_link_arts[0])
        print()
        print('link_arts_autors = ', autors_link_arts[1])
        
    autors = driver.find_elements(
        By.XPATH, '//div//ul[@class="author-list"]//li//span')
    file_load = driver.find_element(
        By.XPATH, '//div[@class="infoblock"]//a[@class="btn-new-square"]').get_attribute("href")
    file_name_db = wget.download(file_load,
                             out='/home/al/Projects_My/downloading_related_articles_cyberleninka/dataset/files_articles')
    autors_f = ''
    for autor in autors:
        autors_f += (autor.text + ',')
        print()
        print(autor.text)
    print()
    print('file_name_db == ', file_name_db)
    sleep(1000)
    driver.close()
    return name_art, spec_art, autors_f, file_name_db


def load_article():
    db = WDB(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/dataset/db_all_info.db')
    list_href = db.get_zero_load()
    print(len(list_href))
    print(list_href[3])
    for str_s in list_href:
        get_all_info_articles(str_s[2])


if __name__ == '__main__':
    #fraza = "зрение роботов"
    fraza = "архитектура сознания"
    step_one(fraza)
    #load_article()
