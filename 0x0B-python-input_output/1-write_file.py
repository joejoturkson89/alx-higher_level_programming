#!/usr/bin/python3
"""Function that defines  file-writing."""


def write_file(filename="", text=""):
    """This writes a string to a UTF8 text file.
    Args:
        filename(str): name of file to write.
        text(str): text to write to the file.
    Return:
        Return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
