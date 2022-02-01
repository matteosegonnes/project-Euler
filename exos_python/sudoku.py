from main_fct import *
from copy import deepcopy


# we name by sudoku a string which contain 9 lines of 9 numbers separated with \n

fichier = open("p096_sudoku.txt", 'r')

def recup_sudokus(fichier) :
    Liste_sudokus = []
    k = 0
    sudoku = ''
    for line in fichier :

        if k%10 == 0 :
            None


        elif k%9 == 0 :
            sudoku = sudoku + line
            sudoku = sudoku.strip('\n')
            liste = sudoku.split('\n')

            Liste_sudokus+=[liste]
            sudoku = ''
            k = -1


        else :
            sudoku = sudoku + line
        k+=1

    return(Liste_sudokus)  # sous forme de liste de liste : un sudoku = list de string

sudokus = recup_sudokus(fichier)




''' FONCTION BRUTEFORCE'''

def configuration_possible(sudoku) : # renvoie True s'il n'y a pas 2 elements en doubles (lignes, colonnes, carrés)

    # lines

    for k in sudoku :
        dico_ligne = {}

        for j in k :
            if j == '0' :
                None
            else :
                if  dico_ligne.get(j) == None :
                    dico_ligne[j] = 1

                else :
                    return(False)
    #columns

    for k in range(9):
        dico_colonnes = {}
        for j in range(9):
            string = sudoku[j][k]
            if string == '0' :
                None
            else :
                if dico_colonnes.get(string) == None :
                    dico_colonnes[string] = 1
                else :

                    return(False)

    # carrés

    carres = []
    for k in range(0,7,3): #0 , 3 , 6
        for j in range(0,7,3): #0 , 3 , 6
            carre = []
            for pk in range(3):
                carre += sudoku[k + pk][j : j+3]
            carres += [carre]

    for k in carres:
        dico_ligne_carre = {}

        for j in k :
            if j == '0' :
                None
            else :
                if  dico_ligne_carre.get(j) == None :
                    dico_ligne_carre[j] = 1
                else :
                    return(False)

    return(True)

def compteur_zero_ligne(sudoku):

     i = None
     min = 10
     for k in range(len(sudoku)) :
         compteur = 0
         for j in sudoku[k] :
             if j == '0':
                 compteur += 1
         if compteur > 0 and compteur < min :
             min = compteur
             i = k
     return(i) # renvoie la ligne où il y a le moins de zero (mais au moins 1)

def hashage(sudoku) :
    sudokucopy = deepcopy(sudoku)
    for k in range(len(sudoku)) :
        sudokucopy[k] = tuple(sudokucopy[k])
    return(tuple(sudokucopy))  # pas utilisé dans solveur_logique : comment hasher mieux ? ...

def solveur_brute_force(sudoku, dico):

    if compteur_zero_ligne(sudoku) == None :

        return(sudoku, True)

    else :
        # at least one '0' in sudoku so we solve...

        sudokucopy2 = deepcopy(sudoku)
        sudokucopy3 = deepcopy(sudoku)

        for k in range(len(sudoku)):
            for j in range(len(sudoku[k])) :

                if sudoku[k][j] == '0' :

                    for x in [1,2,3,4,5,6,7,8,9] :


                        sudokucopy2[k][j] = str(x)
                        t = hashage(sudokucopy2)
                        if configuration_possible(sudokucopy2) and dico.get(t) == None :

                              dico[t] = 1
                              (s, b) = solveur_brute_force(sudokucopy2, dico)
                              sudokucopy2 = deepcopy(sudokucopy3)
                              if b :
                                     return (s, b)
        return(None, False)   # solveur brute force





'''FONCTION NON BRUTEFORCE'''

