"""Main program file of the project.


"""
import warnings
import gui
import drawing as draw
import requests
origin = 0
base_url = 'https://gplan-api.herokuapp.com/'
colors = ['#4BC0D9']*100
def run():
    """Runs the GPLAN program

    Args:
        None

    Returns:
        void

    """
    def printe(string):
        """Prints string on the console

        Args:
            string
            
        Returns:
            void

        """
        gclass.textbox.insert('end',string)
        gclass.textbox.insert('end',"\n")

    warnings.filterwarnings("ignore") #Remove warnings that appear on the terminal
    gclass = gui.gui_class() 
    

    # print("elines",type(gclass.app.elines[0][0]))
    # print("connectivity", gclass.app.connectivity)
    print("hello, we have got the value", gclass.value)
    while (gclass.command!="end"):
        if(gclass.command=="dissection"):
            make_dissection_corridor(gclass)
        if ( gclass.command =="checker"):
            print("Checker called")
            #tests.tester(gclass.value,gclass.textbox)
        else:
            if (gclass.command == "circulation"):
                gclass.pen.ht()
            elif(gclass.command == "single" or gclass.command == "custom"):
                dimensioned = gclass.value[4]
                if(dimensioned == 0):
                    data = {'nodecount': gclass.value[0],
								'edgecount': gclass.value[1],
								'edgeset': list(gclass.value[2]),
								'node_coordinates': gclass.value[7]}
                    print(data)
                    r = requests.get(base_url + 'generatefp/nondim',json = data)
                    print(r)
                    if(r.status_code != 200):
                        print("The api returned error code " + str(r.status_code) + ".Contact developer for further information.")
                    else:
                        print(r.json())
                        printe("Time taken: " + r.json()['time'])
                        draw.draw_rdg(r.json()['floorplans'][0]
							,1
							,gclass.pen
							,1
							,gclass.value[6]
							,gclass.value[5]
							,origin)
                    # G.create_single_dual(1,gclass.pen,gclass.textbox)
                    # draw.draw_rdg(G,1,gclass.pen,G.to_be_merged_vertices,G.rdg_vertices,1,gclass.value[6],[])
                # else:
                #     G.width_min,G.width_max,G.height_min,G.height_max = dimgui.gui_fnc(G.node_count)
                #     G.create_single_floorplan(gclass.pen,gclass.textbox,0)
                #     draw.draw_rdg(G,1,gclass.pen,G.to_be_merged_vertices,G.rdg_vertices,0,gclass.value[6],gclass.value[5])
        # gclass.ptpg = G
        gclass.root.wait_variable(gclass.end)
        # gclass.json_data = G.return_data()
        gclass.graph_ret()
        gclass.ocan.add_tab()

        # gclass.ocan.tscreen.resetscreen()
        gclass.pen = gclass.ocan.getpen()
        gclass.pen.speed(100000)

if __name__ == "__main__":
    run()