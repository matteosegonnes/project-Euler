from main_fct import *
import math
from pqdict import minpq

fichier = open("p083_matrix.txt", "r")

matrix = []
for line in fichier :
    integ = []
    a = line.strip('\n')
    l = a.split(',')
    for k in l :
        integ += [int(k)]
    matrix += [integ]



'''IDEE : GRAPHE + DIJKSTRA'''
# on utilise un dictionnaire pour la structure graphe

graphe = {}
for k in range(80):
    for j in range(80):
        graphe[(k,j)] = {}


for k in range(80):
    for j in range(80):
        try :
            graphe[(k,j)][(k,j+1)] = matrix[k][j+1]
        except Exception :
            None

        try :
            graphe[(k,j)][(k+1,j)] = matrix[k+1][j]
        except Exception :
            None

        try :
            if k>0 :
                graphe[(k,j)][(k-1,j)] = matrix[k-1][j]
            else :
                None
        except Exception :
            None
graphe['entree'] = {(0,0) : 4445}
graphe['sortie'] = {}
graphe[(79,79)]['sortie'] = 0

#graphe pret

dist, pred = dijkstra(graphe, 'entree')
print(pred)
min = math.inf
for k in range(80):

    dist, pred = dijkstra(graphe, source = (k,0))


    for j in range(80):
        t = dist[(j,79)] + matrix[k][0]
        if t<min :
            min = t

print(min)
