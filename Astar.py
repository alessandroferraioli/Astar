from Tkinter import *
import time 
import numpy as  np
import math 
import random

#============================================================================================
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 0
        self.g = 0
        self.f = 0
        self.isWall = False
        self.inCloseSet = False
        self.inOpenSet = False
        self.closeNodes = []
        self.path = []
        self.parent = None
        if(random.uniform(0,1)<0.2):
            self.isWall = True




#--------------------------------------------------------------------------------
    def addCloseNodes(self,grid,w,h):
        x = self.x
        y = self.y
        
        #Right
        if(x+1<w):
            self.closeNodes.append(grid[x+1][y])
        #Left
        if(x-1>=0):
            self.closeNodes.append(grid[x-1][y])
        #Top
        if(y-1>=0):
            self.closeNodes.append(grid[x][y-1])
        #Bottom
        if(y+1<h):
            self.closeNodes.append(grid[x][y+1])
        
        #Top left
        if(x-1>=0 and y-1>=0):
            self.closeNodes.append(grid[x-1][y-1])
        #Bottom right
        if(x+1<w and y+1<h):
            self.closeNodes.append(grid[x+1][y+1])
        


#============================================================================================
class Astar:
    
    def __init__(self,width,height,num_col,num_row,startNode,endNode):
        self.width = width
        self.height = height
        self.col = num_col
        self.row = num_row


        #Assuming square
        self.sizeNode = int(width/num_col)
        self.grid = np.empty([self.row,self.col], dtype=object)

        self.startNode = None 
        self.endNode = None
        
        self.path = []
        #Creating close and open sets
        self.openSet = []
        self.closeSet = []

        self.setup(startNode,endNode)
        self.rootTk = Tk()
        self.window = Canvas(self.rootTk, width=width, height=height)
        self.window.pack()
        self.rootTk.after(100,self.draw)
        self.rootTk.mainloop()

#--------------------------------------------------------------------------------
    def addOpenSet(self,node):
        self.openSet.append(node)
        node.inOpenSet = True
        node.inCloseSet = False
#--------------------------------------------------------------------------------
    def addCloseSet(self,node):
        self.closeSet.append(node)
        node.inOpenSet = False
        node.inCloseSet = True
#--------------------------------------------------------------------------------
    def evalutePath(self,node):
        del self.path[:]
        self.path.append(node)
        while(node.parent is not None):
            self.path.append(node.parent)
            node = node.parent

#--------------------------------------------------------------------------------
    def guessDistance(self,currNode):
        return math.sqrt((self.endNode.x - currNode.x )**2 + (self.endNode.y - currNode.y)**2 )

#--------------------------------------------------------------------------------
    def draw(self):
        finished =  False
        if(len(self.openSet) > 0):
            #Do something
            
            currIndex = 0
            for i in range(len(self.openSet)):
                if(self.openSet[i].f <= self.openSet[currIndex].f):
                    currIndex = i

            currNode = self.openSet[currIndex]
            if(currNode is self.endNode ):
                finished = True
                self.evalutePath(currNode)
            
            self.openSet.remove(currNode)
            self.addCloseSet(currNode)

            
            for currCloseNode in currNode.closeNodes:
                if currCloseNode in self.closeSet :
                    continue
                elif(currCloseNode.isWall is False):
                    tenative_g = currNode.g +1

                    if(currCloseNode in self.openSet ):#If I already evaluteted 
                        if(tenative_g < currCloseNode.g):
                            currCloseNode.g = tenative_g
                    else:
                        currCloseNode.g = tenative_g
                        self.addOpenSet(currCloseNode)
                        

                #Heuristic
                currCloseNode.h = self.guessDistance(currCloseNode)
                currCloseNode.f = currCloseNode.h + currCloseNode.g
                currCloseNode.parent = currNode



    
            #Redraw the grid
            for x in range(self.row):
                for  y in range(self.col):
                    top_left = [x*self.sizeNode+1,y*self.sizeNode+1]
                    bottom_right  = [x*self.sizeNode+ self.sizeNode ,y*self.sizeNode+self.sizeNode]
                    if(self.grid[x][y].isWall is True):
                        self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='black')
                    elif(self.grid[x][y].inOpenSet is True):
                        self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='green')
                    elif(self.grid[x][y].inCloseSet is True):
                        self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='red')
                    else:
                        self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='white')

            #Drawing End point
            top_left = [self.endNode.x*self.sizeNode+1,self.endNode.y*self.sizeNode+1]
            bottom_right  = [self.endNode.x*self.sizeNode+ self.sizeNode ,self.endNode.y*self.sizeNode+self.sizeNode]
            self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='blue')


            for item in self.path:
                x = item.x
                y = item.y
                top_left = [x*self.sizeNode+1,y*self.sizeNode+1]
                bottom_right  = [x*self.sizeNode+ self.sizeNode ,y*self.sizeNode+self.sizeNode]
                self.window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='yellow')

            if(finished is not True):
                self.rootTk.after(100,self.draw)
            else:
                print("Finished!")    
        else:
            print("Solution does not exist!")

#--------------------------------------------------------------------------------
    def setup(self,startNode,endNode):
        for x in range(self.row):
            for y in range(self.col):
                self.grid[x][y] = Node(x,y)
                if(x == startNode[0] and y == startNode[1]):
                    self.startNode = self.grid[x][y]
                elif(x == endNode[0] and y == endNode[1]):
                    self.endNode = self.grid[x][y]

        #Setting close nodes
        for x in range(self.row):
            for y in range(self.col):
                self.grid[x][y].addCloseNodes(self.grid,self.row,self.col)


        self.openSet.append(self.startNode)
        
       # print self.grid


