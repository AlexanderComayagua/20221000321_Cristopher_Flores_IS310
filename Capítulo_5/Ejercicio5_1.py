def identity(x): return x  # Función de identidad

class Link(object):  # Un dato en una lista enlazada
    def __init__(self, datum, next=None):  # Constructor
        self.__data = datum  # El dato de este enlace
        self.__next = next  # Referencia al siguiente enlace

    # Métodos getter y setter para los atributos de Link

    def isLast(self):  # Comprueba si el enlace es el último en la cadena
        return self.getNext() is None  # Verdadero si y solo si no hay siguiente enlace

    def __str__(self):  # Crea una representación de cadena del enlace
        return str(self.getData())

class LinkedList(object):  # Una lista enlazada de elementos de datos
    def __init__(self):  # Constructor
        self.__first = None  # Referencia al primer enlace

    # Métodos getter y setter para el primer enlace

    def isEmpty(self):  # Comprueba si la lista está vacía
        return self.getFirst() is None  # Verdadero si y solo si no hay primer enlace

    def first(self):  # Devuelve el primer elemento de la lista
        if self.isEmpty():  # Mientras no esté vacía
            raise Exception("No hay elementos en una lista vacía")
        return self.getFirst().getData()  # Devuelve el elemento de datos (no el enlace)

    def __iter__(self):
        link = self.getFirst()  # Comenzamos con el primer enlace
        while link is not None:  # Continuamos mientras haya enlaces
            yield link.getData()  # Devolvemos el dato del enlace
            link = link.getNext()  # Avanzamos al siguiente enlace

    def __len__(self):  # Obtiene la longitud de la lista
        return sum(1 for _ in self)  # Utiliza el iterador para contar los enlaces

    def __str__(self):  # Construye una representación de cadena
        result = "["  # Encerramos la lista en corchetes
        first = True
        for item in self:  # Iteramos sobre los elementos de la lista
            if not first:
                result += " > "  # Después del primer enlace, separamos los enlaces con una flecha hacia la derecha
            result += str(item)  # Agregamos la versión en cadena del enlace
            first = False
        return result + "]"  # Cerramos con corchete cuadrado