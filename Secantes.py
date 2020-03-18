# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:37:38 2020

@author: André
"""

print("Digite o número cuja raíz quadrada é buscada:")
c = int(input( ))

print("Digite os extremos do intervalo onde mora a raíz buscada:")
(ai,bi)=(int(input()) ,int(input()))

print("Digite os dois primeiros termos da sequência (chutes iniciais)")
xi=int(input())
xii=int(input())
def f(x):
    return     x**2 - c

def phi(x,y):
    return     y - (f(y)*(y-x))/(f(y)-f(x))

K= 500
eps = 10**(-25)
i=0

# k=phi(xi,xii)
# print(i,xi,xii,k)
while i in range(0,K):
    k=phi(xi,xii)
    if phi(xi,xii) == xii:
        break         
    elif abs(f(xii)) < eps:
        break
    else:
        xi=xii
        xii=k        
    i+=1
    # print(i,xi,xii,phi(xi,xii))
print("A raíz procurada é:")
print(k)
print("O número de iterações necessárias foi")
print(i)        
       