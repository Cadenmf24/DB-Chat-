from cgitb import reset
import csv
from datetime import date, datetime
from sqlite3 import Timestamp
from unittest import result
from src.swen344_db_utils import exec_sql_file
from src.swen344_db_utils import *


from src.swen344_db_utils import connect
    
def rebuildTables():
    conn = connect()
    cur = conn.cursor()
    drop_sql = """
        DROP TABLE IF EXISTS example_table
    """
    create_sql = """
        CREATE TABLE example_table(
            example_col VARCHAR(40)
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)
    conn.commit()
    conn.close()

def run_single_chat(user):
    result = exec_get_all('SELECT body FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info.name = %s' , [user])

    return result

def run_chat_conversation(sender, receiver, year_start = 0):
    if year_start != 0:
        year_end = date(year_start + 1,1,1)
        year_start = date(year_start,1,1)
        result = exec_get_all('SELECT sender, receiver, time_log FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE (user_info.name = %s OR user_info.name = %s) AND chat_logs.time_log > %s AND chat_logs.time_log < %s' , [sender, receiver, year_start, year_end])
    else:
        result = exec_get_all('SELECT sender, receiver FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info.name = %s OR user_info.name = %s' , [sender, receiver])
    
    return result

def run_unread_conversation(user):
    result = exec_get_all('SELECT sender, receiver, message_read, message_id FROM chat_logs INNER JOIN user_info ON chat_logs.receiver = user_info.id WHERE user_info.name = %s AND chat_logs.message_read = FALSE' , [user])
    
    return result

def run_read_conversation(user):
    result = exec_get_all('SELECT sender, receiver, message_read, message_id FROM chat_logs INNER JOIN user_info ON chat_logs.receiver = user_info.id WHERE user_info.name = %s AND chat_logs.message_read = TRUE' , [user])

    return result

def run_banned_time(user, year):
    year = date(year,1,1)
    result = exec_get_all('SELECT user_id from ban_logs INNER JOIN user_info ON ban_logs.user_id = user_info.id WHERE user_info.name = %s AND ban_logs.ban_end > %s' , [user, year])
    
    return result

def run_user_exists(user):
    result = exec_get_all ('SELECT name from user_info where user_info.name = %s', [user])
    
    return result

def create_new_user(username, date_created):
    result = exec_commit('INSERT INTO user_info(name, date_created) VALUES (%s , %s)', (username, date_created))
    
    return result

def read_message(message_id):
    result = exec_commit('UPDATE chat_logs SET message_read = TRUE WHERE id = %s', message_id)
    
    return result

def create_message(sender, receiver, body, time_log):
    exec_commit('INSERT INTO chat_logs (sender, receiver, body, time_log) VALUES (%s, %s, %s, %s)', (sender, receiver, body, time_log))
    result = exec_get_all('SELECT message_id FROM chat_logs WHERE chat_logs.sender = %s AND chat_logs.receiver = %s AND chat_logs.body = %s AND chat_logs.time_log = %s', (sender,receiver,body,time_log))
    
    return result

def get_message(id):
    result = exec_get_all('Select sender, receiver, body, message_read FROM chat_logs WHERE chat_logs.message_id = %s', (id))
    
    return result
    
def change_username(old_name, new_name, time):
    exec_commit('UPDATE user_info SET name = %s, date_created = %s WHERE name = %s', [new_name, time, old_name])
    
    # result = exec_get_all('SELECT name, date_created FROM user_info WHERE user_info.name = %s', )
    
    return result

def read_csv(file):
    with open(file, newline= '\n' ) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # print(row)
            # print(', '.join(row))
            # print(', '.join(row))
            # print(row[0])
            # print(row[0])
            # print(', '.join(row[1:]))
            
            abbott_id = exec_get_all('Select contact FROM user_info WHERE name = \'Abbott\'')
            costello_id = exec_get_all('Select contact FROM user_info WHERE name = \'Costello\'')
            
            if (row[0] == 'Abbott'):
                exec_commit('INSERT INTO chat_logs (sender, receiver, body, time_log) VALUES (%s, %s, %s, %s)', [abbott_id[0], costello_id[0], ', '.join(row[1:]), datetime.now()])
                
            if (row[0] == 'Costello'):
                exec_commit('INSERT INTO chat_logs (sender, receiver, body, time_log) VALUES (%s, %s, %s, %s)', [costello_id[0], abbott_id[0], ', '.join(row[1:]), datetime.now()])

    
    
    
def main():
    
    exec_sql_file("chat.sql")
    
if __name__ == "__main__":
    main()
    
    