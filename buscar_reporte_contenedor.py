# -*- coding: utf-8 -*-

import pandas as pd  # importo esta libreria para poder leer el reporte que viene en excel
from os import listdir  # esta libreria es para manipular ficheros, etc

# path donde se ubicara el documento a leer.
path_reporte = "D:/maykel/computacion/phyton/cOdIGoS/leyendo txt/buscador de contenedores/final/colocarReporte"

# itero para obtener lo que hay en el path, tiene que ser UN fichero que es el que se va a analizar
for documento in listdir(path_reporte):
    continue
# concateno el string para obtener el path total, que usare en df para leer el documento
nuevo_path = path_reporte + '/' + documento

# leo el documento que se pone en esa direccion, en este caso un csv.
# no_filter es para que no ponga 'nan' cuando se lea un valor de casilla vacio. sin eso lo relacionado
# con datetime no es efectivo y da error.
df = pd.read_csv(nuevo_path, delimiter=';')


# convierto los valores de las filas en listas con esos valores
reporte_contenedores = df.values.tolist()


# esta variable almacenara el codigo de contenedor a buscar. la utilizo en el while
contenedor_buscar = ' '
# su valor es espacio, o sea, no esta vacio.

while contenedor_buscar != '':  # aqui el while se ejecuta siempre que no este vacia la variable
    # por ejemplo, si cuando se solicita el codigo del contenedor
    # presiono la tecla ENTER su valor vacio, y jugara un papel en la condicion
    # de salida del programa.

    print()
    # se solicita el codigo del contenedor
    contenedor_buscar = input('Entre el contenedor a buscar en el reporte: ')
    print()
    contador = 0  # se inicia un contador en 0.

    for contenedor in reporte_contenedores:  # aqui comienza la iteracion por cada valor que exista en la lista
        # con lso valores de las filas en el excel

        if contenedor_buscar in contenedor:  # si el codigo que se solicita para saber se encuentra en el excel

            # entonces el contador es 1. Pudo ser lo mismo con  valores booleanos.
            contador += 1

            print('El contenedor se encuentra y {} está habilitado'.format(
                contenedor[11]))
            print()
            print('Cantidad de dias en puerto: {}.'.format(contenedor[1]))
            print('El No Bl es: {}.'.format(contenedor[6]))
            print('El No Manifiesto es: {}.'.format(contenedor[7]))
            print('Tipo de contenedor y longitud: {} {} pies.'.format(
                contenedor[8], contenedor[9]))
            print('La naviera es: {}.'.format(contenedor[10]))
            print('{} está liberado BL House.'.format(contenedor[13]))
            print('{} está bloqueado.'.format(contenedor[15]))
            print('{} está liberado BL Master.'.format(contenedor[17]))
            print('Se transfirió con fecha: {}. '.format(contenedor[14]))

    # si se presiona ENTER se sale del programa
    if contenedor_buscar == '':

        print('Gracias. Vuelva pronto...')

        break

    elif contador == 0:  # si el contenedor no esta en el excel se indica otro mensaje

        print('El contenedor NO se encuentra en el reporte')
