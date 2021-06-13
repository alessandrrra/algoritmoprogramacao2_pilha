from node import Node

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def inserir(self, elem):

        #inserir elemento
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def tirar(self):
        
        #removendo elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        raise IndexError("A pilha está vazia.")

    def importarpilha(self):
        print(Pilha)