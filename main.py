# This is a sample Python script.

import random

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

def find_item(find_x, arr):
    new_list = []
    for x, y in enumerate(arr):
        if y == find_x:
            new_list.append(x)
        else:
            new_list.append('-1')
    return new_list

def find_first_occurrence(find_x, arr):
    list = arr.copy()
    bubble_sort(list)
    for x in list:
        if x == find_x:
            print(f"First occurrence is at index: {list.index(x)}")
            break


def execute():
    # create the list
    find_x = input("Enter an integer number between 1 - 9 -> ")
    if find_x.isnumeric():
        find_x = int(find_x)
    l1= []
    for x in range(100):
        l1.append(random.randint(1,10))

    print(f"The Original List Is: {l1} ")

    bubble_sort(l1)
    print(f"Sorted List: {l1}")

    print("Items found:")
    print(find_item(find_x, l1))

    find_first_occurrence(find_x, l1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
