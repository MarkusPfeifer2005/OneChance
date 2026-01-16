#!/bin/python3
import os
import json
import sys


def main():
    if len(sys.argv) > 2:
        print("Too many arguments provided; aborting.\n" \
        "Only enter the filename of the file you want to indent.")
        exit(-1)
    elif len(sys.argv) == 1:
        print("No filename was provided!\n"
        "Specify the file you want to indent.")
        exit(-1)
    path = sys.argv[1]
    if not os.path.isfile(path):
        print("File not found!")
        exit(-1)
    with open(path, "r") as json_file:
        content = json.loads(json_file.read())
    with open(path, "w") as json_file:
        json_file.write(json.dumps(content, indent=4))


if __name__ == "__main__":
    main()
