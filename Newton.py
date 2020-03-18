# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:37:38 2020

@author: André
"""

print("Digite o número cuja raíz quadrada é buscada:")
c = int(input( ))

print("Digite os extremos do intervalo onde mora a raíz buscada:")
(ai,bi)=(int(input()) ,int(input()))

print("Digite o primeiro termo da sequência (chute inicial)")
xi=int(input())

def f(x):
    return     x**2 - c

def f1(x):
    return     2*x

def phi(x):
    return     x - f(x)/f1(x)

K= 500
i=0


while i in range(0,K):
    if phi(xi) == xi:
        break         
    else:
        xi=phi(xi)
    i+=1
    
print("A raíz procurada é:")
print(xi)
print("O número de iterações necessárias foi")
print(i)        
       