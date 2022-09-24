class Item():
    def __init__(self, dado, prox=None, ant=None):
        self.dado = dado
        self.prox = prox
        self.ant = ant
    

def printL(lista) -> str:
    atual = lista

    end = False
    while not end:
        if atual:
            print(atual.dado)
        if atual.prox == None or atual.prox == lista:
            end = True
            continue
        else:
            atual = atual.prox

        

def remove(lista, dado):
    primeiro = lista
    end = False
    while not end:
        if lista.dado == dado:
            if lista.ant != None:
                lista.ant.prox = lista.prox
            if lista.prox != None:
                lista.prox.ant = lista.ant
            return lista
        if lista.prox == primeiro or lista.prox == None:
            break
        lista = lista.prox

lista = Item(3)
print(type(lista))
print(lista == lista)

lista = remove(lista, 1)

