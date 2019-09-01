from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import similarity_check as sim_check
import stage4


class NodeLink(object):

    ctr = 0
    def __init__(self, companies, date, button):
        self.companies = companies
        self.current_date = date
        self.button = button
        self.cid = None
        self.goto_stage4 = stage4.Company_News()

    def set_button_id(self, cid):

        self.cid = cid

    def goto_Stage4(self, event):
        if(self.cid!=None):
            self.goto_stage4.get_company_news(self.current_date,self.companies)

    def close_fig(self):
        self.goto_stage4.close_fig()


class Evo_graph(object):

    def __init__(self, ax1, ax2, fig, text, button):
        self.button = button
        self.cid = None
        self.ax1 = ax1
        self.ax2 = ax2
        self.text = text
        self.return_similarity_matrix=[[],[],[]]
        self.fig = fig

        self.patchl2 = patches.FancyArrowPatch((0, 0.5), (1, 0.6), arrowstyle='<|-|>, head_length=0.1', connectionstyle="arc3, rad=-0.3", dpi_cor=2)
        self.patchl3 = patches.FancyArrowPatch((0.85, 0.7), (1, 0.6), arrowstyle='-', dpi_cor=2)
        self.patchl4 = patches.FancyArrowPatch((0.75, 0.55), (1, 0.61), arrowstyle='-', dpi_cor=2)


        self.patchr1 = patches.FancyArrowPatch((1, 0.6), (0, 0.4), arrowstyle='<->', connectionstyle="arc3, rad=-0.3", dpi_cor=2)
        self.patchr3 = patches.FancyArrowPatch((0.01, 0.39), (0.15, 0.45), arrowstyle='-', dpi_cor=2)
        self.patchr4 = patches.FancyArrowPatch((0.02, 0.41), (0.08, 0.32), arrowstyle='-', dpi_cor=2)


        self.return_similarity_matrix = self.get_similarity_matrix()


    def get_similarity_matrix(self):
        return_matrix = [[], [], []]
        return_matrix[0] = sim_check.generate_similar_words(self.text[1], self.text[0])
        return_matrix[1] = self.text[1]
        return_matrix[2] = sim_check.generate_similar_words(self.text[1], self.text[2])

        return return_matrix

    def draw_evo(self, event):

        self.ax1.add_patch(self.patchl2)
        self.ax1.add_artist(self.patchl3)
        self.ax1.add_patch(self.patchl3)
        self.ax1.add_artist(self.patchl4)
        self.ax1.add_patch(self.patchl4)


        self.ax2.add_patch(self.patchr1)
        self.ax2.add_artist(self.patchr3)
        self.ax2.add_patch(self.patchr3)
        self.ax2.add_artist(self.patchr4)
        self.ax2.add_patch(self.patchr4)

        self.fig.show()


