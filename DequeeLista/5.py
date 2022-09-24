class Queue():
    def __init__(self) -> None:
        self.list = []
    
    def enqueue(self, item, preco):
        self.list.append((item, preco))
    
    def unqueue(self):
        return self.list.pop()

    def remove(self, nome):
        for i in range(len(self.list)):
            if self.list[i][0] == nome:
                return self.list.pop(i)

    def isempty(self):
        return self.list == []

queue = Queue()

while 1:
    entrada = input()
    if entrada == "fim":
        break
    elif entrada[0] == "-":
        nome = entrada[2:]
        queue.remove(nome)
    else:
        nome, preco = entrada.split()
        queue.enqueue(nome, float(preco))

items = 0
soma = 0
while not queue.isempty():
    nome, preco = queue.unqueue()
    print(f"{nome}: R$ {preco:.02f}")
    soma += preco
    items += 1

print("----------------------")
print(f"{items} item(ns): R$ {soma:.02f}")