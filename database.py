import sqlite3
from sqlite3 import Error

def connect_db():
    db_file = "C:\\Users\\n1delarosa\\SQLite Data\\todo_list.db"
    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

def select_all():
    db_conn = connect_db()
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM taskList")

    task_data = db_cursor.fetchall()

    return task_data

def add_task(priority_input, task_input):
    db_conn = connect_db()
    db_cursor = db_conn.cursor()

    sql_cmd = """
                INSERT INTO taskList (Priority, Task)
                VALUES (?, ?);
              """
    
    dataList = [
        priority_input,
        task_input
    ]

    #sql_cmd = "INSERT INTO taskList (Priority, Task) Values " + "(" + priority_input + "," + task_input + ")"
    db_cursor.execute(sql_cmd, dataList)
    db_conn.commit()

    return None