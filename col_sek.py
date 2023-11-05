'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''


def get_none():
    """AI is creating summary for get_none

    Returns:
        [type]: [description]
    """
    ff = None
    return ff


if __name__ == '__main__':

    TIME_1 = '15:42:52'
    TIME_2 = '19:59:39'
    time_1_list = [int(k) for k in TIME_1.split(':')]
    time_2_list = [int(k) for k in TIME_2.split(':')]
    dd1 = time_1_list[0] * 3600 + time_1_list[1] * 60 + time_1_list[2]
    dd2 = time_2_list[0] * 3600 + time_2_list[1] * 60 + time_2_list[2]
    dr = dd1 - dd2
    print(dr)
    DD_D = get_none()
    if DD_D:
        print(len(DD_D))
    else:
        print('None')
