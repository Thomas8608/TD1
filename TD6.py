# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:54:58 2024

@author: taoua
"""

from tkinter import *
from random import randint
from random import random
import numpy as np


l0 = 1
k = 1
tau = 0.1

root = Tk()

content = Frame(root)


w = 400
h = 400

can = Canvas(content,width = w,height = h, bg ='white')
content.grid(row = 0, column = 0)
can.grid(row = 0, column = 0)
root.title("Graphe")

graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]


pos = np.array([(randint(0,w),randint(0,h))
       for i in range(len(graph))])



def draw(can, graph, pos):
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(len(pos)):
        x,y = pos[i][0], pos[i][1]
        can.create_oval(x-10,y-10,x+10,y+10,fill="#f3e1d4")
        can.create_text(x,y,text=f"{i}", font=("Times","8"),fill="black")
        
draw(can,graph,pos)

vit = np.array([((random()-0.5)*10, (random()-0.5)*10)
       for i in range(len(graph))])

            
def dist(graph,pos):
    distance = []
    for i in range(len(graph)):
        L1 = []
        for j in graph[i]:
            m = (pos[j][1] - pos[i][1])**2 + (pos[j][0] - pos[i][0])**2
            L1.append(np.sqrt(m))
        distance.append(L1)
    return distance

def force(distance,graph,pos):
    F = []
    for i in range(len(graph)):
        L1 = []
        for j in graph[i]:
            f = - k *(distance[i][j] - l0)
            L1.append(f)
        F.append(L1)
    return F
    
distance = dist(graph,pos)
F = force(distance,graph,pos)
def ressort():
    global pos  # Ajouter cette ligne pour accéder à la variable pos globale
    for i in range(len(graph)):
        for j in graph[i]:
            vit[i][j] += tau * F[i][j]
            pos[i][j] += tau * vit[i][j]
    draw(can, graph, pos)  # Mettre à jour le dessin du graphe après chaque itération
    root.after(100, ressort)  # Appeler ressort() de façon récurrente après 100 millisecondes

        
        


            


            








root.mainloop()












