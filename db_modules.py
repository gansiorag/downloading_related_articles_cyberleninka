'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''

import json
import sqlite3
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


class WDB():
    """_summary_
    """
    
    def __init__(self, name_file: str):
        """AI is creating summary for __init__

        Args:
            NameFile (str): [description]
        """
              
        self.conn = sqlite3.connect(name_file, check_same_thread=False)
        self.cur = self.conn.cursor()

    def add_str_all_info_articles(self, data: dict):
        sqlText = 'INSERT INTO all_info_articles (questions, level_link, href, file, name_art, autor, year) '\
            f"""VALUES('{data["questions"]}', '{data["level_link"]}', '{data["href"]}', '{data["file"]}', """\
            f"""'{data["name_art"]}', '{data["autor"]}', '{data["year"]}');"""
        self.cur.execute(sqlText)
        self.conn.commit()

    def get_zero_load(self):
        sqlText = 'SELECT questions, level_link, href, file, name_art, autor, "year" '\
            'FROM all_info_articles WHERE file = "";'
        self.cur.execute(sqlText)
        data = self.cur.fetchall()
        return data
    
    def update_article(self, d_d: dict):
        """AI is creating summary for update_article

        Args:
            dict_data (dict): [description]
        """

        sqlText = 'UPDATE all_info_articles '\
            f"""SET file={d_d["file"]}, name_art=d-D["name_art"],"""\
            f"""autor={d_d["autor"]},"""\
            f"""year={d_d["autor"]}, spec={d_d["autor"]},"""\
            f"""name_mag={d_d["autor"]}, mag_href={d_d["autor"]},"""\
            f"""vak={d_d["autor"]},"""\
            f"""area_sciens='', key_words='', ann_art_rus='', ann_art_eng='',"""\
            f"""name_art_eng='', link_arts_href=''"""\
                f"""WHERE href='{dict_data["href"]}'"""



def prog2():
    pass


if __name__ == '__main__':
    name = ''
    prog1()
    prog2()
