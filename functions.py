import settingspage as stng

def impDados():
    '''
    Print in the console each one of the Selected Filter (settingspage.py)
    '''
    print("Numeros de Questões: {}".format(stng.NQuest))

    print("01 - {}".format(stng.check01.get()))
    print("02 - {}".format(stng.check02.get()))
    print("03 - {}".format(stng.check03.get()))
    print("04 - {}".format(stng.check04.get()))
    print("05 - {}".format(stng.check05.get()))
    print("06 - {}".format(stng.check06.get()))
    print("07 - {}".format(stng.check07.get()))
    print("08 - {}".format(stng.check08.get()))
    print("09 - {}".format(stng.check09.get()))



def getDados() -> []:
    '''
    Return all the Configuration from the Filter (settingspage.py))
    '''
    dados = []
    dados.append(stng.NQuest.get())

    dados.append(stng.check01.get())
    dados.append(stng.check02.get())
    dados.append(stng.check03.get())

    dados.append(stng.check04.get())
    dados.append(stng.check05.get())
    dados.append(stng.check06.get())

    dados.append(stng.check07.get())
    dados.append(stng.check08.get())
    dados.append(stng.check09.get())

    return(dados)