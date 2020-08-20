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


def stacked_bar_chart_example():

    polls = [
        ("Flask vs. Django", 60, 19),
        ("Who will win the election", 15, 36),
        ("Python vs. Java", 26, 40),
        ("Mac vs. Windows", 25, 34),
        ("What is the most popular type of graph?", 20, 13),
        ("who is the podcasting king?", 11, 6)
    ]

    poll_titles = [poll[0] for poll in polls]
    poll_x_coordinates = range(len(polls))
    poll_men = [poll[1] for poll in polls]
    poll_women = [poll[2] for poll in polls]

    figure = plt.figure()
    figure.subplots_adjust(bottom=0.35)
    p = figure.add_subplot()
    p.bar(
        poll_x_coordinates,
        poll_men
    )
    p.bar(
        poll_x_coordinates,
        poll_women,
        bottom=poll_men
    )

    plt.xticks(poll_x_coordinates, poll_titles, rotation=30, ha="right")
    plt.show()


