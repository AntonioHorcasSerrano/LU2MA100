from itertools import permutations, combinations

def aretes(K):
    c = list()
    for sommet in K:
        for v in K[sommet]:
            if {sommet,v} not in c: # verifie si l'arête exite déjà (1,2)=(2,1)
                c.append({sommet,v})
    return {(s,v) for s,v in c} # retourne l'ensemble des arêtes en forme de couple (hashable)

def triangles(K):
    L=list()
    A = aretes(K)
    print('aretes:',A)
    s = set(dict.keys(K))
    t = list(map(set, combinations(s, 3)))
    for tr in t:
        c = list(map(tuple, combinations(tr, 2)))
        add = True
        for couple in c:
            if couple not in A:
                add = False
                break
        if add == True:
            L.append(tr)
    print(L)
                
triangles({1: {2, 3, 4}, 2: {1, 3}, 3: {1, 2}, 4: {1}})