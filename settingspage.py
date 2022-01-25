import functions as func
import tkinter as tk

'''
In this Page, we have all the configuration to the front end that the Page is going to need
that means this page only purpose is to set the Filter to the Backend do the job

'''


def main(app: tk):
    '''
    Variaveis
    '''
    # String -> Get the Number of Questions
    global NQuest
    NQuest = tk.StringVar()

    # Boolean -> Checkbox to the Filter
    global check01  # 01 -> Iniciante
    check01 = tk.BooleanVar()

    global check02  # 02 -> AD-HOC
    check02 = tk.BooleanVar()

    global check03  # 03 -> Strings
    check03 = tk.BooleanVar()

    global check04  # 04 -> Estruturas e Bibliotecas
    check04 = tk.BooleanVar()

    global check05  # 05 -> Matemática
    check05 = tk.BooleanVar()

    global check06  # 06 -> Paradigmas
    check06 = tk.BooleanVar()

    global check07  # 07 -> Grafos
    check07 = tk.BooleanVar()

    global check08  # 08 -> Geometria Computacional
    check08 = tk.BooleanVar()

    global check09  # 09 -> SQL
    check09 = tk.BooleanVar()

    '''
    Configurações da Pagaina
    '''

    tk.Label(app, text="Configurações do Gerador:",
             anchor='w').place(x=20, y=10, w=200, h=20)

    # -> Setting Number of Questions
    tk.Label(app, text="Numero de Questões:",
             anchor='w').place(x=20, y=50, w=150, h=20)
    tk.Entry(app, textvariable=NQuest).place(x=150, y=50, w=40, h=20)

    # -> Checkbox Layout
    tk.Label(app, text="Assuntos: ", anchor='w').place(
        x=20, y=100, w=150, h=20)
    fr_quadro = tk.Frame(app, borderwidth=1, relief='solid')
    fr_quadro.place(x=20, y=120, width=310, height=100)

    # Checkbox -> Settings
    cb_01 = tk.Checkbutton(fr_quadro, text='Iniciante', anchor='w',
                           variable=check01, onvalue=True, offvalue=False)

    cb_02 = tk.Checkbutton(fr_quadro, text='AD-Hoc', anchor='w',
                           variable=check02, onvalue=True, offvalue=False)

    cb_03 = tk.Checkbutton(fr_quadro, text='String', anchor='w',
                           variable=check03, onvalue=True, offvalue=False)

    cb_04 = tk.Checkbutton(fr_quadro, text='Estruturas', anchor='w',
                           variable=check04, onvalue=True, offvalue=False)

    cb_05 = tk.Checkbutton(fr_quadro, text='Matematica', anchor='w',
                           variable=check05, onvalue=True, offvalue=False)

    cb_06 = tk.Checkbutton(fr_quadro, text='Paradigmas', anchor='w',
                           variable=check06, onvalue=True, offvalue=False)

    cb_07 = tk.Checkbutton(fr_quadro, text='Grafos', anchor='w',
                           variable=check07, onvalue=True, offvalue=False)

    cb_08 = tk.Checkbutton(fr_quadro, text='Geo.Compu', anchor='w',
                           variable=check08, onvalue=True, offvalue=False)

    cb_09 = tk.Checkbutton(fr_quadro, text='SQL', anchor='w',
                           variable=check09, onvalue=True, offvalue=False)

    # Checkbox -> Placing
    cb_01.place(x=0, y=10, w=100, h=20)
    cb_02.place(x=100, y=10, w=100, h=20)
    cb_03.place(x=200, y=10, w=100, h=20)
    cb_04.place(x=0, y=40, w=100, h=20)
    cb_05.place(x=100, y=40, w=100, h=20)
    cb_06.place(x=200, y=40, w=100, h=20)
    cb_07.place(x=0, y=70, w=100, h=20)
    cb_08.place(x=100, y=70, w=100, h=20)
    cb_09.place(x=200, y=70, w=100, h=20)

    # Button -> Configuration and Placing
    bt = tk.Button(app, text='Gerar Questões', command=func.impDados)
    bt.place(x=120, y=250, w=100, h=20)
