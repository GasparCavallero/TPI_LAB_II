def crearCodigo(lista): # Busca el último objeto de una lista, accede al atributo código y returnea ese número + 1
    codigo = lista[-1].codigo + 1
    return codigo

def buscarObjetoViaCodigo(codigo, lista): # Busca un match del parámetro "codigo" con el atributo codigo de objetos en una lista y returnea el objeto
    for objeto in lista:
        if objeto.codigo == codigo:
            return objeto
        
def buscarObjetosHabilitados(lista):
    lista = []
    for objeto in lista:
        if objeto.estado == True:
            lista.append(objeto)
    return lista

def cargarArchivoEnLista(archivo, lista, modelo_objeto):
    with open(f"{archivo}", "r") as txt:
        for linea in txt:
            parametros = linea.strip().split(";")
            lista.append(modelo_objeto(parametros))

def convertirEstadosaBool(lista):
    for objeto in lista:
        if objeto.estado == "True":
            objeto.estado = True
        elif objeto.estado == "False":
            objeto.estado = False
        else:
            objeto.estado = None

def convertirCodigosaInt(lista):
    for objeto in lista:
        objeto.codigo = int(objeto.codigo)