#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(list_length):
        div = 0
        try:
            div = my_list_1[n] / my_list_2[n]
        except IndexError:
            print("{}".format("out of range"))
            div = 0
        except (ValueError, TypeError):
            print("{}".format("wrong type"))
            div = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            div = 0
        finally:
            new_list.append(div)
    return(new_list)
