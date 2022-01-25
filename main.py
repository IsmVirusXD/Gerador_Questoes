#Package
import functions as func
import tkinter as tk

#Native
import settingspage

'''
Main Page
'''

if __name__ == '__main__':

    '''
    Inicialização do App
    '''

    app = tk.Tk()
    app.title("Gerador de Questões - URI")
    app.geometry("350x400")
    app.configure()

    settingspage.main(app)  #Pagina do Filtro
    
    app.mainloop()
