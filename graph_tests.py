import matplotlib.pyplot as plt

figure = plt.figure()
p1 = figure.add_subplot(1, 2, 1)  # or add_subplot(121) works
p2 = figure.add_subplot(1, 2, 2)
p1.plot([1, 2, 3, 4], [3, 5, 9, 25])
p2.plot([1, 2, 3, 4], [4, 7, 11, 17])
plt.show()


# other ways to create subplots:

figure, (p1, p2) = plt.subplots(1, 2)  # a figure with two plots side by side
p1.plot([1, 2, 3, 4], [3, 5, 9, 25])
p2.plot([1, 2, 3, 4], [4, 7, 11, 17])
plt.show()

figure, ((p1, p2), (p3, p4)) = plt.subplots(2, 2)  # a figure with four plots 2 x 2
p1.plot([1, 2, 3, 4], [3, 5, 9, 25])
p2.plot([1, 2, 3, 4], [4, 7, 11, 17])
p3.plot([1, 2, 3, 4], [4, 7, 11, 17])
p4.plot([1, 2, 3, 4], [4, 7, 11, 17])
plt.show()
