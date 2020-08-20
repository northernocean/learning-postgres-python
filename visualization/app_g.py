import matplotlib.pyplot as plt
import database_g
import charts


def chart_options_for_poll(poll_id: int):
    options = database_g.get_options(poll_id)
    categories = [option[0] for option in options]
    xs = [option[1] for option in options]
    charts.pie_chart(xs=xs, categories=categories)  # sets current figure.
                                                    # We can also assign the return value as a figure
    # show the pie chart ...
    plt.show()


def chart_votes_for_polls():
    polls = database_g.get_poll_votes()
    votes = [poll[1] for poll in polls]
    poll_titles = [poll[0] for poll in polls]
    charts.bar_chart(ys=votes, categories=poll_titles)
    plt.show()


chart_options_for_poll(1)
chart_votes_for_polls()
charts.stacked_bar_chart_example()
charts.custom_legend_example()
