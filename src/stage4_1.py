import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mpldatacursor import datacursor



class Node_Link_Vis:
    def __init__(self, company_names, company_news):
        self.companies = company_names
        self.news = company_news
        self.px_final = None
        self.py_final = None
        self.cid = None
        self.fig = None

    def set_figure(self):
        mgr = plt.get_current_fig_manager()
        mgr.window.state('zoomed')

        geo = mgr.window.wm_geometry()
        plt.close()

        px = (geo.split('x'))
        px_1 = int(px[0])
        py = px[1].split('+')[0]
        py_1 = int(py)
        self.px_final = (px_1 / 2) - 10
        self.py_final = (py_1 / 2) - 50
        dpi = self.fig.dpi
        inchx_final = self.px_final/dpi
        inchy_final = (self.py_final/dpi) - 0.3

        plt.close(self.fig)
        self.fig = plt.figure()
        self.fig.set_size_inches(inchx_final,inchy_final)



    def close_fig(self, object):
        plt.close(object.fig)
        object.fig = None

    def draw_node_graph(self):

        company_full_name = []
        top_botoom = ["+", "+", "+", "-", "-", "-"]
        fromNodes = []
        toNodes = []
        allNodes = ["Companies"]
        groups = ["group1"]
        company_news = []


        for i in range(0,len(self.companies)):
            with open('../Data/company_division_1.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if row[0] == self.companies[i]:
                        fromNodes.append("Companies")
                        fromNodes.append(row[2])
                        toNodes.append(row[2])


                        toNodes.append(row[3])
                        company_news.append(row[3])
                        if(row[2] not in allNodes):
                            allNodes.append(row[2])
                            groups.append("group2")
                        company_full_name.append(row[3])
                        allNodes.append(row[3])
                        if(top_botoom[i]=="+"):
                            groups.append("group3")
                        else:
                            groups.append("group4")

        df = pd.DataFrame({'from': fromNodes, 'to': toNodes})
        carac = pd.DataFrame({'ID': allNodes, 'myvalue': groups})

        graph = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

        # The order of the node for networkX is the following order:
        graph.nodes()
        # Thus, we cannot give directly the 'myvalue' column to netowrkX, we need to arrange the order!

        # Here is the tricky part: I need to reorder carac to assign the good color to each node
        carac = carac.set_index('ID')
        carac = carac.reindex(graph.nodes())

        # And I need to transform my categorical column in a numerical value: group1->1, group2->2...
        carac['myvalue']=pd.Categorical(carac['myvalue'])
        carac['myvalue'].cat.codes


        self.fig = plt.figure()
        self.set_figure()


        nx.draw(graph, with_labels=True, node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, node_size=1100, font_size=4)

        formatter = lambda **kwargs: ', '.join(kwargs['point_label'])

        company_news = []
        ctr1 = 0
        for i in allNodes:
            if(i in company_full_name):
                if(len(self.news)!=0):
                    company_news.append(self.news[ctr1])
                else:
                    company_news.append("No News present in database")
                ctr1 = ctr1+1
            else:
                company_news.append(i)

        self.cid = datacursor(hover=True, formatter=formatter, point_labels=company_news, draggable=False,size=4)


        mgr = plt.get_current_fig_manager()
        # mgr.window.state('zoomed')
        geometry = "+"+ str(int(self.px_final) + 20) + "+" + str((4 * (int(self.py_final))) // 3 + 20)
        mgr.window.wm_geometry(geometry)

        self.fig.show()
        # plt.show()