class Shapes:

    def __init__(self, text, companies, date):
        self.cid = 0
        self.cid1 = 0
        self.cid2 = 0
        self.ax = []
        self.current_date = date
        self.figure_index_array = []
        self.phrases_matrix = text
        self.similarity_matrix = None
        self.phrases_array = []
        self.patches_array = []
        self.company_names = companies
        self.nrows = 1
        self.ncols = 3
        self.path = None
        self.verts1 = []
        self.NodeLink = None
        self.evo_graph = None
        self.NodeLink_button = None
        self.Evo_button = None
        self.ax_new = None
        self.ax1 = None
        self.ax2 = None
        self.goto_stage4 = None
        self.vertices1 = None
        self.fig = None
        self.ax_evo = None
        self.px_final = None
        self.py_final = None


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


    def onclick(self, event):
        if(event.inaxes == self.Evo_button.ax):
            self.evo_graph = Evo_graph(self.ax1, self.ax2, self.fig, self.phrases_matrix, self.Evo_button)

            self.similarity_matrix = self.evo_graph.return_similarity_matrix
            self.cid1 = self.Evo_button.on_clicked(self.evo_graph.draw_evo)
            self.phrases_matrix_to_array(self.similarity_matrix)

        else:
            self.NodeLink = NodeLink(self.company_names, self.current_date, self.NodeLink_button)
            self.cid2 = self.NodeLink_button.on_clicked(self.NodeLink.goto_Stage4)
            self.NodeLink.set_button_id(self.cid2)


    def create_shape(self):
        sharp_pts = 8
        radius_of_curvature = .2
        no_of_points = sharp_pts * 3 + 1

        angles = np.linspace(0, 2 * np.pi, no_of_points)

        codes = np.full(no_of_points, Path.CURVE4)

        codes[0] = Path.MOVETO

        vertices = np.stack((np.cos(angles), np.sin(angles)))
        self.vertices1 = vertices.T * (2 * radius_of_curvature * np.random.random(no_of_points) + 1 - radius_of_curvature)[:, None]
        self.vertices1[-1, :] = self.vertices1[0, :]

        self.path = Path(self.vertices1, codes)


    def configure_plot(self):
        self.fig = plt.figure()
        self.set_figure()

        # to configure the plot if you do not know the beforehand
        # figure_index_string = str(self.nrows) + str(self.ncols)
        #
        # for i in range(1, (self.nrows * self.ncols) + 1):
        #     self.figure_index_array.append(figure_index_string + str(i))
        #
        # for i in range(len(self.figure_index_array)):
        #     self.figure_index_array[i] = int(self.figure_index_array[i])
        #

        #
        # for i in self.figure_index_array:
        #     self.ax.append(self.fig.add_subplot(i))

        # axis for different random shapes
        for i in range(self.nrows*self.ncols):
            self.ax.append(plt.subplot2grid((8, 5), (0, i*2), rowspan=6, colspan=1))

        self.ax1 = plt.subplot2grid((8, 5), (0, 1), rowspan=6, colspan=1)
        self.ax1.axis("off")
        self.ax2 = plt.subplot2grid((8, 5), (0, 3), rowspan=6, colspan=1)
        self.ax2.axis("off")

        self.ax_new = plt.subplot2grid((8, 5), (7, 3), rowspan=1, colspan=2)
        self.ax_new.cla()
        self.NodeLink_button = Button(self.ax_new, "Node Link Vis")
        self.NodeLink_button.label.set_fontsize(10)

        self.ax_evo = plt.subplot2grid((8, 5), (7, 0), rowspan=1, colspan=2)
        self.ax_evo.cla()
        self.Evo_button = Button(self.ax_evo, "Evo Graph")
        self.Evo_button.label.set_fontsize(10)


        self.phrases_matrix_to_array(self.phrases_matrix)

    # method to partition keyword phrases into each shape
    # def phrases_per_figure(self):
    #     for i in range(self.nrows * self.ncols):
    #         self.phrases_matrix.append([])
    #
    #     ind = 0
    #     while (ind < len(self.text)):
    #         for j in range(len(self.phrases_matrix)):
    #             k = ind + j
    #             if (k < len(self.text)):
    #                 self.phrases_matrix[j].append(self.text[k])
    #             else:
    #                 break
    #             # print(k)
    #         ind = k + 1
    #
    #     # print(self.phrases_matrix)

    def phrases_matrix_to_array(self,text):
        self.phrases_array=[]
        for i in range(len(text)):
            phrase_text = ""
            for j in range(len(text[i])):
                phrase_text = phrase_text + text[i][j] + '\n'
            self.phrases_array.append(phrase_text)

        self.draw_figure()

    def close_fig(self, object):
        if(self.NodeLink != None):
            self.NodeLink.close_fig()
        plt.close(object.fig)
        object.fig = None

    def draw_figure(self):
        facecol = 'g'
        fontcol = 'k'

        for i in range(len(self.ax)):
            p = self.ax[i].patches
            if(len(p) != 0):
                self.ax[i].clear()
                facecol = 'r'
                fontcol = 'k'

        for i in range(len(self.ax)):
            self.create_shape()
            self.patches_array.append(patches.PathPatch(self.path,alpha=0.4))
            self.patches_array[i].set_facecolor(facecol)
            self.ax[i].add_artist(self.patches_array[i])
            self.ax[i].add_patch(self.patches_array[i])
            self.ax[i].text(0, -0.2, self.phrases_array[i], fontsize='4', verticalalignment="center", horizontalalignment="center", color=fontcol)
            self.ax[i].set_xlim(np.min(self.vertices1) * 1.1, np.max(self.vertices1) * 1.1)
            self.ax[i].set_ylim(np.min(self.vertices1) * 1.1, np.max(self.vertices1) * 1.1)
            self.ax[i].axis('off')



        mgr = plt.get_current_fig_manager()
        # mgr.window.state('zoomed')
        geometry = "+0+"+str((4*(int(self.py_final)))//3 + 20)
        mgr.window.wm_geometry(geometry)



        self.NodeLink = NodeLink(self.company_names,self.current_date,self.NodeLink_button)
        self.NodeLink_button.on_clicked(self.NodeLink.goto_Stage4)

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.subplots_adjust(wspace=0)

        self.fig.suptitle("Keyword cloud and Evolution graph")
        self.fig.show()
        # when executing this file as a standalone
        # plt.show()


