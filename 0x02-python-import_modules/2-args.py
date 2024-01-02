#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc-1 == 1:
        print("{:d} argument".format(argc - 1), end="")
    else:
        print("{:d} arguments".format(argc - 1), end="")
    print(".") if argc - 1 == 0 else print(":")
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, sys.argv[i]))
