import matplotlib.pyplot as plt
from typing import List


def pie_chart(xs: List[int], categories: List[str]):
    figure = plt.figure()
    p = figure.add_subplot(1, 1, 1)
    p.pie(
        xs,
        labels=categories,
        autopct="%1.1f%%")
    return figure
