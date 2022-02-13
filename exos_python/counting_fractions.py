from main_fct import *
from fractions import Fraction


# n/d avec n<d   n = 1 * p1^a1 p2^a2...pn^an   pi > 1
# Farey sequence

# trouver c/d < a/b   le plus pres possible
# IDEE : c/d < a/b ssi ad - bc > 0 SSI (intuition + demontre sur wiwi) ad - bc = 1
# de plus si c/d solution, avec bezout, c+ak/d+bk solution aussi et biensur, c+ak/d+bk > c/d
#Ainsi, on a ad-bc = 1 avec d le plus grand possible !!

# donc plus grand d tel que ad = 1 [b] et donc on trouve d en maximum b tests
# puis c = (ad-1)/b    CQFD donc algo en O(1) !!!! 

crible = crible_eratos(1000001)

def find_predecessor_Farey(a,b,Denominateur_max) :

    # C = O(1)
    #looking for c,d such as c/d < a/b
    for k in range(Denominateur_max,0,-1):  # b test vont suffirent cf modulo [b]
        if (a*k)%b == 1 :
            return((a*k - 1)//b , k)

# donc find_predecessor_Farey(3,7,1000000)[0] répond au probleme d'avant


def phi(n,crible) :

    if crible[n-2] :
        return(n-1)

    else :
        p = 1
        for k in range(int(sqrt(n)) -1) :

            u = k + 2

            if n%u == 0 :
                if crible[k] :
                    p = p * (1 - Fraction(1,u))

                a = n//u

                if crible[a - 2] and u != a :
                    p = p * (1 - Fraction(1,a))
    return(n*p)


N = 0
for i in range(2,1000001) :

    N+= phi(i,crible)

print(N)
