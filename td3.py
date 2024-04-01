import unittest

#EXERCICE 1
#Créer l'arbre, changer la valeur de n'importe quel élément de l'arbre ou même la supprimer, voir si un élément est une feuille ou non, voir les enfants d'un élément

#EXERCICE 2

class Tree:
    def __init__(self, label, *children):
        self.gosse = children #tuple
        self.name = label
    def label(self):
        return self.name
    def children(self):
        return self.gosse #tuple et non pas arbre
    def nb_children(self):
        return len(self.gosse)
    def is_leaf(self):
        if len(self.gosse)==0:
            return True
        return False
    def child(self, i:int):
        if len(self.gosse)>i:
            return self.gosse[i]
        return
    def depth(self):
        if self.is_leaf():  #Cas d'arrêt
            return 0

        else :
            t = self.child(0)
            maxi =  t.depth()
            for i in range(self.nb_children()):
                t= self.child(i)
                if t.depth() > maxi:
                    maxi =  t.depth()
            return 1+ maxi
    def __str__(self):  #pour l'afficher en str
        if self.is_leaf():
            return f'{self.label()}'
        else:
            print(self.nb_children())
            ret = ''
            for i in range(self.nb_children()):
                t = self.child(i)
                ret = ret + ',' + t.__str__()
        return f'{self.label()}' + f'({ret[1:]})'
    def __eq__(self, __value:object): #Pour comparer les valeurs ('==')
        if self.__str__() == __value.__str__():
            return True
        return False
    def deriv(self, var: str):
        # On part du principe que on peut n'avoir que des produits à l'avant dernière ligne (on linéarise l'expression) TOUT ARBRE EST ALORS DE PROFONDEUR 3 (sauf polynome constant) avec un '+' ligne 1,
        #puis des signes produits à la ligne 2 et des constantes / signe produit pour la puissance de X à la ligne 3 (par exemple : 3X^2 + 4X + 2 == (3 * (X * X)) + (4*X) + (2) ) et des X à la ligne 4
        #on )
        #On veut ainsi une écriture du type +(*(c1),  *(c2,X), *(c3,*(X,X))) pour un polynome de la forme c1 + c2 X + c3 X**2
        #J'ai conscience que cela rajoute beaucoup de conditions, j'ai eu du mal à trouver comment bien écrire le polynome et je pense qu'il y a une méthode plus efficace
        #Car ce que ma fonction return est assez pesant, mais techniquement le calcul fonctionne malgré toutes les contraintes
        n = self.nb_children()
        L = []
        M = []
        for i in range(n):
            t = self.child(i)
            #Alors d'après mon écriture, il y a deux children (un * qui a la puissance de X children (qui sont tous des X) et une constante)
            if t.child(0) != '*':#alors c'est la constante en child(0)
                t2 = t.child(1)
                c = t.child(0)
                k = t2.nb_children() #la puissance de t2
                if k == 0: #Cas de X puissance 0
                    M = ['*', 0]
                elif k == 1:
                    print(c)
                    M = [ '*', f'{c}' ]

                else:
                    M = ['*', f'{c}*{k}'] #On multiplie par k la constante
                    N = []
                    for i in range(k-1):
                        N.append(var) #On ajoute X k-1 fois
                    M.append(N)
            else: #la puissance de X en child(0)
                t2 = t.child(0)
                c = t.child(1)
                k = t2.nb_children() #la puissance de t2
                if k == 0: #Cas de X puissance 0
                    M = ['*', 0]
                elif k == 1:
                    M = [ '*', f'{c}' ]

                else:
                    M = ['*', f'{c}*{k}'] #On multiplie par k la constante
                    N = []
                    for i in range(k-1):
                        N.append(var) #On ajoute X k-1 fois
                    M.append(N)
            print(M)
            L.append(M)


        return Tree('+', L)





class TestTree(unittest.TestCase):

    def test_label(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.label(), 'f')
    def test_children(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.children(), ('g','k'))
    def test_nb_children(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.nb_children(), 2)
    def test_is_leaf(self):
        t= Tree('f', Tree('g'), Tree('k'))
        t2= Tree('f')
        self.assertEqual(t.is_leaf(), False)
        self.assertEqual(t2.is_leaf(), True)
    def test_child(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.child(1), 'k')
        self.assertEqual(t.child(0), 'g')






if __name__ == '__main__':
    t1 = Tree('f', Tree('2',Tree('4')), Tree('3'))
    t2 = Tree('f', Tree('2',Tree('4')), Tree('3'))
    t3 = Tree('f', Tree('2',Tree('6')), Tree('3'))
    tPoly = Tree('+', Tree('*', Tree('5'),Tree('*', 'X', 'X')), Tree('*',Tree('a'),Tree('*','X'))) #Ceci est le polynome 5X^2 + aX
    tPoly2 = Tree('+', Tree('*', Tree('5'),Tree('*', 'X', 'X')), Tree('*',Tree('a'),Tree('*'))) #Ceci est le polynome 5X^2 + a
    tPoly3 = Tree('+', Tree('*', Tree('1'),Tree('*', 'X', 'X','X','X')), Tree('*',Tree('a'),Tree('*','X','X'))) #Ceci est le polynome X^4 + aX^2
    #print(t1.label())
    #print(t1.children())
    #print(t1.nb_children())
    #print(t1.child(0))
    #print( t1.is_leaf())
    #print(t1.depth())
    print(t1 == t2)
    print(t1 == t3)
    print(tPoly.deriv('X'))
    print(tPoly2.deriv('X'))
    print(tPoly3.deriv('X'))
    unittest.main()


