#!/usr/bin/pynthon
milisegundos=int(input("ingrese los milisegundos:"))
if milisegundos >=0:
    dias=milisegundos//86400000
    horas=milisegundos//3600000
    minutos=milisegundos//60000
    segundos=milisegundos//1000
    milisegun=milisegundos
    print(dias)
    print(horas)
    print(minutos)
    print(segundos)
    print(milisegundos)
else:
    print ("numero incorreto")

  



