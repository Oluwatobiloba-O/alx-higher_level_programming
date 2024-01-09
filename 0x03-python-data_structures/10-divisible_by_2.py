#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for x in range(0, len(my_list)):
        if my_list[x] % 2 == 0:
            list2 = list2 + [True]
        else:
            list2 = list2 + [False]
    return list2
