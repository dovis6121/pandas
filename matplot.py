import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 3, 5, 7, 11]

plt.plot(x, y)
plt.ylim = (-1, 12)
plt.title("Simple Line Plot")
plt.xlim(0, 6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()