from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Calculator")
root.geometry("410x500")
root.resizable(False, False)

def add_to_display(x):
    global display
    global previous_action
    y = display.get()
    if y == "0":
        display.set(x)
    elif previous_action == 1:
        display.set(x)
    else:
        display.set(y + x)
    previous_action = 0

def add_virgula(a):
    b = a + "."
    display.set(b)


def clear():
    global display
    display.set("0")
    global previous_action
    global c
    c = 0
    previous_action = 0


#Sempre que apertado o botão liga
#4 casos possíveis:
#- O botao estar desligado e o display=0//Após ligar: Se nenhum numero for passado ao display o resultado será = 0
#- O botao estar desligado e o display!=0
#= O botao estar ligado e o display=0
#- O botao estar ligado e o display !=0

def bot_add(a):
    global num_a_add
    global previous_action
    global c
    if c == 0 and a == "0":
        num_a_add = a
    elif c == 0 and a != "0":
        num_a_add = a
    elif c == 1 and a == "0":
        pass
    elif c == 1 and a != "0":
        somar(num_a_add, a)
        num_a_add = somar(num_a_add, a)
        display.set(str(ale(num_a_add)))
    c = 1
    previous_action = 1

def bot_sub(a):
    global num_a_sub
    global previous_action
    global c
    if c == 0 and a == "0":
        num_a_sub = a
    elif c == 0 and a != "0":
        num_a_sub = a
    elif c == 2 and a == "0":
        pass
    elif c == 2 and a != "0":
        subtrair(a, num_a_sub)
        num_a_sub = subtrair(a, num_a_sub)
        display.set(str(ale(num_a_sub)))
    c = 2
    previous_action = 1

def bot_mult(a):
    global num_a_multi
    global previous_action
    global c
    if c == 0 and a == "0":
        num_a_multi = a
    elif c == 0 and a != "0":
        num_a_multi = a
    elif c == 3 and a == "0":
        pass
    elif c == 3 and a != "0":
        multipliar(a, num_a_multi)
        num_a_multi = multipliar(a, num_a_multi)
        display.set(str(ale(num_a_multi)))
    c = 3
    previous_action = 1

def bot_divi(a):
    global num_a_divi
    global previous_action
    global c
    if c == 0 and a == "0":
        num_a_divi = a
    elif c == 0 and a != "0":
        num_a_divi = a
    elif c == 4 and a == "0":
        pass
    elif c == 4 and a != "0":
        num_a_divi = dividir(num_a_divi, a)
        display.set(str(ale(num_a_divi)))
    c = 4
    previous_action = 1


def somar(x, y):
    global result
    result = float(x) + float(y)
    return result

def subtrair(x, y):
    global result
    result = float(x) - float(y)
    return result

def multipliar(x, y):
    global result
    result = float(x) * float(y)
    return result

def dividir(x, y):
    global result
    result = round(float(x) / float(y), 7)
    return result

def ale(z):
    x = float(z) - int(z)
    if x == 0:
        return int(z)
    else:
        return float(z)


def bot_igual_a(b):
    global c
    if c == 1:
        x = round(ale(somar(num_a_add, b)), 7)
        display.set(str(x))
    elif c == 2:
        x = round(ale(subtrair(num_a_sub, b)))
        display.set(str(x))
    elif c == 3:
        x = round(ale(multipliar(num_a_multi, b)), 7)
        display.set(str(x))
    elif c == 4:
        x = round(ale(dividir(num_a_divi, b)), 7)
        display.set(str(x))
    else:
        pass
    c = 0




c = 0
previous_action = 0

display = StringVar()
display.set("0")
e = Label(root, width=10, height=1, textvariable=display, font=("Verdana 50"), anchor=E, bg="black", relief=SUNKEN, borderwidth=10)
e.grid(row=0, columnspan=4, column=0)


# CRIAR/DEFINIR BOTÕES

btn1 = Button(root, text="1", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("1"))
btn2 = Button(root, text="2", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("2"))
btn3 = Button(root, text="3", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("3"))
btn4 = Button(root, text="4", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("4"))
btn5 = Button(root, text="5", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("5"))
btn6 = Button(root, text="6", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("6"))
btn7 = Button(root, text="7", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("7"))
btn8 = Button(root, text="8", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("8"))
btn9 = Button(root, text="9", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_to_display("9"))
btn0 = Button(root, text="0", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, width=200, command=lambda: add_to_display("0"))
btnAC = Button(root, text="AC", fg="white", bg="#bfbfbf", font=("Verdana 15"), height=80, width=300, command=clear)
btnDivi = Button(root, text="/", fg="white", bg="#ff9933", font=("Verdana 15"), height=80, command=lambda: bot_divi(display.get()))
btnMulti = Button(root, text="X", fg="white", bg="#ff9933", font=("Verdana 15"), height=80, command=lambda: bot_mult(display.get()))
btnSub = Button(root, text="-", fg="white", bg="#ff9933", font=("Verdana 15"), height=80, command=lambda: bot_sub(display.get()))
btnSoma = Button(root, text="+", fg="white", bg="#ff9933", font=("Verdana 15"), height=80, command=lambda: bot_add(display.get()))
btnResult = Button(root, text="=", fg="white", bg="#ff9933", font=("Verdana 15"), height=80, command=lambda: bot_igual_a(display.get()))
btnVirgu = Button(root, text=".", fg="white", bg="#4d4d4d", font=("Verdana 15"), height=80, command=lambda: add_virgula(display.get()))

btnAC.grid(row=1, columnspan=3, column=0)
btnDivi.grid(row=1, column=3)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btnMulti.grid(row=2, column=3)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btnSub.grid(row=3, column=3)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btnSoma.grid(row=4, column=3)
btn0.grid(row=5, column=0, columnspan=2)
btnVirgu.grid(row=5, column=2)
btnResult.grid(row=5, column=3)

root.mainloop()
