# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import gzip
import datetime

path = Input("Ingrese la path donde estan los archivos")
# <codecell>

def Outdegree(dom):
    global path
    
    ### Busqueda del índice ###
    f_index = gzip.open(path+"\\pld-index.gz")
    index = -1
    t_index = datetime.datetime.now()
    line =  f_index.readline()
    while line and index == -1:
        aux = line.split('\t')
        if aux[0]==dom:
            index = aux[1][:-1]
        line = f_index.readline()
    t_index = datetime.datetime.now()-t_index
    f_index.close()
    
    ### Contar arcos ###
    f_arc = gzip.open(path+"\\pld-arc.gz")
    t_arcs = datetime.datetime.now()
    arcs = 0
    #Los indices de salida estan ordenados. Es decir, todos los que salen del dominio 'A' estan juntos en la lista.
    i = False #iterador que me dirá si ya termine de recorrer los dominios de salida
    line = f_arc.readline()
    while line and not i:
        aux = line.split('\t')
        if aux[0] == index:
            arcs += 1
        elif arcs > 0:
            i = True #Condicion de salida del loop
        line = f_arc.readline()
    t_arcs = datetime.datetime.now()-t_arcs
    f_arc.close()
    
    ### Reporte ###
    print("El dominio: " +str(dom) +", de indice: "+str(index)+", posee: "+str(arcs)+" arcos de salida")
    print("Tiempo busqueda indice: "+str(t_index))
    print("Tiempo busqueda arcos: "+str(t_arcs))
    print("Tiempo total outdegree: "+str(t_arcs+t_index))

# <codecell>

def Indegree(dom):
    global path
    
    ### Busqueda del índice ###
    f_index = gzip.open(path+"\\pld-index.gz")
    index = -1
    t_index = datetime.datetime.now()
    line =  f_index.readline()
    while line and index == -1:
        aux = line.split('\t')
        if aux[0]==dom:
            index = aux[1][:-1]
        line = f_index.readline()
    t_index = datetime.datetime.now()-t_index
    f_index.close()
    
    ### Contar arcos ###
    f_arc = gzip.open(path+"\\pld-arc.gz")
    arcs = 0
    t_arcs = datetime.datetime.now()
    line = f_arc.readline()
    while line:
        aux = line.split('\t')
        if aux[1][:-1] == index:#Le saco el salto de línea
            arcs += 1
        try:
            line = f_arc.readline()
        except:
            line = False
    t_arcs = datetime.datetime.now()
    f_arc.close()
    
    ### Reporte ###
    print("El dominio: " +str(dom) +", de indice: "+str(index)+", posee: "+str(arcs)+" arcos de llegada")
    print("Tiempo busqueda indice: "+str(t_index))
    print("Tiempo busqueda arcos: "+str(t_arcs))
    print("Tiempo total outdegree: "+str(t_arcs+t_index))
    
    

# <codecell>

### Ejemplo ###
Indegree("apple.com")

