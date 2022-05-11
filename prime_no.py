# prime_no.py
"""given an integer N, 2 < N < 2 000 000, print (or write to a file) all the prime numbers smaller than it"""

def get_prime_list(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):

            # If num is divisible by any number between 2 and n / 2, it is not prime
            if (num % i) == 0:
                # print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    return

# iterate the list and print the prime numbers
num = int(input("Give a number between 0-2000000: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    for x in reversed(range(2, num+1)):
        get_prime_list(x)