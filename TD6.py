# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:54:58 2024

@author: taoua
"""

from tkinter import *
import numpy as np
from math import sqrt
from random import randint, random

root = Tk()
content = Frame(root)
w = 700
h = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - w) // 2 
y = (screen_height - h) // 2
root.title("Graphes")
root.geometry(f"{w}x{h}+{x}+{y}")
root.resizable(width=False, height=False)

class Graph:
    def __init__(self, list_adjacence: list, n: int):
        self.__tau = 0.1
        self.__k = 1
        self.__r0 = 100
        self.__nb_vertex = n 
        self.__list_adjacence = list(list_adjacence)
        self.__pos = np.array([[w // 2 + randint(-100, 100), h // 2 + randint(-100, 100)] for _ in range(self.__nb_vertex)])
        self.__vit = np.array([[(random() - 0.5) * 10, (random() - 0.5) * 10] for _ in range(self.__nb_vertex)])
    
    def draw(self):
        can.create_rectangle(0, 0, w, h, fill="white")
        for i in range(self.__nb_vertex):
            for j in self.__list_adjacence[i]: 
                can.create_line(self.__pos[i][0], self.__pos[i][1], self.__pos[j][0], self.__pos[j][1])
        for k in range(self.__nb_vertex):
            can.create_oval(self.__pos[k][0] - 8, self.__pos[k][1] - 8, self.__pos[k][0] + 8, self.__pos[k][1] + 8, fill="#f3e1d4")
            can.create_text(self.__pos[k][0], self.__pos[k][1], text=f"{k}", font=("Times", 10, "bold"), fill="black")

    def ressort(self, event=None):
        forces = np.zeros_like(self.__pos)
        for i in range(self.__nb_vertex):
            for j in self.__list_adjacence[i]:
                if i != j:
                    delta = self.__pos[i] - self.__pos[j]
                    r = np.linalg.norm(delta)
                    if r > 0:
                        f = self.__k * (r - self.__r0) * (delta / r)
                        forces[i] -= f
                        forces[j] += f
        self.__vit += forces * self.__tau
        self.__pos += self.__vit * self.__tau
        self.draw()

g1 = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
      [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
g = Graph(g1, 11)

can = Canvas(content, width=w, height=h, bg="white")
content.grid(row=0, column=0)
can.grid(row=0, column=0)
g.draw()
root.bind('<f>', g.ressort)
root.mainloop()
