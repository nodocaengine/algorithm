#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print findSmallest([2, 4, 1, 7, 3])
