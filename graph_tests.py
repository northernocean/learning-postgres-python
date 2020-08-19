import matplotlib.pyplot as plt

results = [63, 28, 8]
result_labels = ["flask", "django", "not sure"]

figure = plt.figure()
p = figure.add_subplot()
p.pie(
    results,
    labels=result_labels,
    explode=[0.1, 0, 0],
    autopct="%1.1f%%"
    )
plt.show()
