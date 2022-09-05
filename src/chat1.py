from cgitb import reset
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
    
def run_dataseed(database):
    result = exec_get_all(f'SELECT * FROM %s ' % (database)) 
    
    return result

def run_single_chat(user):
    result = exec_get_all(f'SELECT * FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info."name" = \'%s\'' % (user))

    return result

def run_chat_conversation(sender, receiver, year_start = 0):
    if year_start != 0:
        year_end = year_start+1
        year_start = year_start
        result = exec_get_all(f'SELECT * FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info."name" = \'%s\' OR user_info."name" = \'%s\' AND chat_logs.time_log >= \'%d-01-01\' AND chat_logs.time_log <= \'%d-01-01\'' % (sender, receiver, year_start, year_end))
    else:
        result = exec_get_all(f'SELECT * FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info."name" = \'%s\' OR user_info."name" = \'%s\'' % (sender, receiver))
    
    return result

def run_unread_conversation(user):
    result = exec_get_all(f'SELECT * FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info."name" = \'%s\' AND chat_logs.message_read = FALSE' % (user))
    
    return result

def run_read_conversation(user):
    result = exec_get_all(f'SELECT * FROM chat_logs INNER JOIN user_info ON chat_logs.sender = user_info.id WHERE user_info."name" = \'%s\' AND chat_logs.message_read = TRUE' % (user))

    return result


def run_banned_time(user, year):
    result = exec_get_all(f'Select * from ban_logs INNER JOIN user_info ON ban_logs.user_id = user_info.id WHERE user_info."name" = \'%s\'AND ban_logs.ban_end > \'%d-01-01\'' % (user, year))
    
    return result

def run_user_exists(user):
    result = exec_get_all (f'Select * from user_info where user_info."name" = \'%s\' ' % (user))
    
    return result
    
def main():
    
    
    exec_sql_file("chat.sql")
    
    
    
    
if __name__ == "__main__":
    main()
    
    