"""
This module collects
"""
# Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
# Starting 2023/10/10
# Ending 2023//

from time import sleep
import sys
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from termcolor import cprint
# import inspect
import wget
from db_modules import WDB

# Summary:
# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue
# on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> c# print(f'{}' , 'red', attrs=['bold'])
# Shows which module is currently running
# c# print('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name
# + ' << '+'='*20, 'red', attrs=['bold'])

NAME_PROJECT_STARTS = 'downloading_related_articles_cyberleninka'

file_dir = os.path.dirname(__file__)
# print(file_dir)
sys.path.append(file_dir.split(NAME_PROJECT_STARTS)[0] + NAME_PROJECT_STARTS)
base_path = file_dir.split(NAME_PROJECT_STARTS)[0] + NAME_PROJECT_STARTS + '/'


def zero_data():
    """_summary_

    Returns:
        _type_: _description_
    """
    data = {"questions": "",
            "level_link": "",
            "href": "",
            "file": "",
            "name_art": "",
            "autor": "",
            "year": "",
            "spec": "",
            "name_mag": "",
            "mag_href": "",
            "vak": "",
            "area_sciens": "",
            "key_words": "",
            "ann_art_rus": "",
            "ann_art_eng": "",
            "name_art_eng": "",
            "link_arts_href": "",
            }
    return data


def step_one(fraza: str):
    """_summary_

    Args:
        fraza (str): _description_
    """
    # start page
    driver = webdriver.Chrome(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/'
        'config/chromedriver')
    driver.get('https://cyberleninka.ru')
    db = WDB(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/'
        'dataset/db_all_info.db')

    # get first page on ask
    in_ask = driver.find_element(By.XPATH, '//fieldset//input')
    in_ask.send_keys(f'{fraza}')
    butt = driver.find_element(By.XPATH, '//fieldset//button')
    butt.click()
    sleep(3)
    butt2 = driver.find_elements(By.XPATH, '//ul[@class="tag-list"]//li//button')
    butt2[0].click()
    sleep(3)
    # get number pagination
    puginators = driver.find_elements(
        By.XPATH, '//ul[@class="paginator"]//li//a')
    print('puginators = ', len(puginators))
    href_pag_b = puginators[0].get_attribute("href")[:-2]
    # [:-2]
    # print('href_pag_b == ', href_pag_b)
    npag = 1
    list_href = []
    while npag <= (len(puginators)+2):
        # get next partishion articls
        first_articles = driver.find_elements(
            By.XPATH, '//ul[@id="search-results"]//li//h2[@class="title"]')
        # print(len(first_articles))
        for el in first_articles:
            dd = el.find_element(By.XPATH, './a')
            # # print(f'page = {npag} href ==>> {dd.get_attribute("href")}')
            list_href.append(dd.get_attribute("href"))
        # print()
        cprint(
           f'href_pag_b + str(npag) == {href_pag_b + str(npag)}',
           'red', attrs=['bold'])
        driver.get(href_pag_b + str(npag) + '#')
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


