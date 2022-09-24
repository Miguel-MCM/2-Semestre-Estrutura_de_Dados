def getElementById(raiz, id):
    if raiz:
        id = id.casefold()
        ids = []

        if '*' in id:
            comeco, final = id.split('*')
            for i in raiz:
                if comeco in i[:len(comeco)].casefold() and final in i[-len(final):].casefold():
                    ids.append(i)
                if type(raiz[i]) == dict:
                    ids.extend(getElementById(raiz[i], id))
        else:
            for i in raiz:
                if i.casefold() == id:
                    ids.append(i)
                if type(raiz[i]) == dict:
                    ids.extend(getElementById(raiz[i], id))
        return ids

raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}}
print(sorted(getElementById(raiz, 'h*m')))