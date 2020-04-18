from Astar import *
width = 600
height = 600


def draw(size_rec,w,root):
    for x in range(size_rec/2,width,size_rec):
        for y in range(size_rec/2,height,size_rec):
            top_left = [x-size_rec/2,y-size_rec/2]
            bottom_right  = [x+size_rec/2,y+size_rec/2]
            w.create_rectangle(top_left[0],top_left[1],bottom_right[0],bottom_right[1], fill='white')
    root.after(100,draw,size_rec+1,w,root)


#===================================================================================
def main():
    alg = Astar(600,600,10,10,[0,0],[10,10])
    
#===================================================================================
if __name__ == '__main__':
	main()
