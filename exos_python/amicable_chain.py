from main_fct import *


def somme_diviseurs(n):
    somme = 0
    if n == 1 :
        return(0)

    k = 2

    if n%2 == 0 :
        while k < sqrt(n) + 1 :
            if n%k == 0 :
                somme += k
                if n//k != k :

                    somme += n//k
            k+=1
    else :
        k = 3
        while k < sqrt(n) + 1 :
            if n%k == 0 :
                somme += k
                if n//k != k :
                    somme += n//k
            k+=2
    return(1+somme)


def amicable_chaine(n, dico_passe):

    dico_chaine = {}
    r = n
    k = 0
    while dico_chaine.get(r) == None :

        print(r)
        dico_chaine[r] = k

        if dico_passe.get(r) != None :
            return(0,0)
        else :
            dico_passe[r] = 1

        r = somme_diviseurs(r)

        if r > 1000000 :
            return(0,0)


        k+=1

    i = dico_chaine[r]
    longueur_chaine = k-i
    return(longueur_chaine,min)


dico_passe = {}

k = 1
max_longueur = 2
min_nombre = 0
n = 0
while k< 1000000 :

    if dico_passe.get(k) == None :

        longueur,min = amicable_chaine(k,dico_passe)

        if longueur > max_longueur :
            max_longueur = longueur
            min_nombre = min
    print(k)
    k+=1

print(max_longueur, min_nombre)
