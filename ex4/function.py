import numpy as np

def true_function(x):
    """
    x = 0のときy = 0となるテスト
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi * x * 0.8) * 10

if __name__ == "__main__":
    import doctest
    doctest.testmod()