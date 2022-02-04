from main_fct import*
from copy import copy




'''
REPONSE PEU OPTIMALE...

def creer_tuples(my_tuple):

    L = list(my_tuple)
    liste_tuples = []

    for k in range(len(L)):
        V = [0]*len(L)
        for j in range(len(L)):
            if k==j:
                V[j] = L[j] + 1
            else :
                V[j] = L[j]
        if k==0 :
            premier_liste_tuple = copy(V)
            tuple_v = tuple(V)
            liste_tuples+= [tuple_v]

        else :
            bool = True
            for k in liste_tuples :
                if deux_permutation(V,list(k)):
                    bool = False
                    break

            if bool :
                liste_tuples+= [tuple(V)]

    V = L + [1]
    tuple_v = tuple(V)
    liste_tuples+=[tuple_v]
    return(liste_tuples)


def update_dico(dico):

    dico_final = {}
    for k in dico.keys():

        compteur = 0

        liste = creer_tuples(k)

        for j in liste : # j : tuple à mettre en key de dico_final

            liste_j = list(j)
            if compteur == 0 :
                dico_final[j] = 1
                compteur +=1
            else :
                dico_copy = copy(dico_final)
                for keys in dico_copy.keys():
                    if not deux_permutation(list(keys), liste_j) :
                        dico_final[j] = 1

    return(dico_final)


def p(n):
    dico = {(1,) : 1}
    for k in range(n-1):
        dico = update_dico(dico)
    return(len(dico))


n = 1
p = 1
dico ={(1,) : 1}
while p%100 != 0 :
    dico = update_dico(dico)
    p = len(dico)
    print(p)
    n+=1
print(p,n)'''


'''
TOUJOURS PAS ASSEZ RAPIDE...
dico = {}
def p_k(n,k) :
    if n< k :
        return(0)
    elif k==1 or k==n :
        return(1)
    else :
        return(p_k(n-1,k-1) + p_k(n-k,k))
#version encore un peu naive
def p(n) :
    r = 0
    for k in range(1,n+1):
        r+= p_k(n,k)
    return(r)

#p(n,k) = p(n-1,k-1) + p(n-k,k)     p(n,1) = p(n,n) = 1

dico = {}
dico[(1,1)] = 1
dico[(1,0)] = 0
n = 1
p = 2
while p%1000000 != 0 :
    n+=1
    p = 0
    pk = 0
    for k in range(1,n+1):
        if n - k == k :
            a = 1
        elif n-k < k :
            a = 0
        else :
            a = dico[(n-k,k)]
        if k == 1 :
            b = 0
        else :
            b = dico[(n-1,k-1)]
        pk = b + a
        dico[(n,k)] = pk
        p+= pk

print(n)'''

dico = {}
dico[1] = 1
dico[0] = 1
k = 1
n = 1
p = 1
while p%1000000 != 0 :

    n+=1
    if n==1000 :
        break
    bool = True
    p = 0
    k = 1
    while True :
        a = (k*(3*k - 1))/2
        b = (k*(3*k + 1))/2
        x = a
        if n - x >= 0 :
            p += ((-1)**(k-1))*dico[n-x]
        else :
            break
        x = b
        if n - x >= 0 :
            p+= ((-1)**(k-1))*dico[n-x]
        k+=1
    dico[n] = p

print(n,p)
