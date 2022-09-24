class Queue():
    def __init__(self):
        self.list = list()
    def enqueue(self,item):
        self.list.insert(0,item)
    def dequeue(self):
        return self.list.pop()

class Stack():
    def __init__(self):
        self.list = list()
    def enqueue(self,item):
        self.list.append(item)
    def dequeue(self):
        return self.list.pop()

class PQueue():
    def __init__(self):
        self.list = list()
    def enqueue(self,item):
        for i in range(len(self.list)-1,-1,-1):
            if item > self.list[i]:
                self.list.insert(i+1, item)
                return None
        self.list.insert(0, item)
        

    def dequeue(self):
        return self.list.pop()



for _ in range(5):
    queue = Queue()
    stack = Stack()
    pqueue = PQueue()
    oQueue, oStack , oPqueue = list(), list(), list()
    out = list()

    num_instrucoes = int(input())
    for i in range(num_instrucoes):
        instrucao, num = input().split()
        num = int(num)

        if instrucao == 'in':
            queue.enqueue(num)
            stack.enqueue(num)
            pqueue.enqueue(num)
        elif instrucao == 'out':
            oQueue.append(queue.dequeue())
            oStack.append(stack.dequeue())
            oPqueue.append(pqueue.dequeue())
            out.append(num)

    print(out, oQueue, oStack, oPqueue)
    if (oQueue == oStack == out) or (oQueue == oPqueue == out) or (oStack == oPqueue == out):
        print('uai?')
    elif oQueue == out:
        print('FIFO')
    elif oStack == out:
        print('LIFO')
    elif oPqueue == out:
        print('AIPO')
    else:
        print('no hay!')





