class Queue():
    def __init__(self):
        self.list = []
    def enqueue(self,item):
        self.list.insert(0, item)
    def dequeue(self):
        return self.list.pop()
    def is_empty(self):
        return self.list == []

# receber numeros
veiculos, fator, peso_lim = map(int, input().split())

#organizar a fila
fila = Queue()
for i in input().split():
    fila.enqueue(int(i))

tempo = 0
#ver o veiculos
while not fila.is_empty():
    #ver um
    veiculo = fila.dequeue()
    if veiculo > peso_lim:
        tempo += 10
        fila.enqueue(veiculo-2)
    else:
        tempo += 5
    #liberar os outro
    for i in range(fator-1):
        if fila.is_empty():
            break
        tempo += 1
        fila.dequeue()
    
print(tempo)