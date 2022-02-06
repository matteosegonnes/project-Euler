from main_fct import *
from math import *
from copy import deepcopy
from itertools import combinations

# part of a 8 prime value family

crible = crible_eratos(1000000)
bool = False

def doublons_liste(L):
    # L composée d'elements immutable pour hasher...
    dico = {}
    for k in L :
        if dico.get(k) != None :
            return(True)
        else :
            dico[k] = 1
    return(False)

def list_to_int(L):
    s = 0
    n = len(L)
    for k in range(n):
        s+= (10**(n-1-k)) * int(L[k])
    return(s)

def test_remplace_compteur(n,L, crible):
    # L : liste des indices des digits a remplacer (commence à 0)
    st = str(n)
    l = list(st)
    if len(L) >= len(st) :
        return(0)

    c = 0
    for k in range(10):
        for j in L :
            l[int(j)] = k

        if crible[list_to_int(l) - 2] and l[0] != '0' and l[0] != 0:


            c+=1

    return(c)

def trouver_indice(n) :
    #trouve les digits égaux
    dico = {}
    s = str(n)
    lo = len(s)
    for k in range(lo):
        if dico.get(s[k]) != None :
            dico[s[k]] += [int(k)]
        else :
            dico[s[k]] = [int(k)]
    R = []
    for keys in dico.keys() :
        if len(dico[keys]) > 1 :
            R+= sub_lists(dico[keys])
    return(R)


min_compteur = 8
k = 2
bool = True
while bool :
    if crible[k-2] :

        for liste in trouver_indice(k-2) :
            if test_remplace_compteur(k, liste, crible) == min_compteur :
                print(k)
                bool = False

    k+=1