def classer_ligne_colonne_carre(sudoku):
    # renvoie la ligne ou colonne ou carré avec le min > 0 de '0' pour déduire plus vite

    bool1 = False
    bool2 = False
    bool3 = False

    min = 10
    for k in range(len(sudoku)) :
        compteur = 0
        for j in sudoku[k] :   # j : str caractere
            if j == '0':
                compteur +=1

        if compteur > 0 and compteur < min :
            min = compteur
            bool1 = True
            i = k

    if min == 10 : #cas terminal tte les lignes remplies car compteur == 0 pour tout k
        return(100, None)

    if min == 1 :
        return(i, 'ligne')

    c = 9
    for j in range(9):
        compteur = 0
        for k in range(len(sudoku)):
            if sudoku[j][k] == '0':
                compteur +=1
        if compteur > 0 and compteur < min :
            min = compteur
            bool2 = True
            c = j

    if min == 1 :
        return(c, 'colonne')

    carres = []
    for k in range(0,7,3): #0 , 3 , 6
        for j in range(0,7,3): #0 , 3 , 6
            carre = []
            for pk in range(3):
                carre += sudoku[k + pk][j : j+3]
            carres += [carre]

    ca = 9
    for k in range(len(carres)):
        compteur = 0
        for j in range(len(carres[k])) :
            if carres[k][j] == '0':
                compteur +=1
        if compteur > 0 and compteur < min :
            bool3 = True
            min = compteur
            ca = k

    if bool3 :
        return(ca, 'carre')
    elif bool2 :
        return(c, 'colonne')
    else:
        return(i, 'ligne') # renvoie ligne carre ou colonne avec le mouins de vide

def ligne_carre_colonne_correspondant(sudoku, i,j) :
     # renvoie ligne carre et colonne de l element L[i][j]

    ligne = sudoku[i]

    colonne = []
    for k in range(len(sudoku)):
     colonne += sudoku[k][j]

    carre = []
    k_reduce = (i//3)*3
    j_reduce = (j//3)*3
    for pk in range(3):
        carre += sudoku[k_reduce + pk][j_reduce : j_reduce+3]

    return(ligne, colonne, carre) #renvoie ligne colonne et carre de L[i][j]


def nombres_possible_ligne_carre_colonne(ligne, colonne, carre):


    dico1= {}
    set1 = set()

    for k in ligne :
        if k != '0':
            if dico1.get(k) == None :
                dico1[k] = 1
            else :
                return(set())

    for k in range(1,10):
        if dico1.get(str(k)) == None :
            set1.add(str(k))

    dico2= {}
    set2 = set()
    for k in colonne:
        if k != '0':
            if dico2.get(k) == None:
                dico2[k] = 1
            else :
                return(set())

    for k in range(1,10):
        if dico2.get(str(k)) == None :
            set2.add(str(k))

    dico3 = {}
    set3 = set()
    for k in carre :
        if k != '0':
            if dico3.get(k) == None :
                dico3[k] = 1
            else :
                return(set())
    for k in range(1,10):
        if dico3.get(str(k)) == None :
            set3.add(str(k))

    set_final = set1.intersection(set2,set3)
    return(set_final)  #renvoie le set des nombres pas utilisés dans la ligne le carre et la colonne

def solveur_logique(sudoku) :

    if classer_ligne_colonne_carre(sudoku)[0] == 100 :  #

        return(sudoku, True)


    else :
        (x, chaine) = classer_ligne_colonne_carre(sudoku)  # x : numero
        i_corres = 0
        j_corres = 0

        if chaine == 'ligne' :
            for j in range(len(sudoku[x])) :  # 9
                if sudoku[x][j] == '0':
                    i_corres = x
                    j_corres = j
                    break

        elif chaine == 'colonne' :
            for j in range(9):
                if sudoku[j][x] == '0':
                    i_corres = j
                    j_corres = x
                    break

        else :   # a partir du carré : avoir les L[i][j]
            bool = False
            k_reduce = (x//3)*3
            j_reduce = (x%3)*3
            for k in range(k_reduce, k_reduce+3):
                for j in range(j_reduce, j_reduce+3):
                    if sudoku[k][j] == '0':
                        i_corres = k
                        j_corres = j
                        bool = True
                        break
                if bool :
                    break


        ligne, colonne, carre = ligne_carre_colonne_correspondant(sudoku, i_corres, j_corres)
        set_final = nombres_possible_ligne_carre_colonne(ligne, colonne, carre)

        if set_final == set() :  #config impossible
            return (None, False)

        else :
            copy_sudoku = deepcopy(sudoku)
            copy_sudoku2 = deepcopy(sudoku)


            for k in set_final :
                copy_sudoku[i_corres][j_corres] = k

                (s,b) = solveur_logique(copy_sudoku)
                copy_sudoku = deepcopy(copy_sudoku2)

                if b :
                    return(s,b)

            return(None, False)   # solveur plus "optimisé" bien que NP evidemment



somme = 0
for sudoku in sudokus :
    for k in range(len(sudoku)):
        sudoku[k] = list(sudoku[k])

    solve = solveur_logique(sudoku)[0]
    somme += 100*int(solve[0][0]) + 10*int(solve[0][1]) + int(solve[0][2])

print(somme)
