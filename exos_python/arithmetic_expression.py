from main_fct import *

#string = '5*(4+3)'

def operateur(string,a,b) :
    # for op = {+, *, -, /}
    if string == '+' :
        return(a+b)
    elif string == '*' :
        return(a*b)
    elif string == '-' :
        return(a-b)
    else  :
        return(Fraction(a,b))


def partition_two_liste(L) :
    # len(L) = 4 ou 3
    #ensemble des moyens de partitionner 3 ou 4 éléments en 2 sous listes
    if len(L) != 4 and len(L) != 3 :
        return('erreur, len != 4 ; 3')

    if len(L) == 3 :
        R = []
        for k in range(len(L)):
            R+= [[[L[k]]] + [L[:k] + L[k+1:]]]
        return(R)

    else :
        R = []
        for k in range(len(L)):
            R+= [[[L[k]]] + [L[:k] + L[k+1:]]]
        a,b,c,d = L[0],L[1],L[2],L[3]
        R += [[[a,b],[c,d]]] + [[[a,c],[b,d]]] + [[[a,d],[c,b]]]
        return(R)


def arithmetic_exp(L) :
    # at first, L = [a,b,c,d]         last call : L = [x]
    # a < b < c < d    op = {+, -, *, /}

    if len(L) == 1 :
        return([L[0]])

    elif len(L) == 2 :
        a, b = L[0], L[1]
        R = []
        R += [a+b] + [a-b] + [a*b] + [b-a] + [Fraction(a,b)] + [Fraction(b,a)]
        return(R)

    else :
        R = []
        sub = partition_two_liste(L)
        operateurs = ['+', '-', '/', '*']
        for deux_listes in sub :

            l1 = deux_listes[0]
            l2 = deux_listes[1]

            for op in operateurs :
                if op == '/' or op == '-' :

                    F1 = arithmetic_exp(l1)
                    F2 = arithmetic_exp(l2)
                    for f1 in F1 :
                        for f2 in F2 :
                            try:
                                  R+= [operateur(op, f1, f2)]

                            except ZeroDivisionError:
                                  None

                            try:
                                  R+= [operateur(op, f2, f1)]

                            except ZeroDivisionError:
                                  None

                else :

                    F1 = arithmetic_exp(l1)
                    F2 = arithmetic_exp(l2)

                    for f1 in F1 :
                        for f2 in F2 :

                            R+= [operateur(op, f1, f2)]

        return(R)



def un_to_n(L):
    liste = arithmetic_exp(L)
    dico = {}
    for k in liste :
        if k > 0 and k == int(k):
            if dico.get(k) == None :
                dico[k] = 1
            else :
                None
    i = 1
    while dico.get(i) != None :
        i+=1
    return(i-1)

max = 0
string = 0
for k in range(1,7):
    for j in range(k,8):
        for i in range(j,9):
            for u in range(i,10):
                L = [k,j,i,u]
                x = un_to_n(L)
                if x > max :
                    string = str(k) + str(j) + str(i) + str(u)
                    max = x

print(max,string)
