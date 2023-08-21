#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = sum(int(argv[x]) for count in range(1, len(argv)))
    print("{}".format(result))
