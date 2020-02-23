# Module with util functions


def multiply(num1, num2):
    return num1 * num2


# This file can be called by itself like `python util_functions.py 2 4`
if __name__ == "__main__":
    import sys

    print(multiply(int(sys.argv[1]), int(sys.argv[2])))
