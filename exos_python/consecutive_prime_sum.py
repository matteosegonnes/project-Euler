from main_fct import *


L = crible_eratos(1000001)

s = 0
j = 0
max = 0
cmax = 0

while j< 1000000:
    s = 0
    i = j
    c = 0
    while s < 1000000 :
        if i >= 1000000 :
            break
        if L[i] :
            s+=(i+2)
            if s > 1000000 :
                break
            c+=1
        if L[s-2] and c>=cmax:
            cmax = c
            max = s

        i+=1
        if i >= 1000000 :
            break
        while L[i] == False :
            i+=1
            if i >= 1000000 :
                break

    j+=1
    if j == 1000000 :
        break
    while L[j] == False :
        j+=1
        if j == 1000000 :
            break

print('resultat : ', max , ' ; avec : ', cmax, 'termes dans la decomposition')
