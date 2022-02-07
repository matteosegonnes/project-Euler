from main_fct import *

#cf theorie mathématiques sur equation pell-fermat wikipedia
# x^2 - D y^2 = 1

def reduite(liste):
    if len(liste)%2 == 0 :
        return(liste[:-1])
    else :
        V = liste + liste
        return(V[:-1])

xmax = 0
Dmax = 0
for D in range(2,1001) :
    if sqrt(D) != int(sqrt(D)):

        liste = period_square_roots(D)
        L = [liste[0]] + reduite(liste[1])
        frac = expansion(L)
        x,y = frac.denominator , frac.numerator
        if x > xmax :
            xmax = x
            Dmax = D

print(Dmax)


'''Trouver les premieres solutions de E '''

def premier_couple_pell_fermat(D):
    #x,y
    if sqrt(D) == int(sqrt(D)):
        return(None)
    else :
        liste = period_square_roots(D)
        L = [liste[0]] + reduite(liste[1])
        frac = expansion(L)
        return(frac.denominator , frac.numerator)
