import matplotlib.pyplot as plt

plt.figure()
plt.axis([0, 6, 0, 20])  # X axis 0-6 and Y axis 0-20 Note that if we comment this out matplotlib will automatically set axes for us.
plt.plot([1, 2, 3, 4], [3, 5, 9, 25])
plt.show()
