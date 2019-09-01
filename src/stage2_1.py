import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.dates as mdates
import datetime as dt
import math
from mpl_finance import candlestick_ohlc
from matplotlib.widgets import Button
import stage3_1
import json
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)


class Insight(object):

    def __init__(self, date, button):
        self.date = date
        self.nkeywords = stage3_1.News_Keywords()
        self.button = button


    def goto_data_fetch(self, event):
        self.nkeywords.fetch_keywords(self.date)
        self.button.disconnect(self.cid)


    def disconnect_button(self, cid):
        self.cid = cid

    def close_fig(self):
        self.nkeywords.close_fig()
        del self


class Stage2:

    def __init__(self, month, year):
        self.month = {
            'January': "15-01",
            'February': "15-02",
            'March': "15-03",
            'April': "15-04",
            'May': "15-05",
            'June': "15-06",
            'July': "15-07",
            'August': "15-08",
            'September': "15-09",
            'October': "15-10",
            'November': "15-11",
            'December': "15-12"
        }

        self.init_flag = 0
        self.incorrect_date_flag = 0
        self.init_flag_stage3 = 0

        self.px_final = None
        self.py_final = None

        self.datestring = self.month[month]+"-"+year
        self.date = dt.datetime.strptime(self.datestring,"%d-%m-%Y")

        self.fig = plt1.figure(2)
        self.set_figure()

        plt1.subplots_adjust(left=0.08, right=0.95)


        # axis to display Line Chart
        self.ax1 = plt1.subplot2grid((10, 6), (0, 2), rowspan=3, colspan=4)
        plt1.xlabel('Date',fontsize=8)
        plt1.ylabel('S&P 500 Percent change',fontsize=8)

        # axis to display legend
        self.ax3 = plt1.subplot2grid((10, 6), (0, 0), rowspan=2, colspan=1)
        ohlc_legend_pos = 0, 1, 3, 0, 2
        ohlc_legend_pos_arr = []
        ohlc_legend_pos_arr.append(ohlc_legend_pos)
        candlestick_ohlc(self.ax3, ohlc_legend_pos_arr, width=0.4, colorup='g', colordown='r')
        self.ax3.axis("off")


        self.text_props = dict(fontsize="x-small")
        offsetbox = TextArea("High", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,3),
                            xybox=(-30, 0),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax3.add_artist(ab)

        offsetbox = TextArea("Low", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,0),
                            xybox=(-30, 0),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax3.add_artist(ab)

        offsetbox = TextArea("Open", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,1),
                            xybox=(20, -15),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax3.add_artist(ab)

        offsetbox = TextArea("Close", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,2),
                            xybox=(20, 15),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax3.add_artist(ab)

        # axis to display legend
        self.ax4 = plt1.subplot2grid((10, 6), (3, 0), rowspan=2, colspan=1)
        ohlc_legend_pos = 0, 2, 3, 0, 1
        ohlc_legend_pos_arr=[]
        ohlc_legend_pos_arr.append(ohlc_legend_pos)
        candlestick_ohlc(self.ax4, ohlc_legend_pos_arr, width=0.4, colorup='g', colordown='r')
        self.ax4.axis("off")


        offsetbox = TextArea("High", minimumdescent=False,textprops=self.text_props)
        ab = AnnotationBbox(offsetbox, (0,3),
                            xybox=(-30, 0),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax4.add_artist(ab)

        offsetbox = TextArea("Low", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,0),
                            xybox=(-30, 0),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax4.add_artist(ab)

        offsetbox = TextArea("Open", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,2),
                            xybox=(20, 15),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax4.add_artist(ab)

        offsetbox = TextArea("Close", minimumdescent=False,textprops=self.text_props)

        ab = AnnotationBbox(offsetbox, (0,1),
                            xybox=(20, -15),
                            xycoords='data',
                            boxcoords="offset points",
                            arrowprops=dict(arrowstyle="->"))
        self.ax4.add_artist(ab)

        # axis to show top and bottom companies box
        self.ax5 = plt1.subplot2grid((10, 6), (8, 0), rowspan=2, colspan=1)
        self.ax5.axis("off")

        # axis to display the button to transition to the next stage
        self.ax_new = plt1.subplot2grid((10, 6), (8, 5), rowspan=2, colspan=1)
        self.insight = None
        self.ax_new.cla()
        self.button_insight = Button(self.ax_new, "GET INSIGHT")
        self.button_insight.label.set_fontsize(8)
        self.current_date = None

        # axis to show the OHLC graph
        self.ax2 = plt1.subplot2grid((10, 6), (6, 2), rowspan=3, colspan=3)
        plt1.xlabel('Date',fontsize=8)
        plt1.ylabel('S&P 500 Price',fontsize=8)


        self.d2 = []
        self.p2 = []

        self.ax1.grid(b=True)
        self.ax2.grid(b=True)

        self.d, self.o, self.h, self.l, self.c, self.p = np.loadtxt('../Data/GSPC_RAW_change.csv', delimiter=',', unpack=True,
                                      converters={0: self.convert_date})


        self.start_date_string = "01-01-2016"
        self.end_date_string = "31-12-2017"
        self.cid = None
        self.cid1 = None


    def set_figure(self):
        mgr = plt1.get_current_fig_manager()
        mgr.window.state('zoomed')

        geo = mgr.window.wm_geometry()
        plt1.close()

        px = (geo.split('x'))
        px_1 = int(px[0])
        py = px[1].split('+')[0]
        py_1 = int(py)
        self.px_final = (px_1 / 2) - 10
        self.py_final = (py_1 / 2) + 30
        dpi = self.fig.dpi
        inchx_final = self.px_final/dpi
        inchy_final = self.py_final/dpi
        plt1.close(self.fig)
        self.fig = plt1.figure()
        self.fig.set_size_inches(inchx_final,inchy_final)



    def close_fig(self,object):
        plt1.close(object.fig)
        if(self.insight != None):
            self.insight.close_fig()

    def onclick(self,event):
        # reference to display the event data
        # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        #       ('double' if event.dblclick else 'single', event.button,
        #        event.x, event.y, event.xdata, event.ydata))


        if(event.inaxes != self.button_insight.ax):
            self.update_ax2(mdates.num2date(event.xdata))
        else:
            if(self.incorrect_date_flag == 0):
                self.insight = Insight(self.current_date,self.button_insight)
                self.cid1 = self.button_insight.on_clicked(self.insight.goto_data_fetch)
                self.insight.disconnect_button(self.cid1)


    def convert_date(date_bytes):
        return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))

    def get_companies_for_date(self,date):
        company_names = []
        with open('../Data/top_bottom_companies1.json') as f:
            data = json.load(f)
            if(date not in data.keys()):
                print("Incorrect date")
                self.incorrect_date_flag = 1
                return
            else:
                for i in data[date]:
                    company_names.append(i)

        return company_names


    def update_ax2(self,data):
        self.incorrect_date_flag = 0
        if(self.insight != None):
            self.insight.close_fig()
            self.insight = None

        self.ax2.cla()
        plt1.xlabel('Date')
        plt1.ylabel('S&P 500 Price')

        self.ax2.grid(b=True)


        dint = mdates.date2num(data)
        dintmin = math.floor(dint - 15)
        dintmax = math.floor(dint + 15)


        self.ax1.fill_between(self.d2, self.p2, 0, facecolor='w',edgecolor='k',linewidth=0.2)
        self.ax1.axhline(0,color='k',linewidth=0.5)

        #on change remove the selection from previous click

        self.ax1.fill_between(self.d2, 3, -3, where=(self.d2 < dintmin), facecolor='w', edgecolor='w',linewidth=0.2)
        self.ax1.fill_between(self.d2, 3, -3, where=(self.d2 > dintmin), facecolor='g',edgecolor='g',linewidth=0.2,alpha=0.3)
        self.ax1.fill_between(self.d2, 3, -3, where=(self.d2 > dintmax), facecolor='w', edgecolor='w',linewidth=0.2)

        self.ax1.fill_between(self.d2, self.p2, 0, where=(self.d2 < dintmin), facecolor='w', edgecolor='k',linewidth=0.2)
        self.ax1.axhline(0, color='k', linewidth=0.5)
        self.ax1.fill_between(self.d2, self.p2, 0, where=(self.d2 > dintmin), facecolor='b',edgecolor='k',linewidth=0.2)
        self.ax1.axhline(0,color='k',linewidth=0.5)
        self.ax1.fill_between(self.d2, self.p2, 0, where=(self.d2 > dintmax), facecolor='w',edgecolor='k',linewidth=0.2)



        d1 = []
        flag = 0
        for i in range(len(self.d)):
            if (self.d[i] > dintmin):
                flag = 1
                istart = i
                d1.append(self.d[i])
            if (self.d[i] > dintmax):
                iend = i
                break
        istart = iend - len(d1) + 1

        ohlc_selected = []

        for i in range(istart, iend + 1):
            append_me = self.d[i], self.o[i], self.h[i], self.l[i], self.c[i]
            ohlc_selected.append(append_me)

        candlestick_ohlc(self.ax2, ohlc_selected, width=0.4, colorup='g', colordown='r')
        self.ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        for label in self.ax2.xaxis.get_ticklabels():
            label.set_rotation(45)


        self.current_date = data.strftime("%Y-%m-%d")


        companies = self.get_companies_for_date(self.current_date)
        companies_string = "Date: " + self.current_date + "\n" + "Companies"
        companies_bbox = dict(boxstyle="round",facecolor="c")
        if(companies != None):

            for i in range(len(companies)):
                if(i==0):
                    companies_string = companies_string + "\n" + "Top 3:-"
                if(i==3):
                    companies_string = companies_string + "\n" + "Bottom 3:-"
                companies_string = companies_string + "\n" + companies[i]
        else:
            self.ax5.cla()
            self.ax5.axis("off")

        self.ax5.text(0, 0, companies_string, fontsize="xx-small", bbox=companies_bbox)



        mgr = plt1.get_current_fig_manager()
        # mgr.window.state('zoomed')
        geometry = "+"+str(int(self.px_final) + 20)+"+0"
        mgr.window.wm_geometry(geometry)

        self.fig.suptitle("Line Chart and OHLC graph")
        self.fig.show()

    def convert_date(self,date_bytes):
        return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))

    def plot_data(self):
        d1 = []
        p1 = []

        start_date = dt.datetime.strptime(self.start_date_string, "%d-%m-%Y")
        end_date = dt.datetime.strptime(self.end_date_string, "%d-%m-%Y")

        i_int_start_date = mdates.date2num(start_date)
        i_int_end_date = mdates.date2num(end_date)

        for i in range(len(self.d)):
            if self.d[i] > i_int_start_date and self.d[i] < i_int_end_date:
                d1.append(self.d[i])
                p1.append(self.p[i])

        i = 0
        y = len(d1)


        close = '{:.2f}'.format(self.c[-1])

        self.d2 = np.asarray(d1)
        self.p2 = np.asarray(p1)

        self.ax1.plot_date(self.d2, self.p2, '-', linewidth=0.01, color='k')

        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        for label in self.ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        self.update_ax2(self.date)
