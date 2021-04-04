def touschemins(K, i, f, c=set()):
        c = c.copy()
        c.add(i)
        print('recursion avec:',c)
        if i == f:
            return [c]
        if i not in K:
            return set()
        cs = []
        for n in K[i]:
            if n not in c:
                cs_ = touschemins(K, n, f, c)
                print(c)
                for nc in cs_:
                    cs.append(nc)
        return cs

# print(touschemins({1: {2, 3, 4}, 2: {1, 3}, 3: {1, 2}, 4: {1}},2,3))


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                print(path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
print(find_all_paths({1: {2, 3, 4}, 2: {1, 3, 4}, 3: {1, 2, 4}, 4: {1, 2, 3}},2,3))

def recursive(n, s):
    s = s + [n]
    if n == 1:
        return 1
    else:
        k = recursive(n-1,s)
        print(s)
        return n + k
# s=list()
# print(recursive(4))

def recursive(n, s=set()):
    s = s.copy()
    s.add(n)
    if n == 1:
        return 1
    else:
        k = recursive(n-1,s)
        print(s)
        return n + k

# print(recursive(4))

def Fibb(n):
    if n==0 or n==1:
        return 1
    else:
        return Fibb(n-1)+Fibb(n-2)
# print(Fibb(20))

def chemin(K, i, f, c=set()):
    print(c)
    c.add(i)
    if i not in K:
        return None
    if i == f:
        return c
    for n in K[i]:
        if n not in c:
            cn = chemin(K, n, f, c)
            return cn
    return None

# print(chemin({1: {2, 3, 4}, 2: {1, 3}, 3: {1, 2}, 4: {1}},2,3))

import numpy as np
a = np.array([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]])
b = np.linalg.matrix_power(a,2)
# les éléments diagonaux répresentent le nombre d'arêtes de chaque sommet
# avec B on voit s'il y a un chemin de dimension 2 entre les deux indices. A partir de A on voit s'il ont une arête en commun, ce qui signifie que c'est un triangle. Ensuite il faut vérifier s'il sont connectés entre 
n = a.shape[0]
l = list()
print(b)
for i in range(n):
    for j in range(i+1,n):
        if b[i][j] >= 1: # il y a au moins un chemin d'ordre 2 entre i et j
            t = a[i] + a[j]
            for v in range(n):
                if t[v] > 1:   
                    print({i,j,v})
                    if {i,j,v} not in l:
                        l.append({i,j,v})
print(l)