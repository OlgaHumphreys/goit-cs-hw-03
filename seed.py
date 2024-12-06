
from faker import Faker
import psycopg2
import random

db_config = {
    "dbname": "postgres_db",
    "user": "postgres_user",
    "password": "postgres_password",
    "host": "localhost",
    "port": 5433
}

# Налаштування Faker
fake = Faker()
def generate_users(n):
    users = [(fake.name(),fake.unique.email()) for _ in range(n)]
    return users

def generate_statuses():
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses

def generate_tasks(n):
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)  # Припускаючи, що у нас є 3 статуси
        user_id = random.randint(1, 10)  # Припускаючи, що у нас є 10 користувачів
        tasks.append((title, description, status_id, user_id))
    return tasks

# Функція для заповнення бази даних
def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        # Вставка користувачів
        users = generate_users(10)
        cur.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", users)
        # Вставка статусів
        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)
        # Вставка завдань
        tasks = generate_tasks(30)
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    print("start")
    populate_database()
    print("end")
