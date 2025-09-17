import psycopg2
conn = psycopg2.connect(
database = "postgres",
host = "localhost",
user = "postgres",
password = "trisha123",
port = 5432
)
def create_table():
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists USERS_TABLE(id serial primary key,name TEXT not null,age INT not null,department TEXT not null);")
    conn.commit()
def add_user(name,age,department):
    with conn.cursor() as cursor:
        cursor.execute("insert into USERS_TABLE(name,age,department) values(%s,%s,%s);",(name,age,department))
    conn.commit()
def view_users():
    with conn.cursor() as cursor:
        cursor.execute("select * from USERS_TABLE;")
        rows = cursor.fetchall()
        for row in rows:
            print(f" {row[0]} | {row[1]} | {row[2]} | {row[3]}")
    conn.commit()
def delete_users(id):
    with conn.cursor() as cursor:
        cursor.execute("delete from USERS_TABLE where id = %s;",(id,))
    conn.commit()
def update_user(id,name,age,department):
    with conn.cursor() as cursor:
        cursor.execute("update USERS_TABLE set name = %s ,age = %s ,department = %s where id = %s;",(name,age,department,id))


