Write a function for checking the speed of drivers. This function should have one parameter: speed.

    1. If speed is less than 70, it should print “Ok”.
    2. Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
    For example, if the speed is 80, it should print: “Points: 2”.
    3. If the driver gets more than 12 points, the function should print: “License suspended”

Solution

import math


def speed_check(speed):
    demerit_point = 0
    if speed <= 70:
        print('Ok')
    elif speed >= 130:
        print('License suspended')
    else:
        exceeded_speed = speed - 70
        # if exceeded_speed % 5 == 0:
        #     points = exceeded_speed // 5
        #     demerit_point += points
        #     print(f'demerit points = {demerit_point}')
        # else:
        #     demerit_point = exceeded_speed / 5
        #     print(f'demerit points = {demerit_point}')
        demerit_point = exceeded_speed / 5
        print(f'demerit points = {math.floor(demerit_point)}')
    return demerit_point


speed_check(99)
