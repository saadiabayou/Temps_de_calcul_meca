# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 00:34:08 2021

@author: Saadia Bayou
"""
"""
   Etude de convergence 
   Plaque trouée en traction  
   
   Ce programme trace et génère le graphe du temps de calcul en ms 
   en fonction du nombre d'éléments finis du maillage
   
"""

import numpy as np
import matplotlib.pyplot as plt 

#TRI3
mNeTc3=np.loadtxt("NeTc3.txt")

print("\nMatrice nombre d'éléments temps de calcul TRI3 : \n \nmNeTc_TRI3 = ", mNeTc3)

Ne3=mNeTc3[:,0]
print("\nNe3 : Ne_TRI3 =",Ne3)

Tc3=mNeTc3[:,1]
print("\nTemps de calcul: Tc_TRI3 =",Tc3)

# TRI6
mNeTc6=np.loadtxt("NeTc6.txt")

print("\nMatrice nombre d'éléments temps de calcul TRI6 : \n \nmNeTc_TRI6 = ", mNeTc6)

Ne6=mNeTc6[:,0]
print("\nNe6 : Ne_TRI6 =",Ne6)

Tc6=mNeTc6[:,1]
print("\nTemps de calcul: Tc_TRI6 =",Tc6)


plt.subplot (211) 
plt.plot(Ne3,Tc3,marker = '+',label="Temps de calcul TRI3",color="red")
plt.plot(Ne6,Tc6,marker = '+',label="Temps de calcul TRI6",color="blue")


plt.xlabel("Nombre d'éléments du maillage ")
plt.ylabel("Temps de calcul en ms")
plt.title("Temps de calcul en fonction du nombre d'éléments du maillage ")
plt.legend()
plt.savefig("Graphe14-Temps de calcul")
plt.show()

print ("\nLe temps de calcul augmente avec le nombre d'éléments du maillage")
print ("\nCe temps de calcul est plus important pour les éléments triangles à 6 noeuds - TRI6 ")


