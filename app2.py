import psycopg2

url = ""
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("select * from users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
