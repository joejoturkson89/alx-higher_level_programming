#!/usr/bin/python3
"""Function that defines text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """This inserts a text file after each line containing
    a given string in a file.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
