#module pour lire les csv
import csv
import matplotlib.pyplot as plt
import numpy as np

def firstdigit(n):
    # n est un nombre entier positif
    return n // 10**(len(str(n))-1)


def occurrences(liste):
    ocur = list()
    nombres = np.vectorize(firstdigit)(liste)
    for d in range(1,10):
        ocur.append(np.count_nonzero(nombres == d))
    return ocur


fichier = open('BTT_TD_POP1A_2016.txt','r')
tableau = csv.reader(fichier, delimiter=';')
L = list(tableau)
print(L[0])
print(L[1])
print(L[2])
print(L[3])
L1 = list()
print(len(L))
print(L[690000][5])
for line in range((350000)):
    if L[line][5].replace('.','',1).isdigit():
        L1.append(int(float(L[line][5])))
values = occurrences(L1)
plt.bar(range(1,10),values)
plt.show()