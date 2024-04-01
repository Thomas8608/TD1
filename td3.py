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
    #print(t1.label())
    #print(t1.children())
    #print(t1.nb_children())
    #print(t1.child(0))
    #print( t1.is_leaf())
    #print(t1.depth())
    print(t1 == t2)
    print(t1 == t3)
    unittest.main()


