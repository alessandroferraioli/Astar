from Tkinter import *
import time 
import numpy as  np
class Node:
    def __init__(self,x,y,size,isWall):
        self.x = x
        self.y = y
        self.h_cost = 0
        self.g_cost = 0
        self.isWall = isWall
        self.sizeNode = size
    def x(self):
        return self.x
    def y(self):
        return self.x


class Astar:
    
    def __init__(self,width,height,num_col,num_row,startNode,endNode):
        self.width = width
        self.height = height
        self.col = num_col
        self.row = num_row


        #Assuming square
        self.sizeNode = int(width/num_col)
        self.grid = np.empty([self.row,self.col], dtype=object)

        self.startNode = Node(startNode[0],startNode[1],self.sizeNode,False)
        self.endNode = Node(endNode[0],endNode[1],self.sizeNode,False)

        #Creating close and open sets
        self.openSet = []
        self.closeSet = []

        self.setup()
        self.rootTk = Tk()
        self.window = Canvas(self.rootTk, width=width, height=height)
        self.window.pack()
        self.rootTk.after(100,self.draw)
        self.rootTk.mainloop()


    def draw(self):
        if(len(self.openSet) > 0):
            #Do something
            



            #Redraw the grid
            for x in range(self.row):
                for  y in range(self.col):
                    top_left = [x*self.sizeNode+1,y*self.sizeNode+1]
                    bottom_right  = [x*self.sizeNode+ self.sizeNode ,y*self.sizeNode+self.sizeNode]
                    self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='white')

            for item in self.openSet:
                x = item.x
                y = item.y
                top_left = [x*self.sizeNode+1,y*self.sizeNode+1]
                bottom_right  = [x*self.sizeNode+ self.sizeNode ,y*self.sizeNode+self.sizeNode]
                self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='green')

            self.rootTk.after(100,self.draw)
        else:
            print("Finished!")


    def setup(self):
        for x in range(self.row):
            for y in range(self.col):
                self.grid[x][y] = Node(x,y,self.sizeNode,False)

        self.openSet.append(self.startNode)
        
       # print self.grid