def get_all_info_articles(href: str, path_load, questions, level: str):
    """_summary_

    Args:
        href (str): _description_
        path_load (_type_): _description_

    Returns:
        _type_: _description_
    """
    # start page
    db = WDB('/home/al/Projects_My/downloading_related_articles_cyberleninka/dataset/db_all_info.db')
    driver = webdriver.Chrome(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/'
        'config/chromedriver')
    driver.get(href)
    sleep(5)
    data_dict = zero_data()
    name_art = driver.find_element(By.XPATH, '//i[@itemprop="headline"]')
    name_art = name_art.text
    data_dict['name_art'] = name_art
    # print()
    # cprint(name_art, 'green', attrs=['bold'])
    spec_art = driver.find_element(By.XPATH, '//i[@itemprop="articleSection"]')
    spec_art = spec_art.text
    # print()
    # print(spec_art)
    data_dict['href'] = href
    data_dict['spec'] = spec_art

    name_mag = driver.find_element(
        By.XPATH, '//div[@class="half"]//span//a[1]')
    name_mag_text = name_mag.text
    # print()
    # print(name_mag_text)
    data_dict['name_mag'] = name_mag_text
    name_mag_href = name_mag.get_attribute('href')
    # print()
    # print(name_mag_href)
    data_dict['mag_href'] = name_mag_href

    year_art = driver.find_element(
        By.XPATH, '//div[@class="half"]//div[@class="labels"]//'
        'div[@class="label year"]')
    year_art = year_art.text
    # print()
    # print('year_art = ', year_art)
    data_dict['year'] = year_art
    try:
        vak_art = driver.find_element(
            By.XPATH, '//div[@class="half"]//div[@class="labels"]//'
            'div[@class="label vak"]')
        vak_art = vak_art.text
    except Exception:
        vak_art = ''
    # print()
    # print('vak_art = ', vak_art)
    data_dict['vak'] = vak_art

    area_sciens = driver.find_elements(
        By.XPATH, '//div[@class="half-right"]//ul//li//a')
    area_sciens_f = ''
    for area in area_sciens:
        area_sciens_f += (area.text + ',')
        area_sciens_f += (area.get_attribute('href') + ',^')
    # print()
    # print(area_sciens_f)
    data_dict['area_sciens'] = area_sciens_f
    key_words = driver.find_elements(
        By.XPATH, '//div[@class="infoblock visible"]//'
        'i[@itemprop="keywords"]//span')
    key_words_f = ''
    for word in key_words:
        key_words_f += (word.text + ',')
    # print()
    # print(key_words_f)
    data_dict['key_words'] = key_words_f.replace("'", '"')
    ann_art = driver.find_elements(
        By.XPATH, '//div[@class="full abstract"]//p[@itemprop="description"]')
    try:
        ann_art_rus = ann_art[0].text
    except Exception:
        ann_art_rus = ''
    try:
        ann_art_eng = ann_art[1].text
    except Exception:
        ann_art_eng = ''
    # print()
    # print('ann_art_rus = ', ann_art_rus)
    data_dict['ann_art_rus'] = ann_art_rus.replace("'", '"')
    # print()
    # print('ann_art_eng = ', ann_art_eng)
    data_dict['ann_art_eng'] = ann_art_eng.replace("'", '"')
    names_art = driver.find_elements(
        By.XPATH, '//div[@class="full abstract"]//h2')
    try:
        name_art_eng = names_art[1].text
    except Exception:
        name_art_eng = ''
    # print()
    # print('name_art_eng = ', name_art_eng)
    data_dict['name_art_eng'] = name_art_eng.replace("'", '"')
    array_link_arts = ''
    link_arts = driver.find_elements(By.XPATH, '//div[@class="full"]//ul//li')
    for link in link_arts:
        new_art = zero_data()
        new_art["questions"] = questions
        new_art["level_link"] = level
        link_arts_href = link.find_element(
            By.XPATH, './a[@class="similar"]').get_attribute('href')
        array_link_arts += (link_arts_href + ',')
        new_art["href"] = link_arts_href
        # print()
        # print(link_arts_href)
        link_arts_name = link.find_element(
            By.XPATH, './a[@class="similar"]//div[@class="title"]').text
        # print()
        # print('link_arts_name = ', link_arts_name)
        new_art["name_art"] = link_arts_name.replace("'", '"')
        autors_link_arts = link.find_element(
            By.XPATH, './a[@class="similar"]//span').text.split('/')
        # print()
        # print('link_arts_year = ', autors_link_arts[0])
        new_art["year"] = autors_link_arts[0]
        # print()
        # print('link_arts_autors = ', autors_link_arts[1])
        new_art["autor"] = autors_link_arts[1]
        db.add_str_all_info_articles(new_art)
    autors = driver.find_elements(
        By.XPATH, '//div//ul[@class="author-list"]//li//span')

    autors_f = ''
    for autor in autors:
        autors_f += (autor.text + ',')
        # print()
        # cprint(autor.text, 'red', attrs=['bold'])
    # print()
    data_dict["autor"] = autors_f
    file_name_db = ''
    file_load = driver.find_element(
        By.XPATH, '//div[@class="infoblock"]//'
        'a[@class="btn-new-square"]').get_attribute("href")
    file_name_db = wget.download(file_load, out=path_load)
    # print('file_name_db == ', file_name_db)
    data_dict["file"] = file_name_db
    db.update_article(data_dict)
    # sleep(1000)
    driver.close()
    return name_art, spec_art, autors_f, file_name_db


def load_article(fraza: str):
    """_summary_
    """
    db = WDB(
        '/home/al/Projects_My/downloading_related_articles_cyberleninka/'
        'dataset/db_all_info.db')
    list_href = db.get_zero_load(fraza)
    # print(len(list_href))
    # print(list_href[3])
    for str_s in list_href:
        path_load = '/home/al/Projects_My/'\
            'downloading_related_articles_cyberleninka/'\
            f'dataset/files_articles/{str_s[0]}'
        os.makedirs(path_load, exist_ok=True)
        get_all_info_articles(str_s[2], path_load, str_s[0], str(int(str_s[1]) + 1))


if __name__ == '__main__':
    # fraza = "зрение роботов"
    # fraza = "архитектура сознания"
    FRAZA = "комбинаторные методы в лингвистике"
    # FRAZA = "современная теория сознания"

    # FRAZA = "методы современной когнитологии"
    # FRAZA = "современная теория общих систем"
    # load all href on all atricles for fraza
    # step_one(FRAZA)

    # load files articles and add links addons
    load_article(FRAZA)
