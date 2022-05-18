# weekend1.py
############## Request 1 ##################
# Print the Nth number in the Fibonacci sequence (google for rule). 0 <= N <=1 000 000
import timeit

""" 1. Fn = Fn-1 + Fn-2, where n > 1."""

def fib_seq(n):
    seq_list = [0, 1]
    # get result
    def get_nth(key):
        return seq_list[key]

    # go through the sequence and calculate its values
    def set_fib_seq(n):
        if n <= 2:
            print(f"Number must be >= 2")
        else:
            for i in range(2, n + 1):
                s = seq_list[i - 1] + seq_list[i - 2]
                seq_list.append(s)
        # call get_nth
        return get_nth(n)
    # call set_fib_seq
    return set_fib_seq(n)

############## Request 2 ##################
# Find all the divisors of a number

def divisors(n):
    divisors_list = []
    # possible divisors
    for i in range(1, n//2 + 1):
        # if rest is 0, add the number as divisor
        if n%i == 0:
            divisors_list.append(i)
    divisors_list.append(n)
    return divisors_list

############## Request 3 ##################
# Given a file with 2 sorted lists of integers (each list on its row),
# print a single list with all of the elements from the input lists,
# such that the single list is also sorted.
# Hint: you should not use any sort function here,
# but rely on the property of the inputs.

def file_content(list_size):
    def get_file_content():
        data = []
        # create a list with all elements from line1 and line 2
        with open("sorted_lists.txt", "r") as f_content:
            for line in f_content:
                for char in line.split():
                    char = char.strip(',][')
                    if char.isdigit():
                        data.append(char)

        data.sort(key=int)
        print(data)


    def create_list():
        # I want both lists with the same number of elements
        nonlocal list_size
        if list_size%2 == 1:
            list_size += 1

        with open("sorted_lists.txt", "w+") as sl:
            odd_list = []
            even_list = []
            for num in range(1, list_size+1):
                if num % 2 == 1:
                    odd_list.append(num)
                else:
                    even_list.append(num)
            sl.writelines(str(odd_list)+"\n")
            sl.writelines(str(even_list))
        get_file_content()
    return create_list()

############## Request 4 ##################

"""
Write a python program that takes 2 args as input (look that up how to do). 
The args should be file paths. 
The program should emulate the cp command (without support for any flags). 
That means that the program should copy the contents of the first input file over to the second if possible. 
It should print an error if any of the arguments is missing or inaccessible.
Command example
python custom_copy.py /tmp/demo.txt ~/demo.txt
"""


######### Start the program ######
def start():

    # Request 1
    fib_nr = int(input("Fibonacci number: "))
    print("Nth number in the Fibonacci sequence is",fib_seq(fib_nr))

    # Request 2
    divisor_nr = int(input("Get the divisors of .. "))
    print(f"{divisor_nr} has as divisors : {divisors(divisor_nr)}")

    # Request 3
    genric_list = int(input("How big is the list: "))
    file_content(genric_list)

    # Request 4

start()