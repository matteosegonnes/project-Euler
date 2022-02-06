from main_fct import *
import scipy.special



c = 0
for n in range(1,101):
    for k in range(n+1):
        if scipy.special.binom(n, k) >= 10**6 :
            c+=1

print(c)
