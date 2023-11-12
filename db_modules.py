'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

import sqlite3
import sys
import os


# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed
# template --> cprint(f'{}' , 'red', attrs=['bold'])

# Shows which module is currently running
# cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])


NAME_PROJECT_START = 'downloading_related_articles_cyberleninka'
file_dir = os.path.dirname(__file__)
print(file_dir)
sys.path.append(file_dir.split(NAME_PROJECT_START)[0] + NAME_PROJECT_START)


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
        """AI is creating summary for add_str_all_info_articles

        Args:
            data (dict): [description]
        """

        sql_text = 'INSERT INTO all_info_articles (questions, level_link, href, file, name_art, autor, year) '\
            f"""VALUES('{data["questions"]}', '{data["level_link"]}', '{data["href"]}', '{data["file"]}', """\
            f"""'{data["name_art"]}', '{data["autor"]}', '{data["year"]}');"""
        self.cur.execute(sql_text)
        self.conn.commit()

    def get_zero_load(self, fraza):
        """AI is creating summary for get_zero_load

        Returns:
            [type]: [description]
        """

        sql_text = 'SELECT questions, level_link, href, file, name_art, autor, "year" '\
            f'FROM all_info_articles WHERE file = "" and questions="{fraza}";'
        self.cur.execute(sql_text)
        data = self.cur.fetchall()
        return data

    def update_article(self, d_d: dict):
        """AI is creating summary for update_article

        Args:
            dict_data (dict): [description]
        """

        sql_text = 'UPDATE all_info_articles '\
            f"""SET file='{d_d["file"]}',"""\
            f"""name_art='{d_d["name_art"]}',"""\
            f"""autor='{d_d["autor"]}',"""\
            f"""year='{d_d["year"]}',"""\
            f"""spec='{d_d["spec"]}',"""\
            f"""name_mag='{d_d["name_mag"]}',"""\
            f"""mag_href='{d_d["mag_href"]}',"""\
            f"""vak='{d_d["vak"]}',"""\
            f"""area_sciens='{d_d["area_sciens"]}',"""\
            f"""key_words='{d_d["key_words"]}',"""\
            f"""ann_art_rus='{d_d["ann_art_rus"]}',"""\
            f"""ann_art_eng='{d_d["ann_art_eng"]}',"""\
            f"""name_art_eng='{d_d["name_art_eng"]}' """\
            f"""WHERE href='{d_d["href"]}';"""
        # print(sql_text)
        self.cur.execute(sql_text)
        self.conn.commit()


def prog2():
    pass


if __name__ == '__main__':
    name = ''
    prog2()
