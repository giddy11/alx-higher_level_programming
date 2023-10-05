#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1

plural_suffix = "s" if num_of_args != 1 else ":"
print("{} argument{}".format(num_of_args, plural_suffix))

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
