import psycopg2

conn = psycopg2.connect(
    dbname="weather_db",
    user="airflow",
    password="airflow",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
# query = "SELECT * FROM public.weather_data LIMIT 10;"
cur.execute(query)
rows = cur.fetchall()

print(rows)
for row in rows:
    print(row)

cur.close()

print("Connected to the database successfully!")

conn.close()
