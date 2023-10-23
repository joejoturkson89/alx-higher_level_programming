#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    if(my_list):
        for n in range(x):
            try:
                print("{:d}".format(my_list[n]), end='')
                total = total + 1
            except(ValueError, TypeError):
                pass
    print()
    return(total)
