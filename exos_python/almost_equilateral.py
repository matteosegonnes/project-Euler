from main_fct import *



'''
def aire_triangle(a,b,c) :

    p = (a+b+c)/2
    test = (p*(p-a)*(p-b)*(p-c))

    if int(test)%8!= 0 and int(test)%8!= 1 and int(test)%8!= 4 :
        return(1.5)
    else :
        return(sqrt(p*(p-a)*(p-b)*(p-c)))


def perimetrer_triangle(a,b,c):
    return(a+b+c)
'''


perimeter_max = 10**9

coté_max = (perimeter_max + 1)//3  + 1    # au dela, plus de trianle quasi equilateral existe avec p <= pmax

x0,y0 = premier_couple_pell_fermat(3)

x1,y1 = x0,y0

somme = 0
perimeter = 0
while perimeter < perimeter_max :

    if (2*x1 - 1)%3 == 0 :
        perimeter = 3 * ((2*x1 - 1)//3) - 1

        if perimeter > perimeter_max :
            break
        somme += perimeter
    if (2*x1 + 1)%3 == 0 :
        perimeter = 3 * ((2*x1 + 1)//3) + 1
        if perimeter > perimeter_max :
            break
        somme += perimeter
    x1,y1 = x1*x0 + 3*y1*y0, x1*y0 + y1*x0

print(somme - 2)   # on enleve 2 car la solution x1,y1 est compté mais pas correcte car correspond a un triangle 1, 1, 0 de perimetre = 2

# pour trouver l'equation de pell-fermat, on exprime l'air du triangle avec la formule au dessus puis on tape dessus...
