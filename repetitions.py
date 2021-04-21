def combinaisons(E,k):
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
for c in combinaisons([1,2,3],2):
    Lt.append(tuple(c))
print(Lt)