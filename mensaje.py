import data.plantas as plan
import funciones as fun
#menú

def intro (z):
    if z ==1:
        print('\n Para consulta de Total de megavatios de consumos de una ciudad en Una Planta [1]')
        print('Para conocer El total de megavatios que cada Planta le ha dado a la ciudad [2]')
        print('Para conocer lo recaudado por Region [3]')
        print('Para conocer lo recaudado por planta en un mes determinado [4]')
        print()
        return('Para salir [0] \n ' )


#VALIDACIÓN PLANTA 
def validar_plan (nombre) :
    if nombre != 'Sopladora' and nombre != 'Coca Codo Sinclair':
        
        return('ERROR DE DIGITALIZACIÓN') 
    




#meses

def meses_anho (mes):
    if mes == 0:
        return ('Enero')
    elif mes == 1:
        return ('Febrero')
    elif mes == 2:
        return ('Marzo')
    elif mes == 3:
        return('Abril')
    elif mes == 4:
        return('Mayo')
    elif mes == 5:
        return('Junio')
    elif mes == 6:
        return('Julio')
    elif mes ==7:
        return('Agosto')
    elif mes ==8:
        return('Septiembre')
    elif mes == 9:
        return('Octubre')
    elif mes == 10:
        return('Noviembre')
    elif mes == 11:
        return('Diciembre')
    else:
        return('MES NO EXISTE')

# mostrar PLANTAS

def mostrar_plantas(q):
    if q ==1:
        print ('\n Las Plantas Existentes son: \n')
        for i in plan.consumo_energia:
            print( i)
    return('----------------------------------------')
    