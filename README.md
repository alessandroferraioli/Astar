# A* Pathfinding

It is an implementation of A* algorithm.

## Usage

```bash
python main.py
```
The first screen allows you to create the walls inside the map by clicking on a cell with the left button of the mouse.
Then clicking on the (x) or pressing (esc) it will be run the alghoritm on the created map.
## Parameters

Inside the main is it possible to change some parameters of the program. Especially : 

```python
row = 10
col = 10
width = 800
height = 800
delay = 100
```
where the row and col represet the number of cells for each row and each column. The parameters width and height represent the size of the canvas. The delay parameter represents the frequency of update of the GUI. \n
The alghoritm is implemented using the library Tkinter which manages the GUI. G
