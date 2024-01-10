#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    total = 0
    total_weight = 0
    for num, weight in my_list:
        total = total + (num * weight)
        total_weight = total_weight + weight
    if total_weight == 0:
        return 0
    avg = total / total_weight
    return avg
