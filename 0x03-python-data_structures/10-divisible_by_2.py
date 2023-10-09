#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            myList.append(True)
        else:
            myList.append(False)
    return myList

