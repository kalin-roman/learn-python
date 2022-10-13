from tkinter.tix import Tree
import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project",2000, 1000)
def house():
    back1 = gr.Rectangle(gr.Point(0, 500), gr.Point(2000,0))
    back1.setFill('blue')
    back2 = gr.Rectangle(gr.Point(0, 500), gr.Point(2000,1000))
    back2.setFill('gray')

    roof = gr.Polygon(gr.Point(100,400), gr.Point(300,100),gr.Point(400,400))
    roof.setWidth(10)
    roof.setFill("brown")

    wall = gr.Rectangle(gr.Point(100,400), gr.Point(400,800))
    wall.setWidth(10)
    wall.setFill('grey')

    window_in = gr.Rectangle(gr.Point(120, 700), gr.Point(380,500))
    window_in.setWidth(10)
    window_in.setFill('yellow')

    window_line = gr.Line(gr.Point(250, 700), gr.Point(250,500))
    window_line.setWidth(10)

    window_line2 = gr.Line(gr.Point(120, 600), gr.Point(380,600))
    window_line2.setWidth(10)
    back1.draw(window)
    back2.draw(window)
    roof.draw(window)
    wall.draw(window) 
    window_in.draw(window)
    window_line.draw(window)
    window_line2.draw(window)
def sun(x,y):
    sun = gr.Circle(gr.Point(x, y), 100)
    sun.setWidth(1)
    sun.setFill("yellow")
    sun.draw(window)
def cloud(x,y):
    cloud = gr.Circle(gr.Point(x,y), 20)
    cloud.setFill("white")
    cloud2 = gr.Circle(gr.Point(x + 20,y), 20)
    cloud2.setFill("white")
    cloud3 = gr.Circle(gr.Point(x + 40,y), 20)
    cloud3.setFill("white")


    up_cloud = gr.Circle(gr.Point(x + 30,y - 20), 20)
    up_cloud.setFill("white")
    up_cloud2 = gr.Circle(gr.Point(x + 10,y - 20), 20)
    up_cloud2.setFill("white")


    cloud.draw(window)
    up_cloud2.draw(window)
    cloud2.draw(window)
    up_cloud.draw(window)
    cloud3.draw(window)

def tree ():
    treeLeaf = gr.Polygon(gr.Point(1400,650),gr.Point(1500,550),gr.Point(1600,650))
    treeLeaf.setWidth(5)
    treeLeaf.setFill("green")
    treeLeaf2 = gr.Polygon(gr.Point(1400,600),gr.Point(1500,500),gr.Point(1600,600))
    treeLeaf2.setWidth(5)
    treeLeaf2.setFill("green")
    treeLeaf3 = gr.Polygon(gr.Point(1400,550),gr.Point(1500,450),gr.Point(1600,550))
    treeLeaf3.setWidth(5)
    treeLeaf3.setFill("green")
    stick = gr.Rectangle(gr.Point(1500,650), gr.Point(1510,700))
    stick.setWidth(5)
    stick.setFill("brown")

    treeLeaf.draw(window)
    treeLeaf2.draw(window)
    treeLeaf3.draw(window)
    stick.draw(window)


house()
tree ()
sun(1500,200)
cloud(1500,300)
cloud(1300,200)
cloud(1200,400)
window.getMouse()

window.close()

