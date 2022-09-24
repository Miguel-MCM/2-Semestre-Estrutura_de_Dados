entrada = input()

class Queue():
    def __init__(self):
        self.lista = []

    def enqueue(self, letra):
        self.lista.insert(0,letra)

    def dequeue(self):
        return self.lista.pop()
    
    def processData(self, string):
        for letra in string:
            if letra == "*":
                print(self.dequeue(), end="")
            else:
                self.enqueue(letra)

queue = Queue()
queue.processData(entrada)