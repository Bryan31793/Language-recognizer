#primero crear una cola

class Queue():
    """Esta clase representa una cola"""
    def __init__(self):
        self.data = list()
        self.rear = -1

    """Determina si la cola esta vacia o no"""
    def is_empty(self):
        if self.rear == -1:
            return True
        return False
    
    """Inserta un elemento en la cola"""
    def enqueue(self, caracter):
        self.data.append(caracter)  #agrega el caracter al final de la cola
        self.rear += 1

    """Regresa el primer elemento de la cola"""
    def dequeue(self):
        if self.is_empty():
            return None
        
        self.rear -= 1
        return self.data.pop(0)
