from Astar import *

row = 20
col = 30
width = 800
height = 800
delay = 100

sizeSquare = min(width/col,height/row)
grid  = np.ones([row,col]) 

root = Tk()
#===================================================================================
def callback(event):
    clickX = event.x
    clickY = event.y
    grid[ int(event.y/sizeSquare)][int(event.x/sizeSquare)] = grid[ int(event.y/sizeSquare)][int(event.x/sizeSquare)] * -1
#===================================================================================
def exit(e):
    root.destroy()
#===================================================================================
def createWalls(window,root):
    for x in range(row):
        for  y in range(col):
            top_left = [x*sizeSquare+1,y*sizeSquare+1]
            bottom_right  = [x*sizeSquare+ sizeSquare ,y*sizeSquare+sizeSquare]
            if(grid[x][y] == 1):
                window.create_rectangle(top_left[1],top_left[0],bottom_right[1],bottom_right[0], fill='white')
            else:
                window.create_rectangle(top_left[1],top_left[0],bottom_right[1],bottom_right[0], fill='blue')
    root.after(100,createWalls,window,root)
#===================================================================================
def main():

    root.bind("<Button-1>", callback)
    root.bind("<Escape>", exit)
    window = Canvas(root, width=width, height=height)
    window.pack()
    root.after(100,createWalls,window,root)
    root.mainloop()
    print (grid.shape)
    alg = Astar(width,height,row,col,[0,0],[row-1,col-1],delay,grid)
    
#===================================================================================
if __name__ == '__main__':
	main()
