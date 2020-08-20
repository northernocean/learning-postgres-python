import os
import psycopg2
from dotenv import load_dotenv

SELECT_POLLS = "select * from polls;"

SELECT_OPTION_IN_POLLS = """
select options.option_text, count(votes.option_id) from options
inner join polls on options.poll_id = polls.id
inner join votes on options.id = votes.option_id
where polls.id = %s
group by options.option_text;"""

load_dotenv()

connection = psycopg2.connect(os.environ["DATABASE_URL"])


def get_polls():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLLS)
            return cursor.fetchall()


def get_options(poll_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_OPTION_IN_POLLS, (poll_id,))
            return cursor.fetchall()
