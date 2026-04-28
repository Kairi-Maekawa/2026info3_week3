import numpy as np
import matplotlib.pyplot as plt


def true_function(x):
    """
    x = 0のときy = 0となるテスト
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi * x * 0.8) * 10

x = np.linspace(-1, 1, 100)
y = true_function(x)

plt.plot(x, y, label="y = sin(pi * x * 0.8) * 10")
plt.legend() #凡例
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("ex1.1.png") #ex1.1.pngとして保存
plt.show()
if __name__ == "__main__":
    import doctest
    doctest.testmod()