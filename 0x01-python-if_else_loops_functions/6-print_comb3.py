#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if(i == 8 and k == 9):
            print("{}".format(str(i) + str(k)))
        elif(k > i):
            print("{}".format(str(i) + str(k)) + ", ", end="")
