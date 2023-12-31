import sqlite3
from sqlite3 import Error

# creates connection to local database on sqlite3 studio #
def connect_db():
    db_file = "C:\\Users\\n1delarosa\\SQLite Data\\todo_list.db"
    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

# queries for all the data in the taskList table #
def select_all():
    db_conn = connect_db()
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM taskList")

    task_data = db_cursor.fetchall()

    return task_data

# inserts new taskLists input data into the database #
def add_task(priority_input, task_input, date_input):
    db_conn = connect_db()
    db_cursor = db_conn.cursor()

    sql_cmd = """
                INSERT INTO taskList (Priority, Task, Complete_By)
                VALUES (?, ?, ?);
              """
    
    dataList = [
        priority_input,
        task_input,
        date_input
    ]

    db_cursor.execute(sql_cmd, dataList)
    db_conn.commit()

    return None

# deletes certain row based on ID from id_input from the database #
def del_task(id_input):
    db_conn = connect_db()
    db_cursor = db_conn.cursor()

    sql_cmd = """
                DELETE FROM taskLisT WHERE ID = ?
              """
    
    db_cursor.execute(sql_cmd, (id_input,))
    db_conn.commit()

    return None

# gets a single table row from database based on ID #
def edit_task(id_input):
    db_conn = connect_db()
    db_cursor = db_conn.cursor()

    sql_cmd = """
                SELECT * FROM taskLisT WHERE ID = ?
              """
    
    db_cursor.execute(sql_cmd, (id_input,))
    row_data = db_cursor.fetchone()

    return row_data
    