# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:26:08 2021

@author: anntro
"""

import numpy as np
from matplotlib import pyplot as plt



s_0 =float(input("starthøyde i meter: "))                               # starthøyde i meter
#s_0 = float(input("starthøyde i meter: "))
#v_0 = float(input("starfart i m/s: "))
#q = float(input("når er ballen x over bakken: "))
s_topp = 5.6 #toppen av fallet
a =float(input("Hva er akselerasjonen"))                                  # akselerasjon m/s^2
n = 1000                                  # antall steg
dt = 0.01                                 # størrelse på steg

"-1/2*a*t**2+v_0*t+s_0=s"
"s=1/2(v+v_0)*t"
"2*a*s=v**2-v_0**2"

"""mellomregninger """
s_mellom=(s_topp-s_0)                     # avstanden mellom toppen og start
v_0 = np.sqrt(2*a*s_mellom)               # startfart i m/s
t_slutt = (np.sqrt(2*a*s_0+v_0**2)+v_0)/a # tiden hele fallet tar

print (f"start farta er {round((v_0),2)} m/s")
print (f"hele kastet tar {round((t_slutt),2)}sek")


"""lister """
t = np.zeros(n)                         # tom liste for tida
v = np.zeros(n)                         # tom liste for farta
s = np.zeros(n)                         # tom liste for strekning

""" fyller lista med startverider"""
v[0] = v_0                              # startfart
s[0] = s_0                              # startshøyde


"""fyller lista for alle verdiene mellom start og slutt"""

for i in range (1,n):
   
    t[i] = t[i-1] + dt                  # tid       s
    v[i] = v[i-1] - a*dt                # fart      m/s
    s[i] = s[i-1] + (v[i-1]*dt)         # strekning m
   
   
   
    if round(v[i],2) == 0:
        print(f"Ballen er på toppen etter {round(t[i],3)}sek")
       
   
 
    """Stopper å fylle lista med verider"""
    if s[i] < 0 :                      
        break

"""Regner når ballen er 2.8m over bakken """
for i in range(1,n):
     if round(s[i],1) == 2.8:           # betingelse
         print(f"Ved {round(t[i],2)}sek er ballen 2.8 meter over bakken")
   



"""graftegner"""
plt.title("Fart som funk av tid")       # Tittel
plt.xlabel("tid (s) axis")              # Tittel på x-akse
plt.ylabel("strekning (m)")             # Tittel på y-aske
plt.plot(t,s)                           # valg av variabler
plt.show()                              # viser graf

