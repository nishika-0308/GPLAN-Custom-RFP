import tkinter as tk
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def mapper(g):
    nodes = list(g.nodes())
    map = {}
    for k in range(0, len(g.nodes)):
        if nodes[k] == 0:
            map[0] = "LR"
        if nodes[k] == 1:
            map[1] = "MR"
        if nodes[k] == 2:
            map[2] = "K"
        if nodes[k] == 3:
            map[3] = "BR"
        if nodes[k] == 4:
            map[4] = "DR"
        if nodes[k] == 5:
            map[5] = "CR"
        if nodes[k] == 6:
            map[6] = "SR"
        if nodes[k] == 7:
            map[7] = "2R"
        if nodes[k] == 8:
            map[8] = "GR"
        if nodes[k] == 9:
            map[9] = "B"
        if nodes[k] == 10:
            map[10] = "E"
        if nodes[k] == 11:
            map[11] = "S"
    return map

class MultiGraph:
    def __init__(self) -> None:
        self.root = tk.Toplevel()     
        self.root.title('Multiple Graphs')
        self.root.geometry(str(1000) + 'x' + str(400))
        self.final_graph = []
        self.final_graph_map = {}
        self.positions = None
        # self.root.pack_propagate(0)        self.final_graph_map = []
        self.final_graph_names = []
        self.waitvar = tk.IntVar()


        border_details = {'highlightbackground': 'black', 'highlightcolor': 'black', 'highlightthickness': 1}
        # main frame
        self.frame=tk.Frame(self.root,width=700,height=300,bg='black')
        self.frame.grid(row=0,column=0)   
        
        # first canvas
        self.canvas = tk.Canvas(self.frame, **border_details, width = self.root.winfo_screenwidth() - 50, height= 1000)
        canvas = self.canvas
        canvas.pack_propagate(0)
        

        # vertical scrollbar
        scroll_y = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        scroll_y.grid(row=0,column=5, rowspan=4,sticky='ns')        
        scroll_y.config(command=canvas.yview)
       
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.configure(scrollregion=canvas.bbox("all"))

        # added lines
        canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.grid(row=0, column=0, sticky='nsew', padx=4, pady=4)

        # second frame
        self.second_frame=tk.Frame(canvas,width=10000,height=10000,)
        canvas.create_window((0,0),window=self.second_frame, anchor='nw')   
         
        # self.frame = tk.Frame(self.canvas)
        # self.frame.grid()
        # self.canvas.grid(column=0, row=0, padx=2, pady=2)  
        # canvas.configure(scrollregion=canvas.bbox("all")) 
           
    def start(self,redge):
        self.function(redge)     
        print("start", self.final_graph_names)
        # input("hi")
        self.root.wait_variable(self.waitvar)
        return self.final_graph, self.final_graph_names, self.positions
        # self.root.mainloop()
    
    def function(self,redge): 
        # for i in [1,2,3]:
        fig = []
        plot1 = []
        print("inside func")
        for x in range(0,len(redge)):
            i = int(x/4)
            j = int(x%4)

            fig.append(Figure(figsize = (3, 3),dpi = 100, frameon=self.canvas))
            plot1.append(fig[x].add_subplot(111))
            self.plot(redge[x],plot1[x],fig[x],2*i,j)

    def plot(self,l,plot1,fig,i,j):
        g = nx.Graph()
        g.add_edges_from(l)
        nodes = list(g.nodes())

        map = mapper(g)
        g = nx.relabel_nodes(g, map, copy=False)

        gless = nx.Graph()
        gless.add_edges_from(l)
        nx.draw(g,ax=plot1, with_labels = True)
        canvas = FigureCanvasTkAgg(fig,master = self.second_frame )
        canvas.draw()
        canvas.get_tk_widget().grid(row=i, column=j)
        b1 = []
        b1.append(tk.Button(self.second_frame,width=15,text='Produce a floorplan',relief='raised',command=lambda : self.clicked(gless)))
        b1[len(b1) - 1].grid(row=i+1,column=j,padx=5,pady=5)

    def clicked(self,g):
        print("Here are the edges and nodes in MultiGraphCustomGUI")
        print(g.edges())
        print(g.nodes())
        self.final_graph = g.edges()
        self.final_graph_map = mapper(g)
        self.final_graph_names = list(self.final_graph_map.values())
        coordinates = nx.planar_layout(g)
        positions = []
        for node in coordinates:
            positions.append(coordinates[node].tolist())
        self.positions = positions
        self.waitvar.set(1)
        self.root.destroy()
