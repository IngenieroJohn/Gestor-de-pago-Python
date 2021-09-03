#
import funciones as fun
import data.plantas as plan
import mensaje as ms
import json


op = -1

while op != 0:
    
    print(ms.intro(1))

    op=int(input('Ingrese Opción: '))

    if op == 1:
        print(ms.mostrar_plantas(1))
        nom_planta= input('Ingrese el nombre de la planta: ')
        nom_ciudad= input('\n Ingrese el nombre de la ciudad: ')
        fun.buscar_por_planta(nom_planta, nom_ciudad)
        print(' \n El total que genera la ciudad de:  ', nom_ciudad, ' \n en la Planta : ', nom_planta, ' \n es de: $', fun.buscar_por_planta(nom_planta, nom_ciudad) )
    
    elif op == 2:
        print('Ingrese con la primera letra mayúscula¡¡¡¡ \n')
        name_city = input('Ingrese nombre de la ciudad: ')
        fun.ask_city_coca(name_city)
        fun.ask_city_sopla(name_city)
        print('Las plantas que abastecen con la respectiva energía dada son: ')
        print(json.dumps(plan.plantas, sort_keys=False, indent=2))

    elif op == 3:
        region=input('Ingrese el nombre de la Region Ecuatoriana: ')
        print(fun.region(region))

    elif op == 4:
        mes = int(input('Ingrese el mes en números: '))
        mes= mes -1
        print(ms.meses_anho(mes))
        print(ms.mostrar_plantas(1))
        plan_cal= input('Ingrese la planta correspondiente: ')
        print(ms.validar_plan(plan_cal), '\n')
        a= fun.cal_mes(plan_cal, mes)
        print('En el mes de: ', ms.meses_anho(mes), '\n la planta: ', plan_cal, '\n GENERÓ: $', fun.cal_mes(plan_cal, mes))
        






