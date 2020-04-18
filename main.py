from Astar import *

row = 20
col = 20
width = 800
height = 800

sizeSquare = width/row

grid  = np.ones([row,col]) 


root = Tk()
#===================================================================================
def callback(event):
    clickX = event.x
    clickY = event.y
    grid[int(event.x/sizeSquare)][ int(event.y/sizeSquare)] = grid[int(event.x/sizeSquare)][ int(event.y/sizeSquare)] * -1
#===================================================================================
def exit(e):
    root.destroy()
#===================================================================================
def draw(window,root):
    for x in range(row):
        for  y in range(col):
            top_left = [x*sizeSquare+1,y*sizeSquare+1]
            bottom_right  = [x*sizeSquare+ sizeSquare ,y*sizeSquare+sizeSquare]
            if(grid[x][y] == 1):
                window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='white')
            else:
                window.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='blue')
    root.after(100,draw,window,root)
#===================================================================================
def main():

    root.bind("<Button-1>", callback)
    root.bind("<Escape>", exit)

    window = Canvas(root, width=width, height=height)
    window.pack()

    root.after(100,draw,window,root)

    root.mainloop()

    alg = Astar(width,height,row,col,[0,0],[row-1,col-1],100,grid)
    
#===================================================================================
if __name__ == '__main__':
	main()
