import matplotlib.pyplot as plt
import database_g
import charts

MENU_PROMPT = "Enter 'q' to quit, or anything else to chart a new poll: "
POLL_PROMPT = "Select the poll id to create a pie chart of the vote percentages: "


def chart_options_for_poll(poll_id: int):
    options = database_g.get_options(poll_id)
    categories = [option[0] for option in options]
    xs = [option[1] for option in options]
    charts.pie_chart(xs=xs, categories=categories)  # sets current figure.
                                                    # We can also assign the return value as a figure
    # show the pie chart ...
    plt.show()

    # show the bar chart ...
    chart_votes_for_polls()


def chart_votes_for_polls():
    polls = database_g.get_poll_votes()
    votes = [poll[1] for poll in polls]
    poll_titles = [poll[0] for poll in polls]
    charts.bar_chart(ys=votes, categories=poll_titles)
    plt.show()


def prompt_select_poll(polls):
    for poll in polls:
        print(f"{poll[0]}: {poll[1]}")
    (selected_poll := input(POLL_PROMPT))
    chart_options_for_poll(int(selected_poll))


while (user_input := input(MENU_PROMPT)) != 'q':
    polls = database_g.get_polls()
    prompt_select_poll(polls)
