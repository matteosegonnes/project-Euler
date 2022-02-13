from main_fct import *


# e = [2, 1,2,1,1,4,1,1,6 , ...]


def expansion(L) :

    if len(L) == 1:
        return(Fraction(1,L[0]))
    else :
        return(Fraction(1,L[0] + expansion(L[1:])))


V = [1,1]
L = [1]
for k in range(1,100) :
    L = L + [2*k] + V

u0 = 2

u0 += expansion(L[:99])


numerateur = '6963524437876961749120273824619538346438023188214475670667'
r = 0
for k in numerateur :
    r+=int(k)
print(r)
