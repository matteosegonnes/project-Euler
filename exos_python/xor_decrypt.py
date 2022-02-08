from main_fct import *
import string
from copy import deepcopy

fichier = open('p059_cipher.txt', 'r')

chaine = fichier.read()
L = chaine.split(',')

for k in range(len(L)):
    L[k] = int(L[k])



def ascii_word(mot):
    r = 0
    for k in mot :
        r+=ord(k)
    return(r)

all_lower_case = string.ascii_lowercase
V = deepcopy(L)


for i in all_lower_case :
    for j in all_lower_case:
        for w in all_lower_case :
            cle1, cle2, cle3 = ord(i), ord(j), ord(w) #int

            for k in range(0,len(L) - 2,3):
                L[k] = L[k] ^ cle1
                L[k+1] = L[k+1] ^ cle2
                L[k+2] = L[k+2] ^ cle3

            for k in range(len(L)):
                L[k] = chr(L[k])


            txt = ''

            for k in L :
                txt = txt + k
            if 'or' in txt and 'a' in txt and 'of' in txt and 'the' in txt and 'an' in txt and 'I' in txt and 'Euler' in txt:
                texte_final = txt
                print(texte_final)
            L = deepcopy(V)

print(ascii_word(texte_final))
