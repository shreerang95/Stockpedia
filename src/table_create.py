import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = "newsdata.db"
 
    sql_create_news_table = """ CREATE TABLE IF NOT EXISTS news_data (
                                        ticker text,
                                        title text,
                                        publication_date text,
                                        summary text
                                    ); """
 
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_news_table)
       
    else:
        print("Error! cannot create the database connection.")
        
if __name__ == '__main__':
    main()
