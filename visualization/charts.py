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


def bar_chart(ys: List[int], categories: List[str]):
    #figure = plt.figure(figsize=(4, 5))  # ten 100-pixel "inches" by twelve 100-pixel "inches"
    #figure.subplots_adjust(bottom=0.1)
    figure = plt.figure()
    p = figure.add_subplot(1, 1, 1)
    p.set_title("Total votes per poll")
    p.set_ylabel("Vote count")
    p.bar(
        range(len(ys)),
        ys,
        tick_label=categories)
    return figure
