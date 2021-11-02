from tkinter import *

app = Tk()
app.title("Gerador de Questões - URI")
app.geometry("350x400")
app.configure()

NQuest = StringVar()

check01 = BooleanVar()
check02 = BooleanVar()
check03 = BooleanVar()
check04 = BooleanVar()
check05 = BooleanVar()
check06 = BooleanVar()
check07 = BooleanVar()
check08 = BooleanVar()
check09 = BooleanVar()

def impDados():
    print("Numeros de Questões: {}".format(NQuest.get()))
    print("01 - {}".format(check01.get()))
    print("02 - {}".format(check02.get()))
    print("03 - {}".format(check03.get()))
    print("04 - {}".format(check04.get()))
    print("05 - {}".format(check05.get()))
    print("06 - {}".format(check06.get()))
    print("07 - {}".format(check07.get()))
    print("08 - {}".format(check08.get()))
    print("09 - {}".format(check09.get()))

Label(app, text="Configurações do Gerador:", anchor=W).place(x=20, y=10, w=200, h=20)

Label(app, text="Numero de Questões:", anchor=W).place(x=20, y=50, w=150, h=20)
Entry(app, textvariable=NQuest).place(x=150, y=50, w=40, h=20)


Label(app, text="Assuntos: ", anchor=W).place(x=20, y=100, w=150, h=20)

fr_quadro = Frame(app,borderwidth=1,relief='solid')
fr_quadro.place(x=20, y=120, width=310, height=100)

cb_01 = Checkbutton(fr_quadro,text='Iniciante', anchor=W, variable=check01, onvalue=True, offvalue=False)
cb_01.place(x=0, y=10, w=100, h=20)

cb_02 = Checkbutton(fr_quadro,text='AD-Hoc', anchor=W, variable=check02, onvalue=True, offvalue=False)
cb_02.place(x=100, y=10, w=100, h=20)

cb_03 = Checkbutton(fr_quadro,text='String', anchor=W, variable=check03, onvalue=True, offvalue=False)
cb_03.place(x=200, y=10, w=100, h=20)

cb_04 = Checkbutton(fr_quadro,text='Estruturas', anchor=W, variable=check04, onvalue=True, offvalue=False)
cb_04.place(x=0, y=40, w=100, h=20)

cb_05 = Checkbutton(fr_quadro,text='Matematica', anchor=W, variable=check05, onvalue=True, offvalue=False)
cb_05.place(x=100, y=40, w=100, h=20)

cb_06 = Checkbutton(fr_quadro,text='Paradigmas', anchor=W, variable=check06, onvalue=True, offvalue=False)
cb_06.place(x=200, y=40, w=100, h=20)

cb_07 = Checkbutton(fr_quadro,text='Grafos', anchor=W, variable=check07, onvalue=True, offvalue=False)
cb_07.place(x=0, y=70, w=100, h=20)

cb_08 = Checkbutton(fr_quadro,text='Geo.Compu', anchor=W, variable=check08, onvalue=True, offvalue=False)
cb_08.place(x=100, y=70, w=100, h=20)

cb_09 = Checkbutton(fr_quadro,text='SQL', anchor=W, variable=check09, onvalue=True, offvalue=False)
cb_09.place(x=200, y=70, w=100, h=20)

bt = Button(app, text='Gerar Questões', command=impDados)
bt.place(x=120, y=250, w=100, h=20)

app.mainloop()

