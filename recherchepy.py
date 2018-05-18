import os

def recherche(directoire, phrase, extrait, case):
    output = ""
    #cree une liste pour contenire tous les fichiers dans du directoire
    fichiers_liste = list()

    #faire une "marche" pour trouver tous les fichiers dans le directoire specifier
    for subdir, dirs, fichiers in os.walk(directoire):
        for fichier in fichiers:
            #sauveguarder tous ces fichiers dans la liste
            fichiers_liste.append(os.path.join(subdir, fichier))

    #ecrit au console:
    output += 'La phrase a ete trouve dans les fichiers: \n'
    trouve = False

    #trouve chaque nom de fichier dans la liste de fichiers
    for nom_du_fichier in fichiers_liste:
        #ouvre chaque fichier un par un
        try:
            fichier = open(nom_du_fichier, 'r').read()
        except UnicodeDecodeError:
            pass
        for i in range(len(fichier)):
            #je sauveguard chaque phrase la meme longueur que la phrase specifier
            phrase_du_texte = fichier[i:i+len(phrase)]
            #si cette phrase est la meme longueur phrase specifier
            if len(phrase_du_texte) is len(phrase):
                #si la phrase est la phrase specifier
                if case and phrase_du_texte in phrase or not case and phrase_du_texte.lower() in phrase.lower():
                    if case:
                        print('case')
                        print(phrase_du_texte)
                        print(phrase)
                        if phrase_du_texte in phrase:
                            print('prase in phrase')
                    if phrase_du_texte.lower() in phrase.lower():
                        print('!case')
                    trouve = True
                    #imprime le nom du fichier
                    output += '{}: \n'.format(nom_du_fichier)

                    #trouve la distance entre la phrase du texte et la taille de l'extrait choisi
                    mots_avant = 0
                    mots_apres = 0

                    offset_avant = 0
                    offset_apres = 0

                    for j in range(i, -1, -1):
                        if fichier[j] in ' ' or fichier[j] in '\n':
                            mots_avant += 1
                        offset_avant = j
                        if mots_avant is extrait+1:
                            break

                    for j in range(i+len(phrase), len(fichier)):
                        if fichier[j] in ' ' or fichier[j] in '\n':
                            mots_apres += 1
                        offset_apres = j
                        if mots_apres is extrait+1:
                            break

                    #imprime l'extrait
                    output += '\t {} \n'.format(fichier[offset_avant:offset_apres])

    #si le fichier na pas ete trouver, imprime au console:
    if not trouve:
        output += 'La phrase na pas ete trouver \n'

    return output
