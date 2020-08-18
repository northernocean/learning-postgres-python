import matplotlib.pyplot as plt

figure = plt.figure()

subplot = figure.add_subplot()
subplot.set_title("Line Graph")
subplot.set_xlabel("Xs")
subplot.set_ylabel("Ys")
subplot.plot([1, 2, 3, 4], [3, 5, 9, 25])

plt.show() # In some context figure.show() will also work here, such in some notebooks.
