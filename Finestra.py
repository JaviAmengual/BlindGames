import time
import winsound
import keyboard
import playsound
import pyttsx3
import random
from tkinter import *

engine = pyttsx3.init()

desbloqueo = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]


QLOVAC = [["DO", 1], ["DO", 1], ["SOL", 1], ["SOL", 1], ["LA", 1], ["LA", 1], ["SOL", 2], ["FA", 1], ["FA", 1], ["MI", 1], ["MI", 1], ["RE", 1], ["RE", 1], ["DO", 2],
["SOL", 1], ["SOL", 1], ["FA", 1], ["FA", 1], ["MI", 1], ["MI", 1], ["RE", 1], ["RE", 1], ["SOL", 1], ["SOL", 1], ["FA", 1], ["FA", 1], ["MI", 1], ["MI", 1], ["RE", 1], ["RE", 1],
["DO", 1], ["DO", 1], ["SOL", 1], ["SOL", 1], ["LA", 1], ["LA", 1], ["SOL", 2], ["FA", 1], ["FA", 1], ["MI", 1], ["MI", 1], ["RE", 1], ["RE", 1], ["DO", 2]]

HDLA = [["MI", 1], ["MI", 1], ["FA", 1], ["SOL", 1], ["SOL", 1], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["DO", 1], ["RE", 1], ["MI", 1], ["MI", 1.5], ["RE", 0.5], ["RE", 2],
["MI", 1], ["MI", 1], ["FA", 1], ["SOL", 1], ["SOL", 1], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["DO", 1], ["RE", 1], ["MI", 1], ["RE", 1.5], ["DO", 0.5], ["DO", 1], ["SILENCIO", 1],
["RE", 1], ["RE", 1], ["MI", 1], ["DO", 1], ["RE", 1], ["MI", 0.5], ["FA", 1], ["MI", 1], ["DO", 1], ["RE", 1], ["MI", 0.5], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["RE", 1], ["RE", 2],
["MI", 1], ["MI", 1], ["FA", 1], ["SOL", 1], ["SOL", 1], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["DO", 1], ["RE", 1], ["MI", 1], ["RE", 1.5], ["DO", 0.5], ["DO", 1]]

CARAGOL = [["DO", 0.5], ["RE", 0.5], ["MI", 1], ["MI", 0.5], ["MI", 0.5], ["MI", 1], ["MI", 0.5], ["FA", 0.5], ["SOL", 1], ["SOL", 0.5], ["SOL", 0.5], ["SOL", 1],
["FA", 0.5], ["MI", 0.5], ["RE", 1], ["RE", 0.5], ["RE", 0.5], ["RE", 1], ["MI", 0.5], ["RE", 0.5], ["DO", 1], ["DO", 0.5], ["DO", 0.5], ["DO", 1], ["DO@", 0.5], ["SI", 0.5], ["LA", 1],
["LA", 0.5], ["LA", 0.5], ["LA", 1], ["LA", 0.5], ["SOL", 0.5], ["FA", 1], ["FA", 0.5], ["FA", 0.5], ["FA", 1], ["MI", 0.5],["RE", 0.5], ["DO", 1], ["DO", 0.5], ["DO", 0.5], ["DO", 2]]

SYL = [["DO", 1.5], ["RE", 0.5], ["MI", 1.5], ["DO", 0.5], ["MI", 1], ["DO", 1], ["MI", 2], ["RE", 1.5], ["MI", 0.5], ["FA", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 2], ["SILENCIO", 1],
["MI", 1.5], ["FA", 0.5], ["SOL", 1.5], ["MI", 0.5], ["SOL", 1], ["MI", 1], ["SOL", 2], ["FA", 1.5], ["SOL", 0.5], ["LA", 0.5], ["LA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["LA", 2], ["SILENCIO", 1],
["SOL", 1.5], ["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 0.5], ["LA", 2], ["SILENCIO", 1], ["LA", 1.5], ["RE", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SI", 2], ["SILENCIO", 1],
["SI", 1.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SI", 0.5], ["DO@", 2], ["SILENCIO", 1], ["DO@", 0.5], ["SI", 0.5], ["LA", 1], ["FA", 1], ["SI", 1], ["SOL", 1], ["MI", 1], ["RE", 1], ["DO", 1]]

SUSANA = [["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["SOL", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SOL", 0.5], ["MI", 0.5], ["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 0.5], ["RE", 1],
["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["SOL", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SOL", 0.5], ["MI", 0.5], ["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["MI", 0.5], ["RE", 0.5], ["RE", 0.5], ["DO", 2],
["FA", 1], ["FA", 1], ["LA", 0.5], ["LA", 1], ["LA", 0.5], ["SOL", 0.5], ["SOL", 0.5], ["MI", 0.5], ["DO", 0.5], ["RE", 1],
["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["SOL", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SOL", 0.5], ["MI", 0.5], ["DO", 0.5], ["RE", 0.5], ["MI", 0.5], ["MI", 0.5], ["RE", 0.5], ["RE", 0.5], ["DO", 2]]

PDC = [["RE", 1], ["MI", 1], ["FA", 1.5], ["SOL", 0.5], ["LA", 1], ["SOL", 1], ["FA", 1], ["MI", 1], ["FA", 1], ["SOL", 1], ["LA", 1], ["SOL", 2], ["FA", 0.5], ["SOL", 0.5], ["LA", 1.5], ["SOL", 0.5], ["FA", 1],
["MI", 1], ["FA", 1], ["MI", 1], ["RE", 1.5], ["MI", 0.5], ["DO", 1], ["RE", 3], ["SILENCIO", 2], ["RE", 0.5], ["MI", 0.5], ["FA", 1.5], ["MI", 0.5], ["FA", 1], ["SOL", 1], ["FA", 1], ["SOL", 1],
["LA", 1.5], ["SOL", 0.5], ["FA", 1], ["RE", 2], ["RE", 0.5], ["MI", 0.5], ["FA", 1], ["SOL", 1], ["LA", 1], ["SI", 1], ["RE", 1.5], ["SOL", 0.5], ["FA", 1.5], ["SOL", 0.5], ["MI", 1], ["RE", 3]]

NANA = [["MI", 0.5], ["MI", 0.5], ["SOL", 1.5], ["MI", 0.5], ["MI", 1], ["SOL", 2], ["MI", 0.5], ["SOL", 0.5], ["DO@", 1], ["SI", 1], ["SILENCIO", 1], ["LA", 0.5], ["LA", 1], ["SOL", 1], ["RE", 0.5], ["MI", 0.5], 
["FA", 1], ["RE", 1], ["RE", 0.5], ["MI", 0.5], ["LA", 2], ["RE", 0.5], ["FA", 0.5], ["SI", 0.5], ["LA", 0.5], ["SOL", 1], ["SI", 2], ["DO", 0.5], ["DO", 0.5], ["DO@", 2], ["LA", 0.5], ["FA", 0.5], ["SOL", 2], 
["MI", 0.5], ["DO", 0.5], ["FA", 1], ["SOL", 1], ["LA", 1], ["SOL", 1], ["DO", 0.5], ["DO", 0.5], ["DO@", 2], ["LA", 0.5], ["FA", 0.5], ["SOL", 2], ["MI", 0.5], ["DO", 0.5], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 2]]

HIMNO = [["RE", 1], ["RE", 1], ["MI", 1], ["DO", 1.5], ["RE", 1.5], ["MI", 1], ["FA", 1], ["FA", 1], ["SOL", 1], ["FA", 1.5], ["MI", 0.5], ["RE", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["RE", 3], ["RE", 1], ["RE", 1],
["MI", 1], ["DO", 1.5], ["RE", 0.5], ["MI", 1], ["FA", 1], ["FA", 1], ["SOL", 1], ["FA", 1.5], ["MI", 0.5], ["RE", 1], ["MI", 1], ["RE", 1], ["DO", 1], ["RE", 3], ["LA", 1], ["LA", 1], ["LA", 1], ["RE", 1.5],
["SOL", 0.5], ["FA", 1], ["SOL", 1], ["SOL", 1], ["SOL", 1], ["SOL", 1.5], ["FA", 0.5], ["MI", 1], ["FA", 1], ["SOL", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["FA", 1.5], ["SOL", 0.5], ["LA", 1], ["SI", 0.5],
["SOL", 0.5], ["FA", 1], ["MI", 1], ["RE", 3]]

TITANIC = [["FA", 1.5], ["FA", 0.5], ["FA", 1], ["FA", 1], ["MI", 1], ["FA", 1], ["SILENCIO", 1], ["MI", 1], ["MI", 1], ["FA", 1], ["SILENCIO", 1], ["SOL", 2], ["LA", 2], ["SOL", 1], ["FA", 1.5], ["FA", 0.5], ["FA", 1], 
["FA", 1], ["MI", 1], ["FA", 2], ["FA", 1], ["DO", 2], ["SILENCIO", 1], ["FA", 4], ["SOL", 3], ["DO", 1], ["DO@", 2], ["SI", 1], ["LA", 1], ["SOL", 2], ["LA", 1], ["SI", 1], ["LA", 2], ["SOL", 1], ["FA", 1], ["MI", 1],
["FA", 2], ["MI", 1], ["MI", 1], ["FA", 2], ["FA", 1], ["DO", 2], ["SILENCIO", 1.5], ["FA", 4], ["SOL", 3], ["DO", 1], ["DO@", 2], ["SI", 1], ["LA", 1], ["SOL", 2], ["LA", 1], ["SI", 1], ["LA", 2], ["SOL", 1], ["FA", 1], ["MI", 1],
["FA", 2], ["MI", 1], ["MI", 1], ["FA", 2], ["SOL", 1], ["LA", 2], ["SOL", 1], ["FA", 1], ["FA", 2]]

CAN = [["DO", 2], ["RE", 0.5], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["SOL", 1], ["SOL", 1], ["SOL", 0.5], ["LA", 0.5], ["MI", 0.5], ["FA", 0.5], ["RE", 1], ["RE", 1], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5],
["DO", 0.5], ["DO@", 0.5], ["SI", 0.5], ["LA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 2], ["RE", 0.5], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["SOL", 1], ["SOL", 1], ["SOL", 0.5], ["LA", 0.5], 
["MI", 0.5], ["FA", 0.5], ["RE", 1], ["RE", 1], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 0.5], ["SOL", 0.5], ["RE", 0.5], ["MI", 0.5], ["DO", 1], ["SOL", 1], ["DO", 2], ["RE", 0.5], ["RE", 0.5], ["FA", 0.5], 
["MI", 0.5], ["RE", 0.5], ["SOL", 1], ["SOL", 1], ["SOL", 0.5], ["LA", 0.5], ["MI", 0.5], ["FA", 0.5], ["RE", 1], ["RE", 1], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 0.5], ["DO@", 0.5], ["SI", 0.5], ["LA", 0.5], 
["SOL", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 2], ["RE", 0.5], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["SOL", 1], ["SOL", 1], ["SOL", 0.5], ["LA", 0.5], 
["MI", 0.5], ["FA", 0.5], ["RE", 1], ["RE", 1], ["RE", 0.5], ["FA", 0.5], ["MI", 0.5], ["RE", 0.5], ["DO", 0.5], ["SOL", 0.5], ["RE", 0.5], ["MI", 0.5], ["DO", 1], ["DO", 1]]

PAU = [["DO", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 2], ["SILENCIO", 1.5], ["DO", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 2], ["SILENCIO", 1.5], ["DO", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 1], ["MI", 1], ["DO", 1],
["MI", 1], ["RE", 2], ["SILENCIO", 1.5], ["MI", 1.5], ["RE", 0.5], ["DO", 1.5], ["DO", 0.5], ["MI", 1], ["SOL", 1], ["SOL", 0.5], ["FA", 2], ["FA", 0.5], ["MI", 0.5], ["FA", 0.5], ["SOL", 1], ["MI", 1], ["DO", 1], ["RE", 1], ["DO", 2]]

CAMPEONES = [["SOL", 1.5], ["SOL", 0.5], ["SOL", 2], ["MI", 1], ["MI", 1.5], ["MI", 0.5], ["MI", 2], ["DO", 1], ["DO", 1], ["RE", 1], ["RE", 1], ["SOL", 1], ["SOL", 1], ["DO@", 2], ["SILENCIO", 1], 
["SOL", 1.5], ["SOL", 0.5], ["SOL", 2], ["MI", 1], ["MI", 1.5], ["MI", 0.5], ["MI", 2], ["DO", 1], ["DO", 1], ["RE", 1], ["RE", 1], ["SOL", 1], ["SOL", 1], ["MI", 3]]

LCDP = [["FA", 0.5], ["SOL", 0.5], ["LA", 1], ["LA", 1], ["LA", 1], ["FA", 0.5], ["SOL", 0.5], ["LA", 1], ["LA", 1], ["LA", 1], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["RE", 1], ["SILENCIO", 1.5], 
["FA", 0.5], ["SOL", 0.5], ["LA", 1], ["LA", 1], ["LA", 1], ["FA", 0.5], ["SOL", 0.5], ["LA", 1], ["LA", 1], ["LA", 1], ["FA", 1], ["SOL", 0.5], ["LA", 1], ["RE", 1], ["SILENCIO", 1.5], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["MI", 0.5],
["MI", 1], ["RE", 3], ["SILENCIO", 1], ["DO", 0.5], ["RE", 1], ["RE", 1.5], ["SILENCIO", 1], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["MI", 0.5], ["MI", 1], ["RE", 3], ["SILENCIO", 1], ["RE", 1.5], ["MI", 0.5], ["FA", 1],
["SOL", 1], ["MI", 1.5], ["DO", 0.5], ["MI", 0.5], ["RE", 0.5], ["RE", 1]]

TETRIS = [["SI", 1], ["SOL", 0.5], ["LA", 0.5], ["SI", 1], ["LA", 0.5], ["SOL", 0.5], ["MI", 1], ["MI", 0.5], ["LA", 0.5], ["DO@", 1], ["SI", 0.5], ["LA", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SI", 1], ["DO@", 1],
["LA", 1], ["MI", 1], ["MI", 1], ["SILENCIO", 1], ["FA", 1], ["LA", 0.5], ["DO@", 1], ["SI", 0.5], ["LA", 0.5], ["SOL", 1.5], ["MI", 0.5], ["SOL", 1], ["FA", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["LA", 0.5], 
["SI", 0.5], ["SOL", 0.5], ["DO@", 0.5], ["SOL", 0.5], ["LA", 0.5], ["MI", 0.5], ["MI", 1], ["MI", 1]]

OZ = [["DO", 2], ["DO@", 2], ["SI", 1], ["SOL", 0.5], ["LA", 0.5], ["SI", 1], ["DO@", 1], ["DO", 2], ["LA", 2], ["SOL", 2], ["SILENCIO", 1], ["DO", 2], ["FA", 2], ["MI", 1], ["DO", 0.5], ["RE", 0.5], ["MI", 1], ["FA", 1],
["RE", 1], ["DO", 1], ["RE", 0.5], ["DO", 0.5], ["RE", 1], ["MI", 1], ["DO", 2], ["SILENCIO", 1.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5],
["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["LA", 3], ["DO", 2], ["DO@", 2], ["SI", 1], ["SOL", 0.5], ["LA", 0.5], ["SI", 1], ["DO@", 1], ["DO", 2], ["LA", 2], ["SOL", 2],
["SILENCIO", 1], ["DO", 2], ["FA", 2], ["MI", 1], ["DO", 0.5], ["RE", 0.5], ["MI", 1], ["FA", 1], ["RE", 1], ["DO", 1], ["RE", 0.5], ["DO", 0.5], ["RE", 1], ["MI", 1], ["DO", 2], ["SILENCIO", 1.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5],
["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 0.5], ["SOL", 0.5], ["MI", 1], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["FA", 0.5], ["SOL", 0.5], ["LA", 0.5], ["SI", 0.5], ["DO@", 4]]

ESCALA = [["DO", 1], ["RE", 1], ["MI", 1], ["FA", 1], ["SOL", 1], ["LA", 1], ["SI", 1], ["DO@", 1], ["SI", 1], ["LA", 1], ["SOL", 1], ["FA", 1], ["MI", 1], ["RE", 1], ["DO", 1]]

PRUEBA = [["DO", 1], ["RE", 1]]

tonePin = 0

def delay(delayTime):
    time.sleep(delayTime/1000.0)

def tone(unused, freq, length, msg):
    print(msg)
    winsound.Beep(int(min(max(freq,28),32766)),int(length))


def Frecuencia(nota):
    if(nota == "DO"):
        return 523.25
    elif(nota == "RE"):
        return 587.33
    elif(nota == "MI"):
        return 659.26
    elif(nota == "FA"):
        return 698.56
    elif(nota == "SOL"):
        return 783.99
    elif(nota == "LA"):
        return 880
    elif(nota == "SI"):
        return 987.77
    elif(nota == "DO@"):
        return 1046.50


def Tiempo(tp):
    if(tp == 1):
        return 231.480833333
    elif(tp == 2):
        return 462.961666667
    elif(tp == 3):
        return 694.4425
    elif(tp == 0.5):
        return 115.740416667
    elif(tp == 1.5):
        return 347.22125
    elif(tp == 4):
        return 925.923333334

def presentacio():
    engine.say("Bienvenido a Saimon Blaind Gueims. Para saber como se juega ve a la opción TUTORIAL pulsando la tecla 1")
    engine.say("Para poder jugar directamente ve a la opción JUGAR pulsando la tecla 2")
    engine.say("Si quieres jugar en formato aleatorio donde te saldrán 20 notas al azar y tendrás que acertar ve a la opción ALEATORIO pulsando la tecla 3")
    engine.say("Si quieres poner la pantalla completamente negra para saber como juega una persona con discapacidad visual pulsa en el botón SIN MENÚ")
    engine.say("Si quieres volver a oir esta información pulsa la tecla 4")
    engine.say("Para no causar interferencias, es mejor quitar todos los soportes técnicos")
    engine.runAndWait()

def main():
    engine.say("Para saltarte la explicación pulsa la tecla Q sino pulsa P")
    engine.runAndWait()
    while True:
        if keyboard.is_pressed('P'):
            presentacio()
            MenuVista()
            break;
        elif keyboard.is_pressed('Q'):
            MenuVista()
            break;

def MenuVista():
    raiz = Tk()
    raiz.title("Simon Blind Game")
    raiz.geometry("275x275")
    et = Label(raiz, text="BIENVENIDO")
    et.pack()
    et1 = Label(raiz, text="")
    et1.pack()
    boto1 = Button(raiz, text="TUTORIAL", command=tutorial)
    boto1.pack()
    et2 = Label(raiz, text="")
    et2.pack()
    boto2 = Button(raiz, text="JUGAR", command=lambda: empezarVista(raiz))
    boto2.pack()
    et3 = Label(raiz, text="")
    et3.pack()
    boto3 = Button(raiz, text="ALEATORIO", command=construir)
    boto3.pack()
    et4 = Label(raiz, text="")
    et4.pack()
    boto4 = Button(raiz, text="SIN MENÚ", command=lambda: MenuCiego(et, et1, et2, et3, et4, boto1, boto2, boto3, boto4, raiz))
    boto4.pack()
    raiz.bind("<1>", lambda x: tutorial())
    raiz.bind("<2>", lambda y: empezarVista(raiz))
    raiz.bind("<3>", lambda z: construir())
    raiz.bind("<4>", lambda a: presentacio())
    #raiz.configure(bg='white')
    raiz.mainloop()

def MenuVista2(e, e1, e2, e3, e4, b1, b2, b3, b4, raiz):
    e.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    raiz.title("Simon Blind Game")
    raiz.geometry("275x275")
    et = Label(raiz, text="BIENVENIDO")
    et.pack()
    et1 = Label(raiz, text="")
    et1.pack()
    boto1 = Button(raiz, text="TUTORIAL", command=tutorial)
    boto1.pack()
    et2 = Label(raiz, text="")
    et2.pack()
    boto2 = Button(raiz, text="JUGAR", command=lambda: empezarVista(raiz))
    boto2.pack()
    et3 = Label(raiz, text="")
    et3.pack()
    boto3 = Button(raiz, text="ALEATORIO", command=construir)
    boto3.pack()
    et4 = Label(raiz, text="")
    et4.pack()
    boto4 = Button(raiz, text="SIN MENU", command=lambda: MenuCiego(et, et1, et2, et3, et4, boto1, boto2, boto3, boto4, raiz))
    boto4.pack()
    raiz.bind("<1>", lambda x: tutorial())
    raiz.bind("<2>", lambda y: empezarVista(raiz))
    raiz.bind("<3>", lambda z: construir())
    raiz.bind("<4>", lambda a: presentacio())
    raiz.configure(bg='SystemButtonFace')
    raiz.mainloop()

def MenuCiego(e, e1, e2, e3, e4, b1, b2, b3, b4, raiz):
    e.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    raiz.title("Simon Blind Game")
    raiz.geometry("275x275")
    eti = Label(raiz, text="BIENVENIDO", bg='black')
    eti.pack()
    eti1 = Label(raiz, text="", bg='black')
    eti1.pack()
    bto1 = Button(raiz, text="TUTORIAL", command=tutorial, bg='black')
    bto1.pack()
    eti2 = Label(raiz, text="", bg='black')
    eti2.pack()
    bto2 = Button(raiz, text="JUGAR", command=lambda: empezarCiego(raiz), bg='black')
    bto2.pack()
    eti3 = Label(raiz, text="", bg='black')
    eti3.pack()
    bto3 = Button(raiz, text="ALEATORIO", command=construir, bg='black')
    bto3.pack()
    eti4 = Label(raiz, text="", bg='black')
    eti4.pack()
    bto4 = Button(raiz, text="CON MENU", command=lambda: MenuVista2(eti, eti1, eti2, eti3, eti4, bto1, bto2, bto3, bto4, raiz), bg='black')
    bto4.pack()
    raiz.bind("<1>", lambda x: tutorial())
    raiz.bind("<2>", lambda y: empezarCiego(raiz))
    raiz.bind("<3>", lambda z: construir())
    raiz.bind("<4>", lambda a: presentacio())
    raiz.configure(bg='black')
    raiz.mainloop()

def MenuCiego2():
    raiz = Tk()
    raiz.title("Simon Blind Game")
    raiz.geometry("275x275")
    eti = Label(raiz, text="BIENVENIDO", bg='black')
    eti.pack()
    eti1 = Label(raiz, text="", bg='black')
    eti1.pack()
    bto1 = Button(raiz, text="TUTORIAL", command=tutorial, bg='black')
    bto1.pack()
    eti2 = Label(raiz, text="", bg='black')
    eti2.pack()
    bto2 = Button(raiz, text="JUGAR", command=lambda: empezarCiego(raiz), bg='black')
    bto2.pack()
    eti3 = Label(raiz, text="", bg='black')
    eti3.pack()
    bto3 = Button(raiz, text="ALEATORIO", command=construir, bg='black')
    bto3.pack()
    eti4 = Label(raiz, text="", bg='black')
    eti4.pack()
    bto4 = Button(raiz, text="CON MENU", command=lambda: MenuVista2(eti, eti1, eti2, eti3, eti4, bto1, bto2, bto3, bto4, raiz), bg='black')
    bto4.pack()
    raiz.bind("<1>", lambda x: tutorial())
    raiz.bind("<2>", lambda y: empezarCiego(raiz))
    raiz.bind("<3>", lambda z: construir())
    raiz.bind("<4>", lambda a: presentacio())
    raiz.configure(bg='black')
    raiz.mainloop()

def tutorial():
    engine.say("Bienvenido al tutorial. El juego se basará en hacer una canción mediante las teclas de tu ordenador")
    engine.say("En primer lugar vamos a saber cuales son las teclas y tú las tendrás que pulsar")
    engine.say("Primero escucha la nota y luego púlsala")
    engine.say("La nota DO será la tecla de la letra A")
    engine.runAndWait()
    tone(tonePin, Frecuencia("DO"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('A'):
            tone(tonePin, Frecuencia("DO"), Tiempo(2), "")
            break
    engine.say("La nota RE será la tecla de la letra S")
    engine.runAndWait()
    tone(tonePin, Frecuencia("RE"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('S'):
            tone(tonePin, Frecuencia("RE"), Tiempo(2), "")
            break
    engine.say("La nota MI será la tecla de la letra D")
    engine.runAndWait()
    tone(tonePin, Frecuencia("MI"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('D'):
            tone(tonePin, Frecuencia("MI"), Tiempo(2), "")
            break
    engine.say("La nota FA será la tecla de la letra F")
    engine.runAndWait()
    tone(tonePin, Frecuencia("FA"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('F'):
            tone(tonePin, Frecuencia("FA"), Tiempo(2), "")
            break
    engine.say("La nota SOL será la tecla de la letra J")
    engine.runAndWait()
    tone(tonePin, Frecuencia("SOL"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('J'):
            tone(tonePin, Frecuencia("SOL"), Tiempo(2), "")
            break
    engine.say("La nota LA será la tecla de la letra K")
    engine.runAndWait()
    tone(tonePin, Frecuencia("LA"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('K'):
            tone(tonePin, Frecuencia("LA"), Tiempo(2), "")
            break
    engine.say("La nota SI será la tecla de la letra L")
    engine.runAndWait()
    tone(tonePin, Frecuencia("SI"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('L'):
            tone(tonePin, Frecuencia("SI"), Tiempo(2), "")
            break
    engine.say("La nota DO alto será la tecla Ñ")
    engine.runAndWait()
    tone(tonePin, Frecuencia("DO@"), Tiempo(2), "")
    while True:  
        if keyboard.is_pressed('Ñ'):
            tone(tonePin, Frecuencia("DO@"), Tiempo(2), "")
            break
    engine.say("¡Muy Bien!")
    engine.say("La sistemática del juego será muy parecida al juego del Simon. Se oirá primero una nota y el jugador tendrá que repetirla.")
    engine.say("Luego sonarán dos notas y el jugador tendrá que pulsar las dos teclas del ordenador correctas donde la primera será la tecla que ha sonado anteriormente y así sucesivamente hasta el final de la cancion")
    engine.say("Si te equivocas con las notas oirás este sonido")
    engine.runAndWait()
    playsound.playsound("megaman.mp3")
    engine.say("Solo tendrás tres vidas durante toda la canción")
    engine.say("Si las gastas el juego acabará y oirás el sonido siguiente")
    engine.runAndWait()
    playsound.playsound("perder.mp3")
    engine.say("Si consigues hacer toda la cancion el sonido será de victoria")
    engine.runAndWait()
    playsound.playsound("ganar.mp3")
    engine.say("Hagamos una partida de prueba con la escala musical para concluir")
    engine.runAndWait()
    sonido(ESCALA, 0)
    engine.say("¡Enhorabuena!")
    engine.say("Ya estás preparado para empezar")
    engine.say("¡Mucha suerte!")
    engine.runAndWait()

def NotasAl(num):
    if(num == 1):
        return "DO"
    elif(num == 2):
        return "RE"
    elif(num == 3):
        return "MI"
    elif(num == 4):
        return "FA"
    elif(num == 5):
        return "SOL"
    elif(num == 6):
        return "LA"
    elif(num == 7):
        return "SI"
    elif(num == 8):
        return "DO@"

def construir():
    ALEATORIO = []
    for i in range(20):
        conf = []
        nota = NotasAl(random.randint(1,8))
        tiempo = random.randint(1,5)
        if tiempo == 4:
            tiempo = 0.5
        elif tiempo == 5:
            tiempo = 1.5
        conf.append(nota)
        conf.append(tiempo)
        ALEATORIO.append(conf)
        i = i + 1
    sonido(ALEATORIO, 0)
    
niveles = []

def salirVista(r):
    niveles.clear()
    r.destroy()
    MenuVista()

def salirCiego(r):
    niveles.clear()
    r.destroy()
    MenuCiego2()

def empezarVista(r):
    nivel = 1
    for i in range(len(desbloqueo)):
        if (desbloqueo[i]):
            i = i + 1
        else:
            nivel = i
            break
    engine.say("Para jugar los niveles se irán desbloqueando si consigues completar el nivel anterior")
    engine.say("El último nivel desbloqueado es el {}".format(nivel))
    engine.say("Si quieres volver atrás pulsa el botón esqueip")
    engine.say("¡Buena suerte!")
    engine.runAndWait()
    idx = 1
    r.destroy()
    raiz2 = Tk()
    raiz2.title("Simon Blind Game")
    raiz2.geometry("520x480")
    Label(raiz2, text="JUGAR").pack()
    nivel1 = Button(raiz2, text="QUAN LES OQUES VAN AL CAMP", command=lambda: sonido(PRUEBA, 1))
    nivel1.pack()
    niveles.append(nivel1)
    nivel2 = Button(raiz2, text="CAMPEONES OÉ OÉ", command=lambda: sonido(CAMPEONES, 2))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel2.pack()
    niveles.append(nivel2)
    nivel3 = Button(raiz2, text="JO VULL LA PAU", command=lambda: sonido(PAU, 3))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel3.pack()
    niveles.append(nivel3)
    nivel4 = Button(raiz2, text="HIMNO DE LA ALEGRÍA", command=lambda: sonido(HDLA, 4))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel4.pack()
    niveles.append(nivel4)
    nivel5 = Button(raiz2, text="EL CARAGOL", command=lambda: sonido(CARAGOL, 5))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel5.pack()
    niveles.append(nivel5)
    nivel6 = Button(raiz2, text="SONRISAS Y LÁGRIMAS", command=lambda: sonido(SYL, 6))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel6.pack()
    niveles.append(nivel6)
    nivel7 = Button(raiz2, text="OH SUSANA", command=lambda: sonido(SUSANA, 7))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel7.pack()
    niveles.append(nivel7)
    nivel8 = Button(raiz2, text="PIRATAS DEL CARIBE", command=lambda: sonido(PDC, 8))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel8.pack()
    niveles.append(nivel8)
    nivel9 = Button(raiz2, text="CANCIÓN DE CUNA", command=lambda: sonido(NANA, 9))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel9.pack()
    niveles.append(nivel9)
    nivel10 = Button(raiz2, text="GOD SAVE THE QUEEN", command=lambda: sonido(HIMNO, 10))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel10.pack()
    niveles.append(nivel10)
    nivel11 = Button(raiz2, text="TITANIC", command=lambda: sonido(TITANIC, 11))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel11.pack()
    niveles.append(nivel11)
    nivel12 = Button(raiz2, text="CAN CAN", command=lambda: sonido(CAN, 12))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel12.pack()
    niveles.append(nivel12)
    nivel13 = Button(raiz2, text="LA CASA DE PAPEL", command=lambda: sonido(LCDP, 13))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel13.pack()
    niveles.append(nivel13)
    nivel14 = Button(raiz2, text="TETRIS", command=lambda: sonido(TETRIS, 14))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel14.pack()
    niveles.append(nivel14)
    nivel15 = Button(raiz2, text="OVER THE RAINBOW", command=lambda: sonido(OZ, 15))
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel15.pack()
    niveles.append(nivel15)
    raiz2.bind("<Escape>", lambda x: salirVista(raiz2))
    raiz2.mainloop()


def empezarCiego(r):
    engine.say("Para jugar los niveles se irán desbloqueando si consigues completar el nivel anterior")
    engine.say("Si quieres volver atrás pulsa el botón esqueip")
    engine.say("¡Buena suerte!")
    engine.runAndWait()
    idx = 1
    r.destroy()
    raiz2 = Tk()
    raiz2.title("Simon Blind Game")
    raiz2.geometry("520x480")
    Label(raiz2, text="JUGAR", bg='black').pack()
    nivel1 = Button(raiz2, text="QUAN LES OQUES VAN AL CAMP", command=lambda: sonido(QLOVAC, 1), bg='black')
    nivel1.pack()
    niveles.append(nivel1)
    nivel2 = Button(raiz2, text="CAMPEONES OÉ OÉ", command=lambda: sonido(CAMPEONES, 2), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel2.pack()
    niveles.append(nivel2)
    nivel3 = Button(raiz2, text="JO VULL LA PAU", command=lambda: sonido(PAU, 3), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel3.pack()
    niveles.append(nivel3)
    nivel4 = Button(raiz2, text="HIMNO DE LA ALEGRÍA", command=lambda: sonido(HDLA, 4), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel4.pack()
    niveles.append(nivel4)
    nivel5 = Button(raiz2, text="EL CARAGOL", command=lambda: sonido(CARAGOL, 5), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel5.pack()
    niveles.append(nivel5)
    nivel6 = Button(raiz2, text="SONRISAS Y LÁGRIMAS", command=lambda: sonido(SYL, 6), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel6.pack()
    niveles.append(nivel6)
    nivel7 = Button(raiz2, text="OH SUSANA", command=lambda: sonido(SUSANA, 7), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel7.pack()
    niveles.append(nivel7)
    nivel8 = Button(raiz2, text="PIRATAS DEL CARIBE", command=lambda: sonido(PDC, 8), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel8.pack()
    niveles.append(nivel8)
    nivel9 = Button(raiz2, text="CANCIÓN DE CUNA", command=lambda: sonido(NANA, 9), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel9.pack()
    niveles.append(nivel9)
    nivel10 = Button(raiz2, text="GOD SAVE THE QUEEN", command=lambda: sonido(HIMNO, 10), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel10.pack()
    niveles.append(nivel10)
    nivel11 = Button(raiz2, text="TITANIC", command=lambda: sonido(TITANIC, 11), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel11.pack()
    niveles.append(nivel11)
    nivel12 = Button(raiz2, text="CAN CAN", command=lambda: sonido(CAN, 12), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel12.pack()
    niveles.append(nivel12)
    nivel13 = Button(raiz2, text="LA CASA DE PAPEL", command=lambda: sonido(LCDP, 13), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel13.pack()
    niveles.append(nivel13)
    nivel14 = Button(raiz2, text="TETRIS", command=lambda: sonido(TETRIS, 14), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel14.pack()
    niveles.append(nivel14)
    nivel15 = Button(raiz2, text="OVER THE RAINBOW", command=lambda: sonido(OZ, 15), bg='black')
    if(desbloqueo[idx]):
        idx = idx + 1
        nivel15.pack()
    niveles.append(nivel15)
    raiz2.bind("<Escape>", lambda x: salirCiego(raiz2))
    raiz2.configure(bg='black')
    raiz2.mainloop()

def sonido(Cancion, nivel):
    vidas = 3
    i = 0
    while i < len(Cancion) and vidas != 0:
        fallo = False
        j = 0
        esperar = 0 
        while j <= i:   
            if(Cancion[j][0] == "SILENCIO"):
                delay(Tiempo(Cancion[j][1] * 2))
            else:
                tone(tonePin, Frecuencia(Cancion[j][0]), Tiempo(Cancion[j][1]), "Nota: {}, Tiempo: {}".format(Cancion[j][0], Cancion[j][1]))   
            j = j + 1
        while esperar <= i and fallo == False:
            if(Cancion[esperar][0] == "SILENCIO"):
                esperar = esperar + 1
            elif keyboard.is_pressed('A'):
                if ("DO" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("DO"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('A'):
                    True
            elif keyboard.is_pressed('S'):
                if ("RE" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("RE"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('S'):
                    True
            elif keyboard.is_pressed('D'):
                if ("MI" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("MI"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('D'):
                    True
            elif keyboard.is_pressed('F'):
                if ("FA" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("FA"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('F'):
                    True
            elif keyboard.is_pressed('J'):
                if ("SOL" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("SOL"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('J'):
                    True
            elif keyboard.is_pressed('K'):
                if ("LA" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("LA"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('K'):
                    True
            elif keyboard.is_pressed('L'):
                if ("SI" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("SI"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('L'):
                    True
            elif keyboard.is_pressed('Ñ'):
                if ("DO@" != Cancion[esperar][0]):
                    playsound.playsound("megaman.mp3")
                    fallo = True
                else:
                    tone(tonePin, Frecuencia("DO@"), Tiempo(Cancion[esperar][1]), "")  
                    esperar = esperar + 1
                while keyboard.is_pressed('Ñ'):
                    True
        delay(500)
        if (fallo):
            i = i - 1
            vidas = vidas - 1
        i = i + 1
    if vidas == 0:
        playsound.playsound("perder.mp3")
    else:
        if(nivel != len(niveles) and desbloqueo[nivel] == False):
            bn = niveles[nivel]
            bn.pack()
            desbloqueo[nivel] = True
        playsound.playsound("ganar.mp3")

if __name__ == "__main__":
    main()