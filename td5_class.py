# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:11:50 2024

@author: taoua
"""

from tkinter import *
from random import randint 
from math import sqrt

root = Tk()

content = Frame(root)

w = 400
h = 400

can = Canvas(content,width = w,height = h, bg ='red')
content.grid(row = 0, column = 0)
can.grid(row = 0, column = 0)
root.title("Tir à l'arc")

def distance(x,y):
	return x*x + y*y





class Tir_a_larc:
    def __init__(self, centre, rayon):
        self.__rayon = rayon
        self.__centre = centre
        self.__score = 0
        self.__nb_shoot = 0
        self.__position_tir = []
    
    def score(self, x, y):
	    r = 10
	    for k in range(6):
		    r += self.__rayon
		    d = distance(self.__centre-x, self.__centre-y)
		    if d <= r**2 and d >= (r-self.__rayon)**2:
			    self.__score += 6-k
        
    def draw_score(self):
	    if self.__score <= 1:
		    display_score.config(text=f"Score : {self.__score} point")
	    else:
		    display_score.config(text=f"Score : {self.__score} points")
            
    def draw_shoots(self):
	    for (x,y) in self.__position_tir:
		    can.create_oval(x-5,y-5,x+5,y+5, outline="black", fill="black")
            
    def draw_circle(self,r, color1, color2):
	    can.create_oval(self.__centre-r, self.__centre-r, self.__centre+r, self.__centre+r, outline=color1, fill=color2, width=1)

    def draw_cible(self):
	    r = self.__centre - 10
	    for k in range(4):
		    self.draw_circle(r, "red", "white")
		    r -= self.__rayon
	    self.draw_circle(r, "white", "red")
	    r -= self.__rayon
	    self.draw_circle(r, "red", "white")

    def draw_text(self):
	    r = self.__rayon
	    for k in range(1,7,1):
		    if k != 5:
			    can.create_text(self.__centre,r, text=f"{k}", font=("Times","20"),fill="red")
		    else:
			    can.create_text(self.__centre,r,text=f"{k}", font=("Times", "20"), fill="ivory")
		    r += self.__rayon
    
    def draw_lines(self):
        can.create_line(0, 200, 400, 200, fill='red')
        can.create_line(200, 0, 200, 400, fill='red')
        
    def tir(self):
	    feu["state"] = DISABLED
	    for k in range(5-self.__nb_shoot):
		    x = randint(0,2*self.__centre)
		    y = randint(0,2*self.__centre)
		    self.score(x,y)
		    self.__nb_shoot += 1
		    self.__position_tir.append((x,y))
	    self.draw_score()
	    self.draw_shoots()
    
    def shoot(self, *args):
        if self.__nb_shoot < 5 :
            self.__nb_shoot += 1
            x = randint(0,2*self.__centre)
            y = randint(0,2*self.__centre)
            self.score(x,y)
            self.__position_tir.append((x,y))
            self.draw_score()
            self.draw_shoots()
        

            
#Exercice 1
jeu = Tir_a_larc(200,30)
jeu.draw_cible()
jeu.draw_text()
jeu.draw_lines()

feu = Button(content, text = "Feu !",command = jeu.tir)
feu.grid(row = 1, column = 0, sticky = W)
quitter = Button(content, text="Quitter", command = content.destroy)
quitter.grid(row = 1, column = 0,sticky = E)
            


#Exercice 2 
display_score = Label(content, text=f"Score : 0 Point")
display_score.grid(row = 1, column = 0)


#Exercice 3
root.bind("<f>", jeu.shoot)



root.mainloop()


        
        
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        