import matplotlib.pyplot as plt

plt.figure()

plt.xlabel("Xs")
plt.ylabel("Ys")
plt.title("X vs Y")
xs = [1, 2, 3, 4]
ys = [3, 5, 9, 25]
plt.plot(xs, ys, "o")
plt.show()
