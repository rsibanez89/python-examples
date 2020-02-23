import numpy as np
import matplotlib.pyplot as plt

# prints 2 dots (1,1) and (2,2)
def pint_2_dots():
    plt.scatter([1, 2], [1, 2])
    plt.show()


def print_list_of_dots():
    data = np.array([[1, 1.5], [2, 2], [3, 3], [4, 5],])
    x, y = data.T
    plt.scatter(x, y)
    plt.show()


def print_line():
    plt.plot([1, 2])
    plt.show()


def print_line_and_dots():
    plt.plot([4, 4, 5, 7], [1, 2, 3, 4], "y")
    plt.scatter([4, 4, 5], [1, 2, 3.5])
    plt.show()


if __name__ == "__main__":
    # pint_2_dots()
    # print_list_of_dots()
    # print_line()
    print_line_and_dots()
