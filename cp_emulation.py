# cp_emulation.py
"""
Request
Write a python program that takes 2 args as input (look that up how to do). The args should be file paths.
The program should emulate the cp command (without support for any flags).
That means that the program should copy the contents of the first input file over to the second if possible.
It should print an error if any of the arguments is missing or inaccessible.
Command example
python custom_copy.py /tmp/demo.txt ~/demo.txt

Bear in mind the files can be large, or even binary. It should work with any file type. It should not exceed 512 MB of RAM
This task may seem daunting, but it's not.
The basic idea is to try to open the input file, read it in batches of a fixed buffer size,
and before reading the next batch, write it to the output file, while keeping both file descriptors open.
The last requirement is simply to discourage you from trying to fully load the input file in memory
Reading line by line may seem like a good idea, but non-text files  (photos, videos, programs, etc)
usually don't have that. Even text files offer no guarantees that the text isn't on one line.


"""
import sys
import os
import shutil



def read_from(source, buffer=512):

    def get_chunk(source, buffer=512):
        for i in range(0, len(source), buffer):
            yield source[i:i + buffer]

    for word in get_chunk(source):
        data = word
        #print(data, end='', flush=True)
    return data

def copy_file(source, target):
    with open(target, 'a') as file:
        print(len(source))
        file.write(source)


def start():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    except IndexError:
        raise SystemError(f"Script {sys.argv[0]} doesn't have enough arguments")

    with open("test.txt", 'r') as file:
        for content in file:
            file_content = read_from(content)
            copy_file(file_content, file2)

start()
