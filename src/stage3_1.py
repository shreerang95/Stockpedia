import sqlite3
from sqlite3 import Error
import datetime
import json
import keyword_extractor as key_ex
import stage3


class News_Keywords:
    def __init__(self):
        self.database = "newsdata.db"
        self.conn = None
        self.goto_stage3 = None
        self.news_string = ["", "", ""]
        self.keywords = []
        self.start_date = []
        self.end_date = []

        pass

    def create_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            return self.conn
        except Error as e:
            print(e)

        return None


    def get_keywords(self):
        for i in range(len(self.start_date)):
            self.keywords.append(key_ex.findKeywords(self.news_string[i]))


    def select_task_by_ticker(self, ticker, start_date, end_date, news):

        # fetching news from db
        cur = self.conn.cursor()
        news1 = news

        for i in range(len(start_date)):

            news = news1
            cur.execute("SELECT title,summary FROM news_data WHERE ticker=? and publication_date between ? and ? ",
                        (ticker, start_date[i], end_date[i],))

            rows = cur.fetchall()


            for row in rows:
                news = news + "'\ '" + row[0]
                news = news + "'\ '" + row[1]

            news = news + "'"

            self.news_string[i] = self.news_string[i] + news


    def close_fig(self):
        if(self.goto_stage3 != None):
            self.goto_stage3.close_fig(self.goto_stage3)
            self.goto_stage3 = None

    def fetch_keywords(self, current_date):
        news = "'"
        self.start_date = []
        self.end_date = []
        # company names array and dates
        company_names = []
        date_1 = datetime.datetime.strptime(current_date, "%Y-%m-%d")

        self.start_date.append(str(date_1 - datetime.timedelta(days=15))[0:10])
        self.start_date.append(str(date_1 - datetime.timedelta(days=5))[0:10])
        self.start_date.append(str(date_1 + datetime.timedelta(days=6))[0:10])
        self.end_date.append(str(date_1 - datetime.timedelta(days=6))[0:10])
        self.end_date.append(str(date_1 + datetime.timedelta(days=5))[0:10])
        self.end_date.append(str(date_1 + datetime.timedelta(days=15))[0:10])

        self.create_connection(self.database)

        # fetching top companies of that day
        with open('../Data/top_bottom_companies1.json') as f:
            data = json.load(f)
            for i in data[current_date]:
                company_names.append(i)


        # fetching news for each company
        for i in range(0, len(company_names)):
            company_name = company_names[i]
            self.select_task_by_ticker(company_name, self.start_date, self.end_date, news)


        self.get_keywords()

        self.goto_stage3 = stage3.Shapes(self.keywords, company_names, current_date)
        self.goto_stage3.configure_plot()

