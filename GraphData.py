'''
Created on Jan 9, 2016

@author: Hanna
'''

import tkinter


class Graph():
    #inits graph data to appropriate variables and creates a tkinter root window and canvas for drawing a graph
    def __init__(self, afile : str):
        self.x_axis = "Emote Names"
        self.y_axis = "Frequency"
        self.cwidth = 1200
        self.cheight = 700
        
        self.root = tkinter.Tk()
        self.root.title("Graph Data")
     
        self.canvas = tkinter.Canvas(self.root, width = self.cwidth, height = self.cheight)
        self.canvas.pack(fill="both", expand=True)
        
        file = open(afile, 'r')
        data = file.readlines()
        self.graph_title = data[0].rstrip('\n')
        
        self.data_collection = {}
        for i in range(1, len(data)):
            data_tup = data[i].rstrip('\n').split(" ")
            self.data_collection[data_tup[0]] = data_tup[1]
        
        self.max_val = 0
        for i in self.data_collection.values():
            if int(i) > self.max_val:
                self.max_val = int(i)
        self.len = len(self.data_collection)
        
    #creates a bar graph in a tkinter canvas window
    def bar_graph(self):
        graph_width = self.cwidth - 50
        graph_height = self.cheight - 75
        
        self.canvas.create_text(self.cwidth/2, 50, text=self.graph_title, fill="black")
        self.canvas.create_line(50, graph_height, graph_width, graph_height)
        
        bar_width = graph_width/self.len
        xpad = 50
        x = 1
        ypad = 75
        
        for i in self.data_collection:
            x0 = bar_width * x - xpad
            y0 = graph_height - ((int(self.data_collection[i])/int(self.max_val)) * graph_height)
            if(y0 + ypad <= graph_height):
                y0 += ypad
            x1 = x0 + bar_width - xpad
            y1 = graph_height
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')
            self.canvas.create_text(x0+2, y0, anchor=tkinter.SW, text=self.data_collection[i])
            self.canvas.create_text(x0+2, y1+25, anchor=tkinter.SW, text=i)
            
            x += 1
            
        
        
        
if __name__ == '__main__':
    Graph1 = Graph('EmoteData')        
    Graph1.bar_graph()
    Graph1.root.mainloop()

    
    