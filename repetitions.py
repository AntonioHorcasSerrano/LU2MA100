count = 0
def combinaisons(E,k):
    global count
    count += 1
    if E == []:
        return []
    if k==0:
        return [[]]
    else:
        result = combinaisons(E,k-1)
        for e in result:
            e.insert(0,E[0])  #insert E[0] before e[0], push others to the right
        result += combinaisons(E[1:],k)
    return result

Lt=list()
for c in combinaisons([1,2,3,4,5,6,7,8,9,10],9):
    Lt.append(tuple(c))
print(len(Lt))
print(count)

# A=[['1'],['2'],['3'],['4']]
# for a in A:
#     a.insert(0,'#')
#     print(A)

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for result in powerset([1, 2, 3]):
    print(result)

def combin(n,k):
    """Nombre de combinaisons de n objets pris k a k (calcul récursif)"""
    if k==0 or k==n:
        return 1
    return combin(n-1, k-1) + combin(n-1,k)
combin(4 + 2 - 1, 2)