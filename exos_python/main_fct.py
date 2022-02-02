# avoir les fonctions utiles + aide et rappels
from math import *
from itertools import combinations
from pqdict import minpq  #module pour dijkstra atour des piles avec priorité
from fractions import Fraction

'''SLICING'''

# str[a:b] renvoie str[a] str[a+1] ... str[b-1]   d à g car step = 1 > 0
# str[a:b:step] renvoie str[a] str[a+step] ... str[b-1-eps] car a priori : b-1 != a +p*step
# str[a:] de str[a] jusqu'a la fin du tableau
# a[:stop] = a[0:stop]    du début jusqu'a str[stop -1]
# general : si step > 0 : gauche à droite (comme au dessus) et droite à gauche sinon
#                 ex : a[-2:]  les 2 derniers ( -2 et-1 car -1 étant le dernier) g à d
#                      a[:-2] tout sauf les 2 derniers  g à d
#                      a[::-1] tout reversed     d à g
#                      a[1::-1]    2 premiers reversed     d à g
#                      a[-3::-1]  tout sauf les 2 derniers reversed     d à g


'''MATHS'''

def premier(n):

    if n<=10:
        if n==2 or n==3 or n==5 or n==7 :
            return(True)
        else :
            return(False)

    else :
        if n%2==0:
            return(False)

        for k in range(3,int(sqrt(n))+1,2): # valable pour n>10 en sautant les pairs

            if n%k == 0:
                return(False)
    return(True) #version "classique" du test de primalité

def crible_eratos(N) :
    #Liste des booleen premiers en partant de n = 2 jusqu'a N et L[k-2] pour nombre k donc len = N-2+1 = N-1

    if N%2 == 0 :
        L = [False,True]*((N-2)//2) #cas des pairs
        L.append(False)
    else :
        L = [False,True]*(N//2)

    L[0] = True
    c = 1
    while c < N-2 :

        if L[c] :
            for k in range(2, int(N/(c+2) -1)+1,2):
                L[c+k*(c+2)] = False
        c+=1
    return(L)  # pour N >= 2 : la liste des booleen des nbr premiers <= N

def premier_eratostene(n):
    if n==1 :
        return(False)
    if n==2 :
        return(True)
    L = [True for _ in range(2,int(sqrt(n))+2)] #création très longue pour juste n%3==0 par ex..
    c = 0
    while c < int(sqrt(n))-1 :

        if L[c] :
            if n%(c+2) == 0 :
                return(False)
            for k in range(1, int((int(sqrt(n))+1)/(c+2) -1)+1):
                L[c+k*(c+2)] = False
        c+=1
    return(True)  #utilisation du crible pour test de primalité

def fact(n):
    if n==0:
        return(1)
    r = 1
    for k in range(1,n+1):
        r = r*k
    return(r)  #factorielle de n entier >= 0

def base_b(x,b):

    if x==0:
        return 0
    base = '0123456789abcdefghijklmnopqrstuvwxyz'
    resultat = ''
    while x!= 0:
        x,reste = x//b , base[x%b]
        resultat = reste + resultat
    return(resultat) # converti x (base 10) en base b entier dans [2,36] car 10 + 26 lettres = 36

def palindrome(mot):

    if mot == [] or mot == '':
        return False

    elif len(mot) == 1:
        return True

    else :
        booleen = True
        n = len(mot)
        if n%2 == 0 :
            stop = n//2
        else :
            stop = (n-1)//2
        for k in range(stop) :
            if mot[k] != mot [n-1-k]:
                booleen = False
                break

        return booleen  # renvoie true si L (liste) ou string est palindrome

def pandigital(nombre):
    n = len(str(nombre))
    dico = {}
    boleen = True
    for k in str(nombre):
        if dico.get(int(k)) == None and 1<=int(k)<= n :
            dico[int(k)] = 1
        else :
            return(False)
    return(True) #test si un entier est 1_to_n pandigital avec 1<=n<=9 !!

def decomposition_facteur(n):
    # si tu trouves un algo polynomiale on deviens riche ;)

    if n==1 :
        return( {1:1} )
    if n==2 :
        return( { 2 : 1} )

    dico = {}
    L = crible_eratos(int(sqrt(n))+1)

    while n >1 :


        bool = True
        for k in range(len(L)) :

            if L[k] and n%(k+2) == 0:

                bool = False
                if dico.get(k+2) == None :
                    dico[k+2] = 1
                else :
                    dico[k+2] +=1
                n = n//(k+2)
                break
        if bool :
            if dico.get(n) == None :
                dico[n] = 1
            else :
                dico[n]+=1
            n = 1
    return(dico) # renvoie {p1 : vp1(n), p2 : vp2(n), ..., pn : vpn(n)} vpi : valuation pi-adique

def decomposition_facteur_multi(n,L):
    # L = crible pour eviter de calculer à chaque fois

    if n==1 :
        return( {1:1} )
    if n==2 :
        return( { 2 : 1} )

    dico = {}

    while n >1 :

        bool = True
        for k in range(len(L)) :

            if L[k] and n%(k+2) == 0:

                bool = False
                if dico.get(k+2) == None :
                    dico[k+2] = 1
                else :
                    dico[k+2] +=1
                n = n//(k+2)
                break
        if bool :
            if dico.get(n) == None :
                dico[n] = 1
            else :
                dico[n]+=1
            n = 1
    return(dico)

def decompo_somme_generateur(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1] #partionne un entier (je comprend R mais algo le plus efficace au monde askip)

def partition(n):
    L = []
    for j in decompo_somme_generateur(n):
        L+=[j]
    return(L) # pareil que decompo_somme_generateur mais renvoie la liste

def phi(n,crible) :

    if crible[n-2] :
        return(n-1)

    else :
        if n%2 != 0 :

            p = 1
            for k in range(1,int(sqrt(n)) -1,2) :

                u = k + 2

                if n%u == 0 :
                    if crible[k] :
                        p = p * (1 - Fraction(1,u))

                    a = n//u

                    if crible[a - 2] and u != a :
                        p = p * (1 - Fraction(1,a))


        else :
            p = 1
            p = (1 - Fraction(1,2))
            for k in range(1,int(sqrt(n)) -1,2) :
                u = k + 2

                if n%u == 0 :
                    if crible[k] :
                        p = p * (1 - Fraction(1,u))

                    a = n//u

                    if crible[a - 2] and u != a :
                        p = p * (1 - Fraction(1,a))
    return(n*p)   # indicatrice d'euler assez optimisé



'''PERMUTATIONS et ROTATION'''

# les fonctions permut sont certes en O(n!) mais très surement "efficace" (plus que recursif par ex)
# !!En cas de doute de l'efficacité pour project_euler, utiliser itertools de python
#     from itertools import permutations
#     chaine_permu = [''.join(p) for p in permutations(mot)]    pour une str (donc à adapter pour list)
# itertools ne semble pas forcement gérer les doublons mieux que permut (il faut utiliser set)
# itertools offre cependant d'autres possibilités : taille, produit cartesien etc

def permutliste(liste, sans_doublons):

    p = [liste]
    n = len(liste)
    for k in range(0,n-1):
        for i in range(0,len(p)):
            z = p[i][:]
            for c in range(0, n-k-1):
                z.append(z.pop(k))
                if sans_doublons :
                    if (z not in p):
                        p.append(z[:])
                else :
                    p.append(z[:])
    return(p)

def permutchaine(mot, sans_doublons):

    return[''.join(z) for z in permutliste(list(mot),sans_doublons)]

def rotation(mot,sans_doublons):

    # renvoie la liste des rotations de mots avec ou sans doublons

    n = len(mot)
    if n==1 :
        return([mot])
    else :
        L = []
        for k in range(0,n):
            mot = mot[n-1] + mot[:n-1]
            if sans_doublons :
                if mot not in L :
                    L+=[mot]
    return L

def deux_permutation(L1,L2): #gere aussi les doublons

    if len(L1)!= len(L2) :
        return(False)
    else :

        dico1 = {}
        for k in L1 :
            if dico1.get(k) == None :
                dico1[k] = 1
            else :
                dico1[k] += 1

        boleen = True
        for k in L2:
            if dico1.get(k) == None:
                return(False)
            else :
                if dico1[k] == 1 :
                    del dico1[k]
                else :
                    dico1[k] -= 1

        return(True)  # dit en O(n) si L1 permutation de L2 (liste ou str)

def sub_lists(my_list):
	subs = []
	for i in range(2, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs # renvoie la liste des sous listes de L

def period_square_roots(n):

    dico = {}
    if sqrt(n) == int(sqrt(n)):
        return([int(sqrt(n)), [] ])
    else :
        a0 = int(sqrt(n))
        L = []
        # reste = sqrt(n) - a0   avec reste < 1
        bool = True
        a = a0
        b = 1
        while bool :
            (c, a2, b2) = reduction_for_period_square_roots(n, a, b)
            a = a2
            b = b2

            if dico.get((a,b)) == None :
                dico[(a,b)] = 1
                L = L + [c]
            else :
                bool = False

    return((a0, L)) # sqrt(n) = a0 + 1/(a1 + 1/(a2 +...))   return( L = [a0,[a1,a2,...,aN]) and sequence in L[1] is repeating

def reduction_for_period_square_roots(N,a,b):
    # X = (sqrt(n) - a)/b  re arrange X sous la forme 1/(p + q ) avec q<1 et p entier car X<1

    d = gcd(b,N - a**2)
    X = int(b/d)
    Y = int((N-a**2)/d)
    # we are at 1/ ( (sqrt(N) + X*a) / Y )    NORMALEMENT... X = 1    (conjecture d'apres enoncé)
    c = 0
    while (X*sqrt(N) + X*a)/Y - c > 1 :
        c+=1
    return( c, -(X*a - c*Y), Y)   #fonction anecdotique qui sert pour la fonction au dessus

def expansion(L) :

    if len(L) == 1:
        return(Fraction(1,L[0]))
    else :
        return(Fraction(1,L[0] + expansion(L[1:])))  #si L = [a1,a2,...,an] renvoie a1 + 1/(a2 + 1 /(a3 + 1/) ...)


'''FICHIER TEXTE'''

#nom_fichier = open("mon_fichier.extansion", "r")
        #r : read
        # fichier.txt est dans le meme repertoire que le fichier .py ou alors spécifier le chemin

# chaine = fichier.read()   chaine de caractere de tout le fichier
    #il peut y avoir des '\n' si le fichier contient des lignes par ex

# pour récuperer tout le contenu d'une seule chaine de caractere: chaine.split()

# ex : chaine = "bd-be\n\"i"
# (import re)   chaine = re.split('-|\n|\"', chaine) renvoie ['bd', 'be', 'i']
    # syntaxe : a = re.split('p1|p2|...|pn', a)
    # on a donc split sur le - et le \n et le "
    # en python , " = \" pour differencier dans une chaine ex : " \"salut\" " : " "salut" "

# SI ON SPLIT SUR LE 1er OU DERNIER CARACTERE :
    # a = ""moi","toi"" = "\"moi\",\"toi\""
    # alors re.split('\",\"|\"', a) renvoie ['', 'moi', 'toi', '']
    # on a bien viré le ' "," ' du milieu mais comme on split sur le 1ER et/ou dernier: on a '' dans la liste...
    # on utilise donc strip pour les caracteres du debut ou fin :
    # a.strip('\"') retire le " du début et de la fin
    # Ainsi, si a = ""moi","toi,"lui"\n"
    # a = re.split('\",\"', a.strip('\"').strip('\n')) renvoie ['moi', 'toi', 'lui']
    # remarque : on a enlevé le \" dans le re.split() car il ne sert a rien de split dessus car on strip apres

''' LETTRES AVEC ORD'''

# ord("A") - 64 = 1     ord("B") - 64 = 2       etc
# ord("a") - 96 = 1     ord("B") - 96 = 2       etc...
# chr est la fonction inverse de ord

'''RECURSIVITE'''

def create_liste(N,chiffre_max) :
    if  N == 0 :
        return([[]])

    else :
        R = []
        for k in range(chiffre_max):
            for f in create_liste(N-1,chiffre_max):
                R+=[[k] + f]
        return(R) #exemple de récursivité

''' SYNTAXE D'UNE EXCEPTION

try:
      x = int(input("Please enter a number: "))

except ValueError:
      print("Oops!  That was no valid number.  Try again...") '''


'''GRAPHES'''

def dijkstra(graph, source, target=None):
    dist = {}  #lengths of the shortest paths to each node
    pred = {}  #predecessor node in each shortest path

    # Store distance scores in a priority queue dictionary
    pq = minpq()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')

    # popitems always pops out the node with min score
    # Removing a node from pqdict is O(log n).
    for node, min_dist in pq.popitems():
        dist[node] = min_dist
        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    # Updating the score of a node is O(log n) using pqdict.
                    pq[neighbor] = new_score
                    pred[neighbor] = node

    return (dist, pred) # pour graphe implementer avec dict de dict ...

# renvoie sous forme de dict la distance de entrée à chaque noeud et aussi (à part) les predecesseurs de chaque noeud
#dist, pred = dijkstra(graphe, 'entree') puis faire dist['sortie'] pour chemin de 'entrée' a 'sortie'

def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)
    path.reverse()
    return path #renvoie le chemin de entree à sortie dans le graphe

'''EQUATION PELL-FERMAT'''

def reduite(liste):
    if len(liste)%2 == 0 :
        return(liste[:-1])
    else :
        V = liste + liste
        return(V[:-1]) # la réduite sert dans la fonction en dessous cf wikipedia

def premier_couple_pell_fermat(D):
    #x,y
    if sqrt(D) == int(sqrt(D)):
        return(None)
    else :
        liste = period_square_roots(D)
        L = [liste[0]] + reduite(liste[1])
        frac = expansion(L)
        return(frac.denominator , frac.numerator) # donne la premiere solution de x**2 - D * y**2 = 1 dans N*N
