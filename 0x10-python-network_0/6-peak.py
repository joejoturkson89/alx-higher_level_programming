#!/usr/bin/python3
# This script finds the peak of a unsorted integers.


def search(low, h, ints):
    mid = (low + h) // 2
    if low == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, h, ints))
    return(search(low, mid, ints))


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))
