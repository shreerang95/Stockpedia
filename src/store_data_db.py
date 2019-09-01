import json
from pprint import pprint
import sqlite3
    
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_project(conn, project):
    sql = ''' INSERT INTO news_data(ticker,title,publication_date,summary)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def main():
    database = "newsdata.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        ctr=1
        for ctr in range(1,1000):
            with open(str(ctr)+'.json') as f:
                data = json.load(f)
                for i in range(0,4):
                    ticker = data["data"][i]["ticker"]
                    publication_date = data["data"][i]["publication_date"]
                    summary = data["data"][i]["summary"]
                    title = data["data"][i]["title"]
            
                    project = (ticker,title,publication_date,summary);
                    project_id = create_project(conn, project)
                ctr=ctr+1
       
if __name__ == '__main__':
    main()