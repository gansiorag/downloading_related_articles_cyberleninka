'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
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
    
import os
import sys
import sqlite3
import json

nameProjectStart = 'downloading_related_articles_cyberleninka'
file_dir = os.path.dirname(__file__)
print(file_dir)
sys.path.append(file_dir.split(nameProjectStart)[0] + nameProjectStart)


class WDB():
    def __init__(self,NameFile:str):
        self.conn = sqlite3.connect(NameFile, check_same_thread=False)
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
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    name=''
    prog1()
    prog2()