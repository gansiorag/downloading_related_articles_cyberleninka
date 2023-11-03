'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

if __name__ == '__main__':
    TIME_1 = '07:04:00'
    TIME_2 = '08:14:00'
    time_1_list = [int(k) for k in TIME_1.split(':')]
    time_2_list = [int(k) for k in TIME_2.split(':')]
    dd1 = time_1_list[0] * 3600 + time_1_list[1] * 60 + time_1_list[2]
    dd2 = time_2_list[0] * 3600 + time_2_list[1] * 60 + time_2_list[2]
    dr = dd1 - dd2
    print(dr)
