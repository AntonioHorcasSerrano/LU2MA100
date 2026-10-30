def create_dict_sequences(s):
    """ 
    str -> dict[str:int]
    retourne le nombre d'occurrences des éléments de la chaîne de caractères
    """
    L=list(s)
    D=dict()
    for e in L:
        if e not in D:
            D[e]=1
        else:
            D[e]=D[e]+1
    return D
    
assert create_dict_sequences('ACCTG')=={'A': 1, 'C': 2, 'T': 1, 'G': 1}

import random

def infect(S,D):
    d0={'A':'AAA','C':'CCCC','G':'GGGG','T':'TTT'}
    out=''
    for char in S:
        if char in d0.keys():
            if random.random()>=D[char]:
                out=out+d0[char]
            else:
                out=out+d0[char][0]
    return out

# print(infect('ACCTG',{'A':0.2,'C': 0.5,'G': 0.3,'T': 0.1}))

import numpy as np

def S(A,B,i,j):
    return 1 if A[i]==B[j] else 0

def needleman_wunsch(A,B):
    m=len(A)
    n=len(B)
    F = np.zeros((m+1,n+1),dtype=int)
    for i in range(1,m+1):
        for j in range(1,n+1):
            F[i,j]=max(F[i-1,j-1]+S(A,B,i-1,j-1),F[i-1,j]-1,F[i,j-1]-1)
    return F.max()


assert needleman_wunsch('GAATTCAGTTA','GGATCGA')==4
assert needleman_wunsch('TGACGTGC','TCGACGTCA')==5

SEQ="CGTCCGGTTTCGATTGGAGGGCTCGGAA"
D=dict()
with open("adn.txt","r") as file:
    for ligne in file:
        (first, last, seq) = ligne.split()
        key = needleman_wunsch(SEQ,seq)
        if key not in D:
            D[key]=[(first, last, seq)]
        else:
            D[key].append((first, last, seq))

import pprint
L=list()
for score in reversed(sorted(D)):
    for person in D[score]:
        first, last, sequence = person
        L.append((score, first, last))
for k in range(8):
    pprint.pprint(L[k])