import tkinter as tk
import RFPsearch
import networkx as nx
import matplotlib.pyplot as plt
import MultiGraphCustomGUI


class CustomRFPPopup:

    def __init__(self) -> None:
        self.root = tk.Toplevel()
        
    room_check = []
    room_checkobj = []
    room_freq = []
    value = []
    freqbox = []

    def start(self):
        self.root.title('Custom RFP Input')
        self.root.geometry(str(1000) + 'x' + str(400))
        Room_names = ['Living room', 'Master room', 'Kitchen ', 'Bathroom', 'Dining room', 'Child room', 'Study room', 'Second room', 'Guest room', 'Balcony', 'Entrance', 'Storage']
        # mp = {}
        for i in range(0,12):
            CustomRFPPopup.room_checkobj.append(tk.IntVar())
            CustomRFPPopup.room_freq.append(tk.IntVar())
            # mp[CustomRFPPopup.room_checkobj[i]] = i
        checkList = []
        self.room_freq = []
        



        for i in range(0,12):
            label = tk.Label(self.root,text= Room_names[i])
            label.grid(row = i, column= 0)
            self.freqbox.append(tk.Entry(self.root, textvariable= CustomRFPPopup.room_freq[i] ))
            self.freqbox[i].grid(row = i, column = 2)
            checkList.append(tk.Checkbutton(self.root, variable = CustomRFPPopup.room_checkobj[i],onvalue = 1, offvalue = 0))
            checkList[i].grid(row=i, column= 1)


        button = tk.Button(self.root, text='Submit', padx=5, command=lambda:CustomRFPPopup.Submit_clicked(self))      
        button.grid()
        self.root.wait_window(self.root)
    
    def checked(self, i):
        CustomRFPPopup.room_freq[i].set(1)
    
    def Submit_clicked(self):
        for i in range(0,12):
            if CustomRFPPopup.room_checkobj[i].get() == 0:
               CustomRFPPopup.room_check.append(0)
            else:
                CustomRFPPopup.room_check.append(max(1,CustomRFPPopup.room_freq[i].get()))

        self.root.destroy()
        print("room_check",self.room_check)
        params = [] 
        itr = 0
        for freq in self.room_check:
            x = freq
            if(x > 0):
                while(x > 0):
                    params.append(itr)
                    x-=1
            itr+=1


        n, redge = RFPsearch.search(params)
        # outputgraph = redge[1]
        #print("\n###The no. of matched graphs are", len(params))
        self.multi = MultiGraphCustomGUI.MultiGraph()
        outputgraph, graph_values, positions = self.multi.start(redge)

        print("inside custom output")
        CustomRFPPopup.value.append(n)

        CustomRFPPopup.value.append(outputgraph)
        CustomRFPPopup.value.append(graph_values)
        CustomRFPPopup.value.append(positions)
        print("self.multi.final_graph_names",graph_values)
        # CustomRFPPopup.value.append(self.multi.final_graph)
        print("graph added")
        # print(self.multi.final_graph.edges())


def plot(l):
    g = nx.Graph()
    g.add_edges_from(l)
    nx.draw(g)
    plt.show()
        

        




        

        



# if __name__ == '__main__':
# 	app = App()