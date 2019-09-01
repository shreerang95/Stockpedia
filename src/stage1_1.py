# Libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from matplotlib.widgets import Button
import stage1_1_date_map
import stage1_1_color_map
import stage2_1

stage2_flag = {"flag": 0}
mpl.use("TkAgg")

class Year(object):
    # year = 2016

    def __init__(self, fig,year):
        self.fig = fig
        self.year = year
        self.stage1 = None

    def update_year(self, event):
        self.year = ((self.year + 1) % 2) + 2016
        self.stage1 = Stage_1(self.year, self.fig)
        self.stage1.plot_data()





class Stage_1:
    def __init__(self, year, fig):

        self.goto_stage2 = None
        self.year = year
        self.fig = fig
        self.set_figure()
        self.callback = Year(fig,self.year)
        self.month_figure = None
        self.px_final = None
        self.py_final = None


    def set_figure(self):
        mgr = plt.get_current_fig_manager()
        mgr.window.state('zoomed')
        mgr.window.wm_geometry("+0+0")

        geo = mgr.window.wm_geometry()
        plt.close()
        px = (geo.split('x'))
        px_1 = int(px[0])
        py = px[1].split('+')[0]
        py_1 = int(py)
        self.px_final = (px_1 / 2) - 10
        self.py_final = (py_1 / 2) + 30
        dpi = self.fig.dpi
        inchx_final = self.px_final/dpi
        inchy_final = self.py_final/dpi
        self.fig,self.ax = plt.subplots()
        self.fig.set_size_inches(inchx_final,inchy_final)
        self.ax.axis("auto")

    def convert_date(self, date_bytes):
        return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))


    def plot_data(self):
        self.ax.cla()

        year_start_date_string = "01-01-"+str(self.year)
        year_end_date_string = "31-12-"+str(self.year)

        year_start_date = dt.datetime.strptime(year_start_date_string, "%d-%m-%Y")
        year_end_date = dt.datetime.strptime(year_end_date_string, "%d-%m-%Y")


        i_int_start_date = mdates.date2num(year_start_date)
        i_int_end_date = mdates.date2num(year_end_date)
        i_int_day = year_start_date.weekday()

        stage1_1_date_map.year_week_calculator(i_int_start_date, i_int_end_date,i_int_day, week1, week2, week3, week4, week5, week6)

        d1 = []
        p1 = []
        n1 = []

        for i in range(len(d)):
            date0 = mdates.num2date(d[i])

            date0_year = date0.year
            if(date0_year == self.year):
                d1.append(date0)
                p1.append(p[i])
                n1.append(n[i])

        stage1_1_color_map.day_color_map(week1,week1_color,d1,p1,n1)
        stage1_1_color_map.day_color_map(week2,week2_color,d1,p1,n1)
        stage1_1_color_map.day_color_map(week3,week3_color,d1,p1,n1)
        stage1_1_color_map.day_color_map(week4,week4_color,d1,p1,n1)
        stage1_1_color_map.day_color_map(week5,week5_color,d1,p1,n1)
        stage1_1_color_map.day_color_map(week6,week6_color,d1,p1,n1)

        mypie_textprops = dict(verticalalignment='center', horizontalalignment='center', fontsize='xx-small')

        # the 1st ring depicting the months
        mypie = self.ax.pie(month_size, radius=3, labels=months, labeldistance=1.1, colors=['#000000'], startangle=90, counterclock=False)
        plt.setp(mypie[0], width=0.3, edgecolor='white')

        # the 2nd ring depicting days
        mypie2, temp = self.ax.pie(daygroups_size, radius=2.7, labels=daygroups, labeldistance=0.9, colors='c', rotatelabels=True, startangle=90, counterclock=False, textprops=mypie_textprops)
        plt.setp(mypie2, width=0.5, edgecolor='white')

        # the 3rd ring depicting the 1st week of the respective month
        mypie3, temp = self.ax.pie(week1_size, radius=2.2, startangle=90, counterclock=False, colors=week1_color)
        plt.setp(mypie3, width=0.2, edgecolor='white')

        # the 4th ring depicting the 2nd week of the respective month
        mypie4, temp = self.ax.pie(week2_size, radius=2, startangle=90, counterclock=False, colors=week2_color)
        plt.setp(mypie4, width=0.2, edgecolor='white')

        # the 5th ring depicting the 3rd week of the respective month
        mypie5, temp = self.ax.pie(week3_size, radius=1.8, startangle=90, counterclock=False, colors=week3_color)
        plt.setp(mypie5, width=0.2, edgecolor='white')

        # the 6th ring depicting the 4th week of the respective month
        mypie6, temp = self.ax.pie(week4_size, radius=1.6, startangle=90, counterclock=False, colors=week4_color)
        plt.setp(mypie6, width=0.2, edgecolor='white')

        # the 7th ring depicting the 5th week of the respective month
        mypie7, temp = self.ax.pie(week5_size, radius=1.4, startangle=90, counterclock=False, colors=week5_color)
        plt.setp(mypie7, width=0.2, edgecolor='white')

        # the 8th ring depicting the 5th week of the month starting on saturday or sunday
        mypie8, temp = self.ax.pie(week6_size, radius=1.2, startangle=90, counterclock=False, colors=week6_color)
        plt.setp(mypie8, width=0.2, edgecolor='white')


        plt.title("Stockpedia Circular Calendar Graph",y=1.9)

        pos_col = ["#a1d99b", "#41ab5d", "#006d2c", "#00441b"]
        neg_col = ["#fc9272", "#ef3b2c", "#a50f15", "#67000d"]
        pos_leg = ["0 to 25%", "25% to 50%", "50% to 75%", "more than 75%"]
        neg_leg = ["0 to -25%", "-25% to -50%", "-50% to -75%", "less than -75%"]


        # axis to display the legend
        ax1 = plt.axes([0.90, 0.85, 0.1, 0.075])
        ax1.cla()
        ax1.axis('off')
        ax1.plot([], [], linewidth=5, label=pos_leg[0],color=pos_col[0])
        ax1.plot([], [], linewidth=5, label=pos_leg[1], color=pos_col[1])
        ax1.plot([], [], linewidth=5, label=pos_leg[2], color=pos_col[2])
        ax1.plot([], [], linewidth=5, label=pos_leg[3], color=pos_col[3])
        ax1.legend(loc="upper left", bbox_to_anchor=(-0.9,0.5), fontsize='x-small')

        # axis to display the legend
        ax2 = plt.axes([0.15, 0.85, 0.1, 0.075])
        ax2.cla()
        ax2.axis('off')
        ax2.plot([], [], linewidth=5, label=neg_leg[0],color=neg_col[0])
        ax2.plot([], [], linewidth=5, label=neg_leg[1], color=neg_col[1])
        ax2.plot([], [], linewidth=5, label=neg_leg[2], color=neg_col[2])
        ax2.plot([], [], linewidth=5, label=neg_leg[3], color=neg_col[3])
        ax2.legend(loc="upper right",bbox_to_anchor=(0.5,0.5),fontsize="x-small")


        # axis to display the button to change the year
        ax_new = plt.axes([0.85, 0.05, 0.1, 0.075])
        ax_new.cla()
        button_year = Button(ax_new,self.year)

        button_year.on_clicked(self.callback.update_year)


        def onclick(event1):

            stage2_flag["flag"] = 1

            if(event1.inaxes == ax_new):
                if (self.goto_stage2 != None):
                    self.goto_stage2.close_fig(self.goto_stage2)

            for pie in mypie[0]:
                hit,_= pie.contains(event1)
                if(hit):
                    pie.set_facecolor((1.0, 0.0, 0.0, 1.0))
                    self.fig.show()
                    click_month = pie.get_label()
                    click_year = str(self.year)

                    if(self.goto_stage2 != None):
                        self.goto_stage2.close_fig(self.goto_stage2)

                    self.goto_stage2 = stage2_1.Stage2(click_month, click_year)
                    self.goto_stage2.plot_data()
                else:
                    pie.set_facecolor((0.0, 0.0, 0.0, 1.0))


            self.fig.show()


        self.month_figure = mypie[0][0].figure
        plt.subplots_adjust(top=0.60, bottom=0.3)
        cid = self.month_figure.canvas.mpl_connect('button_press_event', onclick)

        mgr = plt.get_current_fig_manager()
        # to show window in full screen uncomment the next line
        # mgr.window.state('zoomed')
        mgr.window.wm_geometry("+0+0")

        self.fig.show()
        plt.show()



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_size = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dates = []
daygroups = []
daygroups_size = []
week1 = []
week2 = []
week3 = []
week4 = []
week5 = []
week6 = []
week1_size = []
week2_size = []
week3_size = []
week4_size = []
week5_size = []
week6_size = []
week1_color = []
week2_color = []
week3_color = []
week4_color = []
week5_color = []
week6_color = []

day_date_group = []
group_string = ""

for i in months:
    for j in days:
        daygroups.append(j[:3])
        daygroups_size.append(1)
        dates.append(0)
        week1_size.append(1)
        week1.append([])
        week1_color.append([])
        week2_size.append(1)
        week2.append([])
        week2_color.append([])
        week3_size.append(1)
        week3.append([])
        week3_color.append([])
        week4_size.append(1)
        week4.append([])
        week4_color.append([])
        week5_size.append(1)
        week5.append([])
        week5_color.append([])
        week6_size.append(1)
        week6.append([])
        week6_color.append([])




fig, ax = plt.subplots()

ax.axis('auto')
stage_1 = Stage_1(2016,fig)
d, o, h, l, c, p, n = np.loadtxt('../Data/GSPC_RAW_change_1.csv', delimiter=',', unpack=True, converters={0: stage_1.convert_date})
stage_1.plot_data()
