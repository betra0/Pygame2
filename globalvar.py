variable_global = 5

def mostrar():
    print(variable_global)
def modificar_variable_global():
    global variable_global
    variable_global -= 2

while True:
    mostrar()
    
    modificar_variable_global()