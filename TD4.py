# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:55:29 2024

@author: taoua
"""
import matplotlib.pyplot as plt
 
def hash_naif(key):
    return sum([ord(c) for c in key])

def hash_horner(c):
    h = 0
    for i in c : 
        h = 33*h + ord(i)
    return h 

#Exercice 2

class Hashtable:
    def __init__(self,hash_fonction,N):
        self.__hash_fonction = hash_fonction
        self.__taille = N
        self.__tableau = [[] for k in range(N)]
               

    def resize(self):

        '''redimensione la table en multipliant par deux le nombres de tiroirs'''

        self.__taille =2*self.__taille 
    
    
    def put(self,key,value):

        '''permet d'ajouter une cle et une valeure a la table'''
        c=0
        for elem in self.__tableau :
            if elem==[]:
                c+=1
        if c>0.8*self.__taille:
            self.resize
        image=self.__hash_fonction(key) % self.__taille
        yes =False
        for value in self.__tableau[image]:
            if value[0]==key:
                value=(key,value)
                yes =True
        if not yes :
            self.__tableau[image].append((key,value))

        
    

# Exercice 3

    def get(self,key):
        index = self.__hash_fonction(key) % self.__taille
        for (k,v) in self.__tableau[index]:
            if k == key :
                return v
        return None 
    
    def __str__(self):
        return str(self.__tableau)
    
#Exercice 4

    def repartition(self):

        '''trace la repartition des elements de la table en fonction des tiroirs'''

        X=[i for i in range(len(self.__tableau))]

        Y=[len(self.__tableau[j]) for j in range( len(self.__tableau))]

        plt.bar(X,Y,color="blue")

        plt.show()
        
if __name__=="__main__":
    ht=Hashtable(hash_naif,320)

    ht.put('abc',3) 

    print('test de get sur ht ='  , ht.get('abc'))
    print('_______________________')
    

def Exercice5(g,N):
    lexique = open("frenchssaccent.dic",'r')
    D = Hashtable(g,N)
    for l in lexique : 
        D.put(l[0:len(l) - 1],len(l) - 1)
    lexique.close()
    D.repartition()

    

    
    
   
    
    
# Test exercice 2         
        
D = Hashtable(hash_naif,5)
D.put('abc',3)

# Test exercice 3 
print('-----Test exercice 3')
print(D.get('abc'))
print(D.get('aaa'))

# exercice 4 
D.put('bac', 4)
D.put('cba',13)
D.put('tuv',11)
D.put('uvt',1)
D.repartition()


# Test exercice 5 
print('-----Test exercice 5')
print(Exercice5(hash_naif,300))
print(Exercice5(hash_naif,100000))
print(Exercice5(hash_horner,300))









    