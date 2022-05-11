# This is a sample Python script.

import random
from prime_no import get_prime_list

def bubble_sort(arr):
    # sort the list

    swap_happened = True
    comparisons = 0
    while swap_happened:
        comparisons += 1
        swap_happened = False
        for num in range(len(arr)-1):
            comparisons += 1
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

"""
def find_item(find_x, arr):
    new_list = []
    for x, y in enumerate(arr):
        if y == find_x:
            new_list.append(x)
        else:
            new_list.append('-1')
    return new_list
"""

def search_first_occurrence(line2, x):
    for item, value in enumerate(line2):
        if int(value) == int(x):
            print(f"Element {int(x)} has first occurrence at index {item}", flush=True)
            break
        elif x not in line2:
            print("-1")
            break
    return

def search_using_binary_alg(ll, low, high, item):

    if low > high:
        return False
    else:
        mid = (low + high)//2
        if ll[mid] == item:
            return mid
        elif ll[mid] > item:
            return search_using_binary_alg(ll, low, mid-1, item)
        else:
            return search_using_binary_alg(ll, mid+1, high, item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l2 = []
    with open("input.txt", "r") as fp:
        x = fp.readline()[2:-1]
        l2 = fp.readline().split()
        # print(l2)
    fp.close()

    # search_first_occurrence(l2, x)

    result = search_using_binary_alg(l2, 0, len(l2)-1, x)
    if result != -1:
        print(f"Element {x} has the index {result}")
    else:
        print("Element is not in the list")

