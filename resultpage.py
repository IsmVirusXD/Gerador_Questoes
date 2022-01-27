import functions as func
import tkinter as tk


def main():
    top = tk.Toplevel()
    top.title("Resultado da Pesquisa")

    global X    
    x = 0
    global data
    global value
    global item
    global k

    data = func.getDados()
   #value = int(data[0])

    banco_de_dados = func.getProblems(1, 2)

    label01 = tk.Label(top, text="Indice", anchor='w')
    label01.grid(row=0, column=0)

    label02 = tk.Label(top, text="Dificuldade", anchor='w')
    label02.grid(row=0, column=1)

    label03 = tk.Label(top, text="Problema", anchor='w')
    label03.grid(row=0, column=2)

    label04 = tk.Label(top, text="Link", anchor='w')
    label04.grid(row=0, column=3)


    for i in banco_de_dados:
        x = x + 1

        indice = tk.Label(top, text=i[0], anchor='w')
        indice.grid(row=x, column=0)

        name = tk.Label(top, text=i[1], anchor='w')
        name.grid(row=x, column=2, sticky = "W")

        link = tk.Label(top, text=i[2], anchor='w')
        link.grid(row=x, column=3, sticky = "W")

        difc = tk.Label(top, text=i[3], anchor='w')
        difc.grid(row=x, column=1)

