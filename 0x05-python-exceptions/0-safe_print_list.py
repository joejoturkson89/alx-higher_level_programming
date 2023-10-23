#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    if(my_list):
        for n in range(x):
            try:
                print("{}".format(my_list[n]), end='')
                total = total + 1
            except IndexError:
                print()
                return(total)
    print()
    return(total)
