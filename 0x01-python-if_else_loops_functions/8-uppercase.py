#!/usr/bin/python3
def uppercase(input_str):
    formatted_str = ""
    for char in input_str:
        formatted_str += "{}".format(chr(ord(char) - 32)
                                     if 'a' <= char <= 'z' else char)
    print("{}\n".format(formatted_str))
