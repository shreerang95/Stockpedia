INSTALLATION GUIDE

In order to run our system, we recommend you install the following tools & libraries:

1.	PyCharm – Editor for Python
2.	Python 3.6 – Install 3.6 version of Python and make sure to have its path mapped in PyCharm
3.	SQLite for Database (Can be avoided if using .db file directly) 
4.	Python Libraries Required for the system to run (Can be installed directly through PyCharm):
5.	Create project in pycharm
6.	Add the "data" and the "src" files to the project folder
7.	Open Pycharm
8.	Go to File->Settings->Project Interpreter->click on the "+" sign below the interpreter path and add the following modules
9.	numpy
10.	matplotlib
11.	mpl-finance
12.	genism
13.	nltk (need to add nlkt.download(‘punkt’)*)
14.	pandas
15.	networkx
16.	mpldatacursors

*In order to download punkt follow the next step
1.	open the file named "similarity check"
2.	uncomment the line import nltk
3.	uncomment the line nltk.download()
4.	a dialog box will open when you execute the project
5.	go to the "All Packages" tab
6.	scroll down to "punkt" and download it
7.	comment the two lines you added above (as they are not required now. You need to run that only once)
8.	Execute the project


The S&P 500 index data are present in the Data folder by the names GSPC_RAW_change, GSPC_RAW_change_1, company_division_1, top_bottom_companies1.json
The news data is stored in the newsdata.db file present in the src folder.
For retrieving the news data from the web API and setting up the database, we have used python script named fetch_data_api.py file, table_create.py, store_data_db.py