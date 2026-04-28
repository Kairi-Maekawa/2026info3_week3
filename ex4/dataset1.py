import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def true_function(x):
    """
    x = 0のときy = 0となるテスト
    >>> true_function(0)
    0.0
    """
    return np.sin(np.pi * x * 0.8) * 10

x = np.linspace(-1, 1, 100)
y = true_function(x)

np.random.seed(0)
xdot = np.random.uniform(-1, 1, 20)
ydot = true_function(xdot)

df = pd.DataFrame({
    "観測点": xdot,
    "真値": ydot
})

noise = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=20)
noise = noise / 2
df["観測値"] = df["真値"] + noise
print(df)

plt.plot(x, y, label="y = sin(pi * x * 0.8) * 10")
plt.scatter(df["観測点"], df["真値"], color="red", label="observations")
plt.scatter(df["観測点"], df["観測値"], color="blue", label="observations_noise")

plt.legend() #凡例
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("ex1.3.png") #ex1.1.pngとして保存
plt.show()

df.to_csv("data.tsv", sep="\t", index=False)

if __name__ == "__main__":
    import doctest
    doctest.testmod()