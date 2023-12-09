class NodoBST:
    def __init__(self, clave, valor=None, izquierda=None, derecha=None):
        self.clave = clave
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class BinarySearchTree:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor=None):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoBST(clave, valor)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor

        return nodo

    def nodeBalance(self):
        return self._nodeBalance(self.raiz)

    def _nodeBalance(self, nodo):
        if nodo is None:
            return 0

        return self._nodeBalance(nodo.derecha) - self._nodeBalance(nodo.izquierda)

    def levelBalance(self):
        return self._levelBalance(self.raiz)

    def _levelBalance(self, nodo):
        if nodo is None:
            return 0

        return self._maxLevel(nodo.derecha) - self._maxLevel(nodo.izquierda)

    def _maxLevel(self, nodo):
        if nodo is None:
            return 0

        return 1 + max(self._maxLevel(nodo.izquierda), self._maxLevel(nodo.derecha))

    def unbalancedNodes(self, by=1):
        return self._unbalancedNodes(self.raiz, by)

    def _unbalancedNodes(self, nodo, by):
        if nodo is None:
            return []

        node_balance = abs(self._nodeBalance(nodo))
        level_balance = abs(self._levelBalance(nodo))

        if node_balance > by or level_balance > by:
            return [nodo.clave] + self._unbalancedNodes(nodo.izquierda, by) + self._unbalancedNodes(nodo.derecha, by)
        else:
            return self._unbalancedNodes(nodo.izquierda, by) + self._unbalancedNodes(nodo.derecha, by)
bst = BinarySearchTree()
bst.insertar(5)
bst.insertar(3)
bst.insertar(7)
bst.insertar(2)
bst.insertar(4)
bst.insertar(6)
bst.insertar(8)
bst.insertar(1)
bst.insertar(9)
bst.insertar(10)

print("Equilibrio de nodos:", bst.nodeBalance())
print("Equilibrio de niveles:", bst.levelBalance())
print("Nodos desequilibrados (by=1):", bst.unbalancedNodes())
print("Nodos desequilibrados (by=2):", bst.unbalancedNodes(2))