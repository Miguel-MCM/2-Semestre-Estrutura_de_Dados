class Deque():
    def __init__(self) -> None:
        self.lista = []
    
    def addFront(self,item):
        if self.lista:
            self.lista.insert(0, item)
        else:
            self.lista.append(item)
    
    def addRear(self, item):
        self.lista.append(item)
    
    def removeFront(self):
        if self.lista:
            return self.lista.pop(0)
    
    def removeRear(self):
        if self.lista:
            return self.lista.pop()


entrada = input()
deque = Deque()
remocoes = []

for i in entrada:
    if i.isdigit():
        deque.addRear(i)
    elif i == "*":
        remocoes.append(deque.removeFront())
    elif i == "+":
        remocoes.append(deque.removeRear())
    else:
        deque.addFront(i)

for i in remocoes:
    print(i, end='')
    
