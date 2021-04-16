#module pour lire les csv
import csv
#module pour faire un graphique
from pylab import *
#ouverture du fichier 
lecture= open('vac.csv','r')
read = csv.reader(lecture, dialect='excel')
li=list(read)
#on fait un tableau forme du premier caractere
#de la premiere chaine (il n y en a qu une)
#de chaque ligne non vide
compt=[int(elem[0][0]) for elem in li if len(elem) > 0 ] 
abs=range(1,10)
#on compte
effe=[compt.count(k) for k in abs]
#on represente
bar(abs,effe,width=0.35,color='r',align='center',edgecolor='b')
show()
lecture.close()
#  1234 // 10**(len(str(1234))-1)