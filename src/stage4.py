import sqlite3
from sqlite3 import Error
import datetime
import stage4_1 as node


class Company_News:

    def __init__(self):
        self.conn = None
        self.database = "newsdata.db"
        self.goto_stage4_vis = None

    def close_fig(self):
        if(self.goto_stage4_vis != None):
            self.goto_stage4_vis.close_fig(self.goto_stage4_vis)
            self.goto_stage4_vis = None

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def select_task_by_ticker(self, conn, ticker, start_date, end_date, news):

        # fetching news from db
        cur = conn.cursor()
        cur.execute("SELECT title,summary FROM news_data WHERE ticker=? and publication_date between ? and ? ",
                    (ticker, start_date, end_date,))

        rows = cur.fetchall()

        for row in rows:
            news = news + "'\ '" + row[0]
            news = news + "'\ '" + row[1]

    def get_company_news(self, current_date, company_names):
        date_1 = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        start_date = date_1
        end_date = date_1

        company_news = []

        # create a database connection
        self.conn = self.create_connection(self.database)

        # fetching news for each company
        for i in range(0, len(company_names)):
            comapny_name = company_names[i]
            news = []
            ctr = 0

            while len(news) < 3 and ctr < 15:
                with self.conn:
                    cur = self.conn.cursor()
                    cur.execute("SELECT summary FROM news_data WHERE ticker=? and publication_date between ? and ?",
                                (comapny_name, start_date, end_date))

                    rows = cur.fetchall()
                    if (len(rows) > 0):
                        for row in rows:
                            news.append(row[0])
                    else:
                        ctr = ctr + 1
                        start_date = start_date - datetime.timedelta(days=1)
                        end_date = end_date + datetime.timedelta(days=1)

            s = "News: \n"
            sr = ["   1.", "   2.", "   3."]
            for i in range(1, len(news) + 1):
                if (i % 3 == 1):
                    s = s + sr[0] + news[i - 1] + "\n"
                elif (i % 3 == 2):
                    s = s + sr[1] + news[i - 1] + "\n"
                else:
                    company_news.append(s + sr[2] + news[i - 1])
                    s = "News: \n"


        self.goto_stage4_vis = node.Node_Link_Vis(company_names, company_news)
        self.goto_stage4_vis.draw_node_graph()

