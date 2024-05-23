from tkinter import *
from math import sqrt


root = Tk()
content = Frame(root)
w = 1000
h = 1000

root.title("Graphes")


class Graph:
    def __init__(self, list_adjacence: list, n: int):
        self.__nb_vertex = n
        self.__list_adjacence = list_adjacence
        self.__pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
        self.__col = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
        self.__col_index = [i for i in range(self.__nb_vertex)]
        self.__appel = []


    def draw(self,can):
        can.create_rectangle(0, 0, w, h, fill="white")
        for i in range(self.__nb_vertex):
            for j in self.__list_adjacence[i]:
                can.create_line(self.__pos[i][0], self.__pos[i][1], self.__pos[j][0], self.__pos[j][1])
        for k in range(self.__nb_vertex):
            col = self.__col[self.__col_index[k]]
            can.create_oval(self.__pos[k][0] - 8, self.__pos[k][1] - 8, self.__pos[k][0] + 8, self.__pos[k][1] + 8, fill=col)
            can.create_text(self.__pos[k][0], self.__pos[k][1], text=f"{k}", font=("Times", 10, "bold"), fill="black")


	def min_local(self, i):
		" self.__appel permet de mémoriser les sommets déjà traiter. "
		if i not in self.__appel:
			self.__appel.append(i)
		min = self.__col_index[i]
		sommets = self.__list_adjacence[i]
		for s in sommets:
			if min > self.__col_index[s]:
				min = self.__col_index[s]
        self.__col_index[i] = min
		for s in sommets:
			self.__col_index[s] = self.__col_index[i]
			if s not in self.__appel:
				self.min_local(s)


    def composantes_connexes(self):
        " On applique la fonction min_local à tous les sommets. "
        for i in range(self.__nb_vertex):
            self.min_local(i)












# Graphe 1
g1 = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
g = Graph(g1, 12)


# Création de la fenêtre
can = Canvas(content, width=w, height=h, bg="white")
content.grid(row=0, column=0)
can.grid(row=0, column=0)

# Exercice 2
g.composantes_connexes()
g.draw(can)


root.mainloop()