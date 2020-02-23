# > python -m pip install -U pip

# install numpy https://numpy.org/
# > python -m pip install -U numpy

# install matplotlib: https://matplotlib.org/users/installing.html
# > python -m pip install -U matplotlib

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()

