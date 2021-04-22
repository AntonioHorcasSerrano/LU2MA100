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