# Desarrollo de un agente aspiradora
# La basura debe ser generada aleatoriamente
# Requisitos v1:
# 15 movimientos
# Imprimir base de conocimiento
# Requisitos v2:
# 50 movimientos
# Imprimir base de conocimiento

import turtle
import random
import csv
from time import sleep

t1 = turtle.Turtle()
t2 = turtle.Turtle()
agente = turtle.Turtle()

#Escritura de las leyendas
t1.hideturtle()
t1.penup()
t1.setpos(-100,120)
t1.write("Lado A", align="center", font=("Arial",12,"normal"))
t1.setpos(100,120)
t1.write("Lado B", align="center", font=("Arial",12,"normal"))

#Dibujo de los espacios
t2.hideturtle()
t2.setpos(0,100)
t2.speed(0)
for _ in range(2):
    t2.forward(200)
    t2.right(90)
t2.forward(400)
for _ in range(3):
    t2.right(90)
    t2.forward(200)
t2.penup()
t2.right(90)

# Definicion de la forma y configuracion del agente
agente.setpos(0,0)
agente.shape("square")
agente.color("blue")
agente.shapesize(4)
agente.penup()
agente.speed(1)

# Indicadores
t1.setpos(-100, -75)
t2.setpos(100, -75)
t1.shape("square")
t2.shape("square")
t1.color("black")
t2.color("black")
t1.shapesize(1,4)
t2.shapesize(1,4)
t1.showturtle()
t2.showturtle()

#Numero de ciclos deseados
ciclos = int(input("Ingrese el numero deseado de ciclos: "))
print("\nEjecucion:\n") 
print("# ciclo"+" "+"Accion en A"+" "+"Estado A"+" "+"Accion en B"+" "+"Estado B")
#Ciclos de limpieza
_ = 1
#Variables de seguimiento
accionA="NONE"
accionB="NONE"
posicion = ""

#Creacion de las listas para guardar los registros del agente
nciclos = []
lpos = []
laccionA = []
lestadoA = []
laccionB = []
lestadoB = []
lmov = []

while _ <= ciclos:
    #Seleccion del primer lado a comprobar
    if agente.pos() == (0,0):
        estadoA = False
        t1.color("green")
        estadoB = False
        t2.color("green")
        mr = random.choice([-100,100])
        agente.goto(mr,0)
        if mr == -100:
            mov = "LEFT"
        elif mr == 100:
            mov = "RIGHT"
        lmov.append(mov)

    #Seleccion aleatoria del estado de los espacios A y B
    #Donde Verdadero simula la deteccion de basura (rojo) y Falso la ausencia de esta (verde)  
    #Agente en el Lado A
    if agente.pos() == (-100.00,0.00):
        posicion = "Lado A"
        if not estadoA:
            accionA="NONE"
            print(str(_)+" "+posicion+" "+str(estadoA)+" "+accionA+" "+str(estadoB)+" "+accionB)
            nciclos.append(_)
            lpos.append(posicion)
            lestadoA.append(estadoA)
            laccionA.append(accionA)
            lestadoB.append(estadoB)
            laccionB.append(accionB)

        elif estadoA:
            accionA="CLEAN"
            sleep(2)
            t1.color("green")
            print(str(_)+" "+posicion+" "+str(estadoA)+" "+accionA+" "+str(estadoB)+" "+accionB)
            nciclos.append(_)
            lpos.append(posicion)
            lestadoA.append(estadoA)
            laccionA.append(accionA)
            lestadoB.append(estadoB)
            laccionB.append(accionB)    
            estadoA = False
            accionA="NONE"
        
        estadoB = random.choice([True,False])
        if estadoB:
            t2.color("red")
        elif not estadoB:
            t2.color("green")
        agente.goto(100,0)
        mov = "RIGHT"
        lmov.append(mov)

    if agente.pos() == (100.00,0.00):
        posicion = "Lado B"
        if not estadoB:
            accionB = "NONE"
            print(str(_)+" "+posicion+" "+str(estadoA)+" "+accionA+" "+str(estadoB)+" "+accionB)
            nciclos.append(_)
            lpos.append(posicion)
            lestadoA.append(estadoA)
            laccionA.append(accionA)
            lestadoB.append(estadoB)
            laccionB.append(accionB)
        if estadoB:
            accionB = "CLEAN"
            sleep(2)
            t2.color("green")
            print(str(_)+" "+posicion+" "+str(estadoA)+" "+accionA+" "+str(estadoB)+" "+accionB) 
            nciclos.append(_)
            lpos.append(posicion)
            lestadoA.append(estadoA)
            laccionA.append(accionA)
            lestadoB.append(estadoB)
            laccionB.append(accionB)  
            estadoB = False
            accionB = "NONE"
        
        estadoA = random.choice([True,False])
        if estadoA:
            t1.color("red")
        if not estadoA:
            t1.color("green")
        agente.goto(-100,0)
        mov = "LEFT"
        lmov.append(mov)

    #Impresion de los ciclos de trabajo
    
    _ += 1
    if _ == ciclos+1:
        t1.color("black")
        t2.color("black")
        agente.goto(0,0)
        

print("\n-----------Simulacion terminada-----------\n\n")        
turtle.exitonclick()

#Creacion del archivo .csv con los datos de la simulacion
choice = input("¿Desea generar el registro del Agente? (Si/No): ")
choice.lower()
if choice == "si":
    outfile = open("Registro.csv","w")
    outfile.write("Ciclo, Movimiento, Posicion, Estado en A, Accion en A, Estado en B, Accion en B")
    outfile.write("\n")

    for _ in range(0,len(nciclos)):
        newrow = ""
        newrow = ("{},{},{},{},{},{},{}".format(nciclos[_],lmov[_],lpos[_],lestadoA[_],laccionA[_],lestadoB[_],laccionB[_]))
        outfile.write(newrow)
        outfile.write("\n")
    outfile.close()
else:
    print("\n-----------Ejecución Terminada-----------\n\n")