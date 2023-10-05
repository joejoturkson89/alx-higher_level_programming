#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if(args <= 1):
        print("{} arguments.".format(args - 1))
    elif(args == 2):
        print("{} :".format(args - 1))
