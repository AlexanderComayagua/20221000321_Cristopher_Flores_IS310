x=input("Ingrese una cadena de caracteres: ")

def impresion(x):
    imp=[char for char in x if not char.isspace()]
    print(imp)
    return imp
impresion(x)