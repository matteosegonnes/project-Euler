from main_fct import *


bool = True
k = 0
while bool :

    k+=1

    bool2 = True
    for i in range(1,7):
        if not deux_permutation(str(k), str(i*k)):
            bool2 = False
            break

    if bool2 :
        print(k)
        break
