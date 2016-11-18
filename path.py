import random
from Tkinter import *
import node

nodes = []

choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

final = {'A':[],
         'B':[],
         'C':[],
         'D':[],
         'E':[],
         'F':[],
         'G': [],
         'H': [],
         'I': [],
         'J': [],
         'K': []}

master = Tk()
w = Canvas(master, width=1000, height=800)
tvar = StringVar(master)
fvar = StringVar(master)

def generateMap():
    random.seed()
    global final
    for i, a in final.items():
        r = random.randint(1, 7)
        for m in range(r):
            c = choices[random.randint(0, len(choices)-1)]
            if(c in a or c == i):
                continue
            else:
                a.append(c)

def main():
    generateMap()
    w.pack()
    for i, a in final.items():
        x1 = random.randint(20, 990)
        y1 = random.randint(50, 790)
        id = w.create_rectangle(x1,y1, x1+30, y1+30)
        w.create_text(x1+15, y1+15, text=i)
        n = node.node(id, (x1, y1), (x1+30, y1+30), i, a)
        nodes.append(n)
    drawLines()
    tvar.set("A")
    tmenu = OptionMenu(master, tvar, *choices)
    fvar.set("B")
    fmenu = OptionMenu(master, fvar, *choices)
    button = Button(master, text="Go", command=clickGo)
    tmenu.place(relx=.05, rely=.03)
    fmenu.place(relx=.12, rely=.03)
    button.place(relx=.2, rely=.03)
    mainloop()

def clickGo():
    to = tvar.get()
    fr = fvar.get()
    n1 = searchNodes(to)
    n2 = searchNodes(fr)
    print(w.coords(n1.pointsTo[0][1]))

def searchNodes(name):
    global nodes
    for n in nodes:
        if name == n.name:
            return n

def drawLines():
    global nodes
    for n in nodes:
        lines = []
        for a in n.pointsTo:
            pnode = searchNodes(a)
            id = w.create_line((n.p1[0])+15, (n.p1[1])+15, (pnode.p1[0])+15, (pnode.p1[1])+15, width=2)
            lines.append(id)
        n.addLines(lines)
    for n in nodes:
        print(n.pointsTo)

main()














