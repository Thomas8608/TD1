





class Polynom:
    def __init__(self,coefs,q,n):
        self.__coefs = coefs
        self.__q = q
        self.__n = n
        " Dans Z_q[x]/(x^n+1)Z_q[x] les polynômes ne peuvent être de degré supérieur à (n - 1) "
        assert(len(self.__coefs) == n)
        for i in range(n):
            assert(self.__coefs[i] >= 0)
            assert(self.__coefs[i] < q)

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.__coefs):
            if coef != 0:
                terms.append(f"{coef}*x^{i}" if i > 0 else f"{coef}")
        return " + ".join(terms) if terms else "0"


    def __add__(self,other):
        assert(self.__n == other.__n)
        assert( self.__q == other.__q)
        S_coefs = [0 for _ in range(self.__n)]
        """ Les degrés ne dépasseront pas les conditions mais

        les coefficients ne seront plus forcément modulo q """
        for i in range(self.__n):
            S_coefs[i] = (self.__coefs[i] + other.__coefs[i]) % self.__q
        return Polynom(S_coefs, self.__q, self.__n)

    def scalar(self,c):
        S_coefs = [0 for _ in range(self.__n)]
        for i in range(self.__n):
            S_coefs[i] = (c * self.__coefs[i]) % self.__q
        return Polynom(S_coefs, self.__q, self.__n)

    def __mul__(self,other):
        assert(self.__n == other.__n)
        assert( self.__q == other.__q)
        S_coefs = [0] * self.__n
        for i in range(self.__n):
            for j in range(self.__n):
                k = (i + j) % self.__n
                S_coefs[k] = (S_coefs[k] + self.__coefs[i] * other.__coefs[j]) % self.__q
                if i + j >= self.__n:
                    S_coefs[k] = (S_coefs[k] - self.__coefs[i] * other.__coefs[j]) % self.__q
        return Polynom(S_coefs, self.__q, self.__n)

    def rescale(self,r):
        """
        Pour que le polynôme soit dans Z_r[x]/(x^n+1)Z_r[x] en partant d'un polynôme dans
        Z_q[x]/(x^n+1)Z_q[x], il suffit de mettre les coefficients du polynôme modulo r
        """
        S_coefs = [coef % r for coef in self.__coefs]
        return Polynom(S_coefs, r, self.__n)

    def fscalar(self,r,alpha):
        """
        Le polynôme Q sera du même degré que le polynôme P
        """
        S_coefs = [(int(alpha * coef) % r) for coef in self.__coefs]
        return Polynom(S_coefs, r, self.__n)





P1 = Polynom([1,2,2,1,4],6,5)
P2 = Polynom([2,1,5,2,4],6,5)

# Produit de deux polynômes


Prod = P1 * P2
print("P1 x P2 =", Prod)

# Somme de deux polynômes

Som = P1 + P2
print("P1 + P2 = ",Som)


# Création des polynômes
p = Polynom([1, 2, 3], q=5, n=3)


# Multiplication par un scalaire
p_scalar = p.scalar(3)
print("Multiplication de p par 3:", p_scalar)

# Changement de l'échelle à Z_7
p_rescale = p.rescale(7)
print("Rescale de p à Z_7:", p_rescale)

# Transformation avec une fonction scalaire, alpha=2.5 et r=7
p_fscalar = p.fscalar(7, 2.5)
print("Transformation de p avec alpha=2.5 et r=7:", p_fscalar)

















