# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:26:54 2020

@author: André
"""
print("Digite o número cuja raíz quadrada é buscada:")
c = int(input( ))

print("Digite os extremos do intervalo ondemora a raíz buscada:")
(ai,bi)=(int(input()) ,int(input()))


def f(x):
    return     x**2 - c

K= 500
eps=10**(-5)
xi= (ai+bi)/2
i=0


while i in range(0,K):
    if f(xi) == 0:
        break            
    elif f(xi)*f(ai) < 0:
        ai=ai
        bi=xi
    else:
        ai=xi
        bi=bi
    xi=(ai+bi)/2
    i+=1
    # if abs(f(xi)) < eps:
    #     break
    # if abs(ai-bi) < eps:
    #     break
print("A raíz procurada é:")
print(xi)
print("O número de iterações necessárias foi")
print(i)        
       