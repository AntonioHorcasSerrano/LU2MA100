mots = ['Abricot', 'Airelle', 'Ananas', 'Banane', 'Cassis', 'Cerise', 'Citron',\
'Clémentine', 'Coing', 'Datte', 'Fraise', 'Framboise', 'Grenade', 'Groseille',\
'Kaki', 'Kiwi', 'Litchi', 'Mandarine', 'Mangue', 'Melon', 'Mirabelle', 'Nectarine',\
'Orange', 'Pamplemousse', 'Papaye', 'Pêche', 'Poire', 'Pomme', 'Prune', 'Raisin']
mots_dict=dict()
for word in mots:
    for letter in word:
        if (letter,letter.find(letter)) not in mots_dict:
            mots_dict[(letter,word.find(letter))]={word}
        else: 
            mots_dict[(letter,word.find(letter))].add(word)
mots_dict