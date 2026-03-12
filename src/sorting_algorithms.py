import random
import time

def bubble_sort(L):
    swaps = 0
    for i in range(len(L) - 1):
        swapped = False
        for j in range(len(L) - 1 - i): 
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swaps += 1
                swapped = True
        if swapped == False: 
            break
    return swaps

def insertion_sort(L):
    swaps = 0
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            swaps += 1
            j -= 1
        L[j + 1] = key
    return swaps

def selection_sort(L):
    n = len(L)
    swaps = 0
    for i in range(n - 1):
        max_j = 0
        for j in range(1, n - i):
            if L[j] > L[max_j]:
                max_j = j
        if (n - i - 1) != max_j:
            L[n - i - 1], L[max_j] = L[max_j], L[n - i - 1]
            swaps += 1
    return swaps
