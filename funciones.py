
from typing import DefaultDict
import data.plantas as plan
import data.informacion as info

#buscando nombre de ciudad

def buscar_por_ciudad_en_Sopladora(ciudad):
    
    if ciudad == 'Quito':
        return(sum(plan.consumo_energia['Sopladora']['Quito']['consumos'])* plan.consumo_energia['Sopladora']['Quito']['tarifa'])
    elif ciudad == 'Guayaquil':
        return(sum(plan.consumo_energia['Sopladora']['Guayaquil']['consumos'])* plan.consumo_energia['Sopladora']['Guayaquil']['tarifa'])
    elif ciudad == 'Loja':
        return(sum(plan.consumo_energia['Sopladora']['Loja']['consumos'])* plan.consumo_energia['Sopladora']['Loja']['tarifa'])
    else:
        return('No existe la ciudad en Dicha planta')


    
def buscar_por_ciudad_en_Coca(ciudad):
    
    if ciudad == 'Quito':
        return(sum(plan.consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])*plan.consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
    elif ciudad == 'Guayaquil':
        return(sum((plan.consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])* (plan.consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])))
    else:
        return('No existe la ciudad en Dicha planta')


#Buscando por nombre de la planta

def buscar_por_planta(planta, ciudad):
    if planta == 'Coca Codo Sinclair':
        return buscar_por_ciudad_en_Coca(ciudad)
    elif planta == 'Sopladora':
        return buscar_por_ciudad_en_Sopladora(ciudad)
    else:
        return('No existe la planta en la BASE DE DATOS')

#Calculando por mes

def cal_mes (planta, mes):
    a = (plan.consumo_energia[planta]['Quito']['consumos'][mes] * plan.consumo_energia[planta]['Quito']['tarifa'])
    b = (plan.consumo_energia[planta]['Guayaquil']['consumos'][mes] * plan.consumo_energia[planta]['Guayaquil']['tarifa'])
    
    if planta == 'Sopladora':
        total = a+b+(plan.consumo_energia[planta]['Loja']['consumos'][mes] * plan.consumo_energia[planta]['Loja']['tarifa'])
        return total
    elif planta == 'Coca Codo Sinclair':
        total= a+b
        return total


#opción 3

def region(nombre):
    sms = 'La region en base las plantas que abastecen allí ha generado: $'
    nombre= nombre.lower()
    if nombre == 'costa':
        return(sms , (sum(plan.consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])*84) + (sum(plan.consumo_energia['Sopladora']['Guayaquil']['consumos'])*55))
    elif nombre == 'sierra':
        return(sms, (sum(plan.consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])*65) + (sum(plan.consumo_energia['Sopladora']['Quito']['consumos'])*79) + (sum(plan.consumo_energia['Sopladora']['Loja']['consumos'])*32))
    elif nombre == 'oriente':
        return ('En Nueva Loja no existen plantas que la abastezcan')
    else:
        return ('No hay region con Ingreso que mostrar')

#opcion 2
def ask_city_coca(name):
     
  if name == 'Quito':
    energia = sum(plan.consumo_energia['Coca Codo Sinclair'][name]['consumos'])
    plan.plantas['Coca Codo Sinclair']= energia

  elif name == 'Guayaquil':
      energia = sum(plan.consumo_energia['Coca Codo Sinclair'][name]['consumos'])
      plan.plantas['Coca Codo Sinclair']= energia

  else:
    plan.plantas['Coca Codo Sinclair']='Para esta ciudad no le abastece esta planta'

def ask_city_sopla(name):
   
    if name == 'Quito':
        energia = sum(plan.consumo_energia['Sopladora'][name]['consumos'])
        plan.plantas['Sopladora']= energia

    elif name == 'Guayaquil':
        energia = sum(plan.consumo_energia['Sopladora'][name]['consumos'])
        plan.plantas['Sopladora']= energia
    elif name == 'Loja':
        energia = sum(plan.consumo_energia['Sopladora'][name]['consumos'])
        plan.plantas['Sopladora']= energia
    else:
        plan.plantas['Sopladora']='Para esta ciudad no le abastece esta planta'

