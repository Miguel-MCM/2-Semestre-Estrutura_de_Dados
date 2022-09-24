def getElementsByClassName(raiz, classes):
    retorno = []
    for i in raiz:
        if "class" in raiz[i]:
            for j in classes.casefold().split():
                if raiz[i]["class"].casefold() == j:
                    retorno.append(i)
                    break
        if "children" in raiz[i]:
            retorno.extend(getElementsByClassName(raiz[i]["children"], classes))
    return retorno
