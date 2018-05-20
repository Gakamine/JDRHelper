# Créé par Antoine, le 25/04/2017 en Python 3.2
from tkinter import *
import random
Fenetre =  Tk()
Titre="Dés"
texteresultat = StringVar()
texteresultat.set("Sélectionnez un dé")
Fenetre.geometry('110x130')
Fenetre.title('Set de dés')
Resultat = Label(Fenetre, textvariable=texteresultat).pack(side=BOTTOM)
def resultat(dé):
    Resultat, texteresultat
    def inner():
        def alea():
            valeur = random.randint(0, int(dé))
            return valeur
        texteresultat.set(alea())
    return inner
Set1=Frame(Fenetre)
Set1.pack(side=TOP, fill=Y)
Set2=Frame(Fenetre)
Set2.pack(side=TOP)
Set3=Frame(Fenetre)
Set3.pack(side=TOP)
Set4=Frame(Fenetre)
Set4.pack(side=TOP)
Des100 = Button(Set1, text="100", width=6, command=resultat(100)).pack(side=LEFT)
Des20 = Button(Set1, text="20", width=6, command=resultat(20)).pack()
Des12 = Button(Set2, text="12", width=6, command=resultat(12)).pack(side=LEFT)
Des10 = Button(Set2, text="10", width=6, command=resultat(10)).pack()
Des8 = Button(Set3, text="8", width=6, command=resultat(8)).pack(side=LEFT)
Des6 = Button(Set3, text="6", width=6, command=resultat(6)).pack()
User_Choice=Spinbox(Set4, width=7 ,from_=0, to=1000)
User_Choice.pack(side=LEFT)
Drop=Button(Set4, width=5 ,text="Lancer", command=resultat(User_Choice.get())).pack()
Fenetre.resizable(False, False)
Fenetre.mainloop()
