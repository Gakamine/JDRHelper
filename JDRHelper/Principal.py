# Par Antoine, le 20/02/2017 en Python 3.2
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
import pickle
import os
import webbrowser
import sys
from tkinter.constants import *
from tkinter.messagebox import *
#===============Variables=====================
imgdict={}
imgperso={}
imge={}
NbCartes=1
NbScenarios = 0
NbObjets = 0
NbPersos = 0
NbEnnemis = 0
NbPDF=0
ScenarioTitreE = {}
ScenarioContenu = {}
ScenariosPDF={}
creaperso= ["Nom","Niveau","Sexe","Origine","Métier","PV","Mana","Magie Physique","Magie Psychique","Résistance magique","Courage","Force","Adresse","Intelligence","Charisme","Attaque","Parade","Points de destin"]
creaennemis = ["Nom","Niveau","Resistance","Dégats","Bonus","Description"]
Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Adresse, Intelligence, Charisme, Attaque, Parade, Points_de_destin = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE = {},{}, {}, {}, {}, {}
ImagesObjets={}
DescriptionsObjets={}
TitresObjets={}
NbModules = 0
PathPyM = {}
Inventaires={}
#===============Fonction======================
#=====Exportation Sauvegardes====
def export():
    def ConfirmExport():
        if NameSave.get("1.0", "end-1c")!="":
            SaveName=NameSave.get("1.0", "end-1c")
            SaveF.destroy()
            global imgdict,imge,NbPersos,NbCartes,NbScenarios,NbObjets,NbEnnemis,ScenarioTitreE,ScenarioContenu,ScenariosPDF,creaperso,creaennemis,Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Adresse, Intelligence, Charisme, Attaque, Parade, Points_de_destin,NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, ImagesObjets, DescriptionsObjets, TitresObjets, NbModules,PathPyM,Inventaires,imgperso
            allvar=[imge,NbPersos,NbScenarios,NbObjets,NbEnnemis,ScenarioTitreE,ScenarioContenu,ScenariosPDF,creaperso,creaennemis,Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Adresse, Intelligence, Charisme, Attaque, Parade, Points_de_destin,NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, ImagesObjets, DescriptionsObjets, TitresObjets, NbModules,PathPyM,Inventaires,imgperso,NbPDF]
            CheminSauvegarde = open('saves/'+SaveName+'.jdr','wb')
            pickle.dump(allvar, CheminSauvegarde)
            CheminSauvegarde.close()
            webbrowser.open('saves')
        else:
            showerror("Erreur sauvegarde","Vous n'avez pas entrez un nom de sauvegarde valide.")
    SaveF=Tk()
    SaveF.title("Sauvegarder")
    NameSave=Text(SaveF, height=1)
    NameSave.pack(side=TOP)
    NameSave.insert(END,"Nommez votre sauvegarde")
    ButtonSave=Button(SaveF, text="Sauvegarder", command=ConfirmExport).pack(side=BOTTOM, fill=X)
    SaveF.resizable("false","false")
    SaveF.mainloop()
#=====Importation Sauvegardes====
def import_sauvegarde():
    global imgdict,imge,NbPersos,NbCartes,NbScenarios,NbObjets,NbEnnemis,ScenarioTitreE,ScenarioContenu,ScenariosPDF,creaperso,creaennemis,Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Adresse, Intelligence, Charisme, Attaque, Parade, Points_de_destin,NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, ImagesObjets, DescriptionsObjets, TitresObjets, NbModules,PathPyM,Inventaires,imgperso, NbPDF
    CheminImportSauvegarde = tkinter.filedialog.askopenfilename(title="Ouvrir une sauvegarde",filetypes=[('Fichiers JDR','.jdr')])
    Sauvegarde = open(CheminImportSauvegarde ,'rb')
    Saves = pickle.load(Sauvegarde)
    if NbPersos>0 or NbObjets>0 or NbScenarios>0 or NbEnnemis > 0:
        showerror("Importation Impossible", "Vous ne pouvez pas importez une sauvegarde sur une partie en cours.")
    else:
        imge=Saves[0]
        NbPersos=Saves[1]
        NbScenarios=Saves[2]
        NbObjets=Saves[3]
        NbEnnemis=Saves[4]
        ScenarioTitreE=Saves[5]
        ScenarioContenu=Saves[6]
        ScenariosPDF=Saves[7]
        creaperso=Saves[8]
        creaennemis=Saves[9]
        Nom=Saves[10]
        Niveau=Saves[11]
        Sexe=Saves[12]
        Origine=Saves[13]
        Metier=Saves[14]
        PV=Saves[15]
        Mana=Saves[16]
        Magie_Physique=Saves[17]
        Magie_Psychique=Saves[18]
        Resistance_Magique=Saves[19]
        Courage=Saves[20]
        Force=Saves[21]
        Adresse=Saves[22]
        Intelligence=Saves[23]
        Charisme=Saves[24]
        Attaque=Saves[25]
        Parade=Saves[26]
        Points_de_destin=Saves[27]
        NomE=Saves[28]
        NiveauE=Saves[29]
        ResistanceE=Saves[30]
        DegatsE=Saves[31]
        BonusE=Saves[32]
        DescriptionE=Saves[33]
        ImagesObjets=Saves[34]
        DescriptionsObjets=Saves[35]
        TitresObjets=Saves[36]
        NbModules=Saves[37]
        PathPyM=Saves[38]
        Inventaires=Saves[39]
        imgperso=Saves[40]
        NbPDF=Saves[41]
        if NbPersos>=1:
            menu2.add_separator()
        for i in range(NbPersos):
            commandPersos=GetPerso(i)
            menu2.add_command(label=Nom[i], command=commandPersos)
        if NbObjets>=1:
            menu5.add_separator()
        for i in range(NbObjets):
            commandObj=GetObj(i)
            menu5.add_command(label=TitresObjets[i], command=commandObj)
        if NbEnnemis>=1:
            menu6.add_separator()
        for i in range(NbEnnemis):
            CommandEnnemis=GetEnnemis(i)
            menu6.add_command(label=NomE[i], command=CommandEnnemis)
        if NbScenarios>=1 or NbPDF>=1:
            menu3.add_separator()
        for i in range(NbScenarios):
            CommandScenario=GetScenario(i)
            menu3.add_command(label=ScenarioTitreE[i], command=CommandScenario)
        for i in range(NbPDF):
            CommandScenarioPDF=ReadPDF(ScenariosPDF[i])
            menu3.add_command(label=ScenariosPDF[i], command=CommandScenarioPDF)
    Sauvegarde.close()
#=====Informations sur le logiciel===
def help():
    webbrowser.open('file://' + os.path.realpath('help/index.html'))
#=====Import module====
def importmodule():
    global NbModules, PathPyM
    PathPy = tkinter.filedialog.askopenfilename(title="Ouvrir un module",filetypes=[('Fichier PYTHON','.py')])
    if NbModules==0:
        menu1.add_separator()
    menu1.add_command(label=PathPy, command=runimportmodule(PathPy))
    NbModules=NbModules+1
def runimportmodule(PathPy):
    def inner():
        pyexec = sys.executable
        os.system('%s %s' % (pyexec, PathPy))
    return inner
#=====Personnages====
def perso():
    global ImagePerso, PersoImg, NbObjets, ImagesObjets, PathImgPerso
    PersoImg = PhotoImage(file='question.gif')
    PathImgPerso='question.gif'
    def imageperso():
        global PersoImg, ImagePerso, PathImgPerso
        PathImgPerso = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
        PersoImg = ImageTk.PhotoImage(file=PathImgPerso)
        ImagePerso['image']=PersoImg
    def confirmerInput(event):
        global NbPersos, Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Intelligence, Charisme, Attaque, Parade, Points_de_destin, Adresse, imgperso, PersoImg, ImagePerso
        Nom[NbPersos]=X1.get("1.0", "end-1c")
        Niveau[NbPersos]=X2.get("1.0", "end-1c")
        Sexe[NbPersos]=X3.get("1.0", "end-1c")
        Origine[NbPersos]=X4.get("1.0", "end-1c")
        Metier[NbPersos]=X5.get("1.0", "end-1c")
        PV[NbPersos]=X6.get("1.0", "end-1c")
        Mana[NbPersos]=X7.get("1.0", "end-1c")
        Magie_Physique[NbPersos]=X8.get("1.0", "end-1c")
        Magie_Psychique[NbPersos]=X9.get("1.0", "end-1c")
        Resistance_Magique[NbPersos]=X10.get("1.0", "end-1c")
        Courage[NbPersos]=X11.get("1.0", "end-1c")
        Force[NbPersos]=X12.get("1.0", "end-1c")
        Adresse[NbPersos]=X13.get("1.0", "end-1c")
        Intelligence[NbPersos]=X14.get("1.0", "end-1c")
        Charisme[NbPersos]=X15.get("1.0", "end-1c")
        Attaque[NbPersos]=X16.get("1.0", "end-1c")
        Parade[NbPersos]=X17.get("1.0", "end-1c")
        Points_de_destin[NbPersos]=X18.get("1.0", "end-1c")
        imgperso[NbPersos]=PathImgPerso
        if NbPersos==0:
            menu2.add_separator()
        CommandPerso = GetPerso(NbPersos)
        menu2.add_command(label=Nom[NbPersos], command=CommandPerso)
        NbPersos = NbPersos+1
        perso.destroy()
    def confirmer():
        global NbPersos, Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Intelligence, Charisme, Attaque, Parade, Points_de_destin, Adresse, imgperso, PersoImg, ImagePerso
        Nom[NbPersos]=X1.get("1.0", "end-1c")
        Niveau[NbPersos]=X2.get("1.0", "end-1c")
        Sexe[NbPersos]=X3.get("1.0", "end-1c")
        Origine[NbPersos]=X4.get("1.0", "end-1c")
        Metier[NbPersos]=X5.get("1.0", "end-1c")
        PV[NbPersos]=X6.get("1.0", "end-1c")
        Mana[NbPersos]=X7.get("1.0", "end-1c")
        Magie_Physique[NbPersos]=X8.get("1.0", "end-1c")
        Magie_Psychique[NbPersos]=X9.get("1.0", "end-1c")
        Resistance_Magique[NbPersos]=X10.get("1.0", "end-1c")
        Courage[NbPersos]=X11.get("1.0", "end-1c")
        Force[NbPersos]=X12.get("1.0", "end-1c")
        Adresse[NbPersos]=X13.get("1.0", "end-1c")
        Intelligence[NbPersos]=X14.get("1.0", "end-1c")
        Charisme[NbPersos]=X15.get("1.0", "end-1c")
        Attaque[NbPersos]=X16.get("1.0", "end-1c")
        Parade[NbPersos]=X17.get("1.0", "end-1c")
        Points_de_destin[NbPersos]=X18.get("1.0", "end-1c")
        imgperso[NbPersos]=PathImgPerso
        if NbPersos==0:
            menu2.add_separator()
        CommandPerso = GetPerso(NbPersos)
        menu2.add_command(label=Nom[NbPersos], command=CommandPerso)
        NbPersos = NbPersos+1
        perso.destroy()
    perso = Toplevel()
    perso.resizable('false','false')
    perso.title('Créer')
    perso.geometry('200x635')
    F1 = Frame(perso)
    F1.pack(side=TOP)
    F2 = Frame(perso)
    F2.pack(side=TOP)
    F3 = Frame(perso)
    F3.pack(side=TOP)
    F4 = Frame(perso)
    F4.pack(side=TOP)
    F5 = Frame(perso)
    F5.pack(side=TOP)
    F6 = Frame(perso)
    F6.pack(side=TOP)
    F7 = Frame(perso)
    F7.pack(side=TOP)
    F8 = Frame(perso)
    F8.pack(side=TOP)
    F9 = Frame(perso)
    F9.pack(side=TOP)
    F10 = Frame(perso)
    F10.pack(side=TOP)
    F11 = Frame(perso)
    F11.pack(side=TOP)
    F12 = Frame(perso)
    F12.pack(side=TOP)
    F13 = Frame(perso)
    F13.pack(side=TOP)
    F14 = Frame(perso)
    F14.pack(side=TOP)
    F15 = Frame(perso)
    F15.pack(side=TOP)
    F16= Frame(perso)
    F16.pack(side=TOP)
    F17 = Frame(perso)
    F17.pack(side=TOP)
    F18 = Frame(perso)
    F18.pack(side=TOP)
    F19 = Frame(perso)
    F19.pack(side=TOP)
    F20 = Frame(perso)
    F20.pack(side=TOP)
    L1= Label(F1, text=creaperso[0])
    L1.pack(side=LEFT)
    X1= Text(F1, height=1)
    X1.pack(side=RIGHT)
    L2=Label(F2, text=creaperso[1])
    L2.pack(side=LEFT)
    X2=Text(F2, height=1)
    X2.pack(side=RIGHT)
    L3=Label(F3, text=creaperso[2])
    L3.pack(side=LEFT)
    X3=Text(F3, height=1)
    X3.pack(side=RIGHT)
    L4=Label(F4,text=creaperso[3])
    L4.pack(side=LEFT)
    X4=Text(F4, height=1)
    X4.pack(side=RIGHT)
    L5=Label(F5,text=creaperso[4])
    L5.pack(side=LEFT)
    X5=Text(F5, height=1)
    X5.pack(side=RIGHT)
    L6=Label(F6,text=creaperso[5])
    L6.pack(side=LEFT)
    X6=Text(F6, height=1)
    X6.pack(side=RIGHT)
    L7=Label(F7,text=creaperso[6])
    L7.pack(side=LEFT)
    X7=Text(F7, height=1)
    X7.pack(side=RIGHT)
    L8=Label(F8,text=creaperso[7])
    L8.pack(side=LEFT)
    X8=Text(F8, height=1)
    X8.pack(side=RIGHT)
    L9=Label(F9,text=creaperso[8])
    L9.pack(side=LEFT)
    X9=Text(F9, height=1)
    X9.pack(side=RIGHT)
    L10=Label(F10,text=creaperso[9])
    L10.pack(side=LEFT)
    X10=Text(F10, height=1)
    X10.pack(side=RIGHT)
    L11=Label(F11,text=creaperso[10])
    L11.pack (side=LEFT)
    X11=Text(F11, height=1)
    X11.pack(side=RIGHT)
    L12=Label(F12,text=creaperso[11])
    L12.pack(side=LEFT)
    X12=Text(F12, height=1)
    X12.pack(side=RIGHT)
    L13=Label(F13,text=creaperso[12])
    L13.pack(side=LEFT)
    X13=Text(F13, height=1)
    X13.pack(side=RIGHT)
    L14=Label(F14,text=creaperso[13])
    L14.pack (side=LEFT)
    X14=Text(F14, height=1)
    X14.pack(side=RIGHT)
    L15=Label(F15,text=creaperso[14])
    L15.pack (side=LEFT)
    X15=Text(F15, height=1)
    X15.pack(side=RIGHT)
    L16=Label(F16,text=creaperso[15])
    L16.pack (side=LEFT)
    X16=Text(F16, height=1)
    X16.pack(side=RIGHT)
    L17=Label(F17,text=creaperso[16])
    L17.pack (side=LEFT)
    X17=Text(F17, height=1)
    X17.pack(side=RIGHT)
    L18=Label(F19,text=creaperso[17])
    L18.pack (side=LEFT)
    X18=Text(F19, height=1)
    X18.pack(side=RIGHT)
    ImagePerso=Label(perso, image=PersoImg, height='200', width='200')
    ImagePerso.pack(fill=BOTH)
    B18= Button(perso, text="Changer d'image", command=imageperso).pack(fill=X)
    B21=Button(perso,text="Confirmer", command=confirmer)
    B21.pack(side=BOTTOM, fill=X)
    perso.bind("<Return>", confirmerInput)
    perso.mainloop()
def GetPerso(NbPersos):
    global imgperso
    def inner():
        global Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Intelligence, Adresse, Charisme, Attaque, Parade, Points_de_destin, PersoImg, PersoImg, ImagePerso,NbObjets, ImagesObjets
        def confirmer():
            global PathImgPerso, Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Intelligence, Adresse, Charisme, Attaque, Parade, Points_de_destin, PersoImg, ImagePerso
            menu2.delete(Nom[NbPersos])
            Nom[NbPersos]=X1.get("1.0", "end-1c")
            Niveau[NbPersos]=X2.get("1.0", "end-1c")
            Sexe[NbPersos]=X3.get("1.0", "end-1c")
            Origine[NbPersos]=X4.get("1.0", "end-1c")
            Metier[NbPersos]=X5.get("1.0", "end-1c")
            PV[NbPersos]=X6.get("1.0", "end-1c")
            Mana[NbPersos]=X7.get("1.0", "end-1c")
            Magie_Physique[NbPersos]=X8.get("1.0", "end-1c")
            Magie_Psychique[NbPersos]=X9.get("1.0", "end-1c")
            Resistance_Magique[NbPersos]=X10.get("1.0", "end-1c")
            Courage[NbPersos]=X11.get("1.0", "end-1c")
            Force[NbPersos]=X12.get("1.0", "end-1c")
            Intelligence[NbPersos]=X13.get("1.0", "end-1c")
            Adresse[NbPersos]=X14.get("1.0", "end-1c")
            Charisme[NbPersos]=X15.get("1.0", "end-1c")
            Attaque[NbPersos]=X16.get("1.0", "end-1c")
            Parade[NbPersos]=X17.get("1.0", "end-1c")
            Points_de_destin[NbPersos]=X18.get("1.0", "end-1c")
            CommandPerso = GetPerso(NbPersos)
            imgperso[NbPersos]=PathImgPerso
            menu2.add_command(label=Nom[NbPersos], command=CommandPerso)
        def confirmerInput(event):
            global PathImgPerso, Nom, Niveau, Sexe, Origine, Metier, PV, Mana, Magie_Physique, Magie_Psychique, Resistance_Magique, Courage, Force, Intelligence, Adresse, Charisme, Attaque, Parade, Points_de_destin, PersoImg, ImagePerso
            menu2.delete(Nom[NbPersos])
            Nom[NbPersos]=X1.get("1.0", "end-1c")
            Niveau[NbPersos]=X2.get("1.0", "end-1c")
            Sexe[NbPersos]=X3.get("1.0", "end-1c")
            Origine[NbPersos]=X4.get("1.0", "end-1c")
            Metier[NbPersos]=X5.get("1.0", "end-1c")
            PV[NbPersos]=X6.get("1.0", "end-1c")
            Mana[NbPersos]=X7.get("1.0", "end-1c")
            Magie_Physique[NbPersos]=X8.get("1.0", "end-1c")
            Magie_Psychique[NbPersos]=X9.get("1.0", "end-1c")
            Resistance_Magique[NbPersos]=X10.get("1.0", "end-1c")
            Courage[NbPersos]=X11.get("1.0", "end-1c")
            Force[NbPersos]=X12.get("1.0", "end-1c")
            Intelligence[NbPersos]=X13.get("1.0", "end-1c")
            Adresse[NbPersos]=X14.get("1.0", "end-1c")
            Charisme[NbPersos]=X15.get("1.0", "end-1c")
            Attaque[NbPersos]=X16.get("1.0", "end-1c")
            Parade[NbPersos]=X17.get("1.0", "end-1c")
            Points_de_destin[NbPersos]=X18.get("1.0", "end-1c")
            CommandPerso = GetPerso(NbPersos)
            imgperso[NbPersos]=PathImgPerso
            menu2.add_command(label=Nom[NbPersos], command=CommandPerso)
        def imageperso():
            global PersoImg, ImagePerso, PathImgPerso
            PathImgPerso = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
            PersoImg = ImageTk.PhotoImage(file=PathImgPerso)
            ImagePerso['image'] = PersoImg
        def inventaire():
            def sauvegarderinventaire():
                inventaire=[]
                for i in range(NbObjets):
                    inventaire.append(int(InvQuantite[i].get()))
                Inventaires[Nom[NbPersos]]=inventaire
                Finventaire.destroy()
            Finventaire = tk.Toplevel()
            Finventaire.title("Inventaire de "+Nom[NbPersos])
            Finventaire.resizable('false','false')
            Finventaire.geometry("675x600")
            Confimerinv = Button(Finventaire, text="Confirmer", command=sauvegarderinventaire).pack(side=BOTTOM, fill=X)
            sw= tk.ScrolledWindow(Finventaire, scrollbar=tk.Y) # just the vertical scrollbar
            sw.pack(fill=tk.BOTH, expand=1)
            InvQuantite=[]
            RetenuInv=0
            for i in range(NbObjets):
                if i%2==0:
                   FInvMaitre=tk.Frame(sw.window)
                   FInvMaitre.pack(side=TOP, fill=X)
                FInvObj=Frame(FInvMaitre,borderwidth=2, relief=GROOVE)
                FInvObj.pack(side=LEFT)
                ImgInv=PhotoImage(file=ImagesObjets[i])
                InvImg = Label(FInvObj, image=ImgInv).pack(fill=BOTH)
                Inv = Label(FInvObj, text=TitresObjets[i]).pack(fill=X)
                if Nom[NbPersos] in Inventaires:
                    if len(Inventaires[Nom[NbPersos]])==NbObjets:
                        Spin=Spinbox(FInvObj, from_=0, to=1000)
                        Spin.insert(END, Inventaires[Nom[NbPersos]][i])
                    elif RetenuInv!=len(Inventaires[Nom[NbPersos]]):
                        Spin=Spinbox(FInvObj, from_=0, to=1000)
                        Spin.insert(END, Inventaires[Nom[NbPersos]][i])
                        RetenuInv=RetenuInv+1
                    else:
                        Spin=Spinbox(FInvObj, from_=0, to=1000)
                else:
                    Spin=Spinbox(FInvObj, from_=0, to=1000)
                InvQuantite.append(Spin)
                InvQuantite[i].pack(fill=X)
            Finventaire.mainloop()
        perso = Toplevel()
        perso.geometry('200x640')
        perso.resizable('false','false')
        perso.title(Nom[NbPersos])
        photo = PhotoImage()
        F1 = Frame(perso)
        F1.pack(side=TOP)
        F2 = Frame(perso)
        F2.pack(side=TOP)
        F3 = Frame(perso)
        F3.pack(side=TOP)
        F4 = Frame(perso)
        F4.pack(side=TOP)
        F5 = Frame(perso)
        F5.pack(side=TOP)
        F6 = Frame(perso)
        F6.pack(side=TOP)
        F7 = Frame(perso)
        F7.pack(side=TOP)
        F8 = Frame(perso)
        F8.pack(side=TOP)
        F9 = Frame(perso)
        F9.pack(side=TOP)
        F10 = Frame(perso)
        F10.pack(side=TOP)
        F11 = Frame(perso)
        F11.pack(side=TOP)
        F12 = Frame(perso)
        F12.pack(side=TOP)
        F13 = Frame(perso)
        F13.pack(side=TOP)
        F14 = Frame(perso)
        F14.pack(side=TOP)
        F15 = Frame(perso)
        F15.pack(side=TOP)
        F16= Frame(perso)
        F16.pack(side=TOP)
        F17 = Frame(perso)
        F17.pack(side=TOP)
        F18 = Frame(perso)
        F18.pack(side=TOP)
        F19 = Frame(perso)
        F19.pack(side=TOP)
        F20 = Frame(perso)
        F20.pack(side=TOP)
        L1= Label(F1, text=creaperso[0])
        L1.pack(side=LEFT)
        X1= Text(F1, height=1)
        X1.pack(side=RIGHT)
        L2=Label(F2, text=creaperso[1])
        L2.pack(side=LEFT)
        X2=Text(F2, height=1)
        X2.pack(side=RIGHT)
        L3=Label(F3, text=creaperso[2])
        L3.pack(side=LEFT)
        X3=Text(F3, height=1)
        X3.pack(side=RIGHT)
        L4=Label(F4,text=creaperso[3])
        L4.pack(side=LEFT)
        X4=Text(F4, height=1)
        X4.pack(side=RIGHT)
        L5=Label(F5,text=creaperso[4])
        L5.pack(side=LEFT)
        X5=Text(F5, height=1)
        X5.pack(side=RIGHT)
        L6=Label(F6,text=creaperso[5])
        L6.pack(side=LEFT)
        X6=Text(F6, height=1)
        X6.pack(side=RIGHT)
        L7=Label(F7,text=creaperso[6])
        L7.pack(side=LEFT)
        X7=Text(F7, height=1)
        X7.pack(side=RIGHT)
        L8=Label(F8,text=creaperso[7])
        L8.pack(side=LEFT)
        X8=Text(F8, height=1)
        X8.pack(side=RIGHT)
        L9=Label(F9,text=creaperso[8])
        L9.pack(side=LEFT)
        X9=Text(F9, height=1)
        X9.pack(side=RIGHT)
        L10=Label(F10,text=creaperso[9])
        L10.pack(side=LEFT)
        X10=Text(F10, height=1)
        X10.pack(side=RIGHT)
        L11=Label(F11,text=creaperso[10])
        L11.pack (side=LEFT)
        X11=Text(F11, height=1)
        X11.pack(side=RIGHT)
        L12=Label(F12,text=creaperso[11])
        L12.pack(side=LEFT)
        X12=Text(F12, height=1)
        X12.pack(side=RIGHT)
        L13=Label(F13,text=creaperso[12])
        L13.pack(side=LEFT)
        X13=Text(F13, height=1)
        X13.pack(side=RIGHT)
        L14=Label(F14,text=creaperso[13])
        L14.pack (side=LEFT)
        X14=Text(F14, height=1)
        X14.pack(side=RIGHT)
        L15=Label(F15,text=creaperso[14])
        L15.pack (side=LEFT)
        X15=Text(F15, height=1)
        X15.pack(side=RIGHT)
        L16=Label(F16,text=creaperso[15])
        L16.pack (side=LEFT)
        X16=Text(F16, height=1)
        X16.pack(side=RIGHT)
        L17=Label(F17,text=creaperso[16])
        L17.pack (side=LEFT)
        X17=Text(F17, height=1)
        X17.pack(side=RIGHT)
        L18=Label(F19,text=creaperso[17])
        L18.pack (side=LEFT)
        X18=Text(F19, height=1)
        X18.pack(side=RIGHT)
        B19=Button(perso,text="Confirmer", command=confirmer)
        B19.pack(side=BOTTOM, fill=X)
        if NbObjets!=0:
            B21=Button(perso,text="Gérer inventaire", command=inventaire)
            B21.pack(side=BOTTOM, fill=X)
        B21=Button(perso, text="Changer d'image", command=imageperso)
        B21.pack(side=BOTTOM, fill=X)
        ImgPersoVar=ImageTk.PhotoImage(file=imgperso[NbPersos])
        ImagePerso=Label(perso, image=ImgPersoVar, height='300', width='300')
        ImagePerso.pack(fill=BOTH)
        X1.insert(END,Nom[NbPersos])
        X2.insert(END,Niveau[NbPersos])
        X3.insert(END,Sexe[NbPersos])
        X4.insert(END,Origine[NbPersos])
        X5.insert(END,Metier[NbPersos])
        X6.insert(END,PV[NbPersos])
        X7.insert(END,Mana[NbPersos])
        X8.insert(END,Magie_Physique[NbPersos])
        X9.insert(END,Magie_Psychique[NbPersos])
        X10.insert(END,Resistance_Magique[NbPersos])
        X11.insert(END,Courage[NbPersos])
        X12.insert(END,Force[NbPersos])
        X13.insert(END,Adresse[NbPersos])
        X14.insert(END,Intelligence[NbPersos])
        X15.insert(END,Charisme[NbPersos])
        X16.insert(END,Attaque[NbPersos])
        X17.insert(END,Parade[NbPersos])
        X18.insert(END,Points_de_destin[NbPersos])
        perso.bind("<Return>", confirmerInput)
        perso.mainloop()
    return inner
#==Editer sections==
def sections():
    global creaperso
    def confirm():
        creaperso[0]=X0.get("1.0", "end-1c")
        creaperso[1]=X1.get("1.0", "end-1c")
        creaperso[2]=X2.get("1.0", "end-1c")
        creaperso[3]=X3.get("1.0", "end-1c")
        creaperso[4]=X4.get("1.0", "end-1c")
        creaperso[5]=X5.get("1.0", "end-1c")
        creaperso[6]=X6.get("1.0", "end-1c")
        creaperso[7]=X7.get("1.0", "end-1c")
        creaperso[8]=X8.get("1.0", "end-1c")
        creaperso[9]=X9.get("1.0", "end-1c")
        creaperso[10]=X10.get("1.0", "end-1c")
        creaperso[11]=X11.get("1.0", "end-1c")
        creaperso[12]=X12.get("1.0", "end-1c")
        creaperso[13]=X13.get("1.0", "end-1c")
        creaperso[14]=X14.get("1.0", "end-1c")
        creaperso[15]=X15.get("1.0", "end-1c")
        creaperso[16]=X16.get("1.0", "end-1c")
        creaperso[17]=X17.get("1.0", "end-1c")
        sections.destroy()
    sections=Tk()
    sections.title("Editer les sections")
    sections.resizable(0,0)
    sections.geometry('200x400')
    F1 = Frame(sections)
    F1.pack(side=TOP)
    F2 = Frame(sections)
    F2.pack(side=TOP)
    F3 = Frame(sections)
    F3.pack(side=TOP)
    F4 = Frame(sections)
    F4.pack(side=TOP)
    F5 = Frame(sections)
    F5.pack(side=TOP)
    F6 = Frame(sections)
    F6.pack(side=TOP)
    F7 = Frame(sections)
    F7.pack(side=TOP)
    F8 = Frame(sections)
    F8.pack(side=TOP)
    F9 = Frame(sections)
    F9.pack(side=TOP)
    F10 = Frame(sections)
    F10.pack(side=TOP)
    F11 = Frame(sections)
    F11.pack(side=TOP)
    F12 = Frame(sections)
    F12.pack(side=TOP)
    F13 = Frame(sections)
    F13.pack(side=TOP)
    F14 = Frame(sections)
    F14.pack(side=TOP)
    F15 = Frame(sections)
    F15.pack(side=TOP)
    F16= Frame(sections)
    F16.pack(side=TOP)
    F17 = Frame(sections)
    F17.pack(side=TOP)
    F18 = Frame(sections)
    F18.pack(side=TOP)
    F19 = Frame(sections)
    F19.pack(side=TOP)
    X0= Text(F1, height=1)
    X0.pack(side=RIGHT)
    X0.insert(END, creaperso[0])
    X1=Text(F2, height=1)
    X1.pack(side=RIGHT)
    X1.insert(END, creaperso[1])
    X2=Text(F3, height=1)
    X2.pack(side=RIGHT)
    X2.insert(END, creaperso[2])
    X3=Text(F4, height=1)
    X3.pack(side=RIGHT)
    X3.insert(END, creaperso[3])
    X4=Text(F5, height=1)
    X4.pack(side=RIGHT)
    X4.insert(END, creaperso[4])
    X5=Text(F6, height=1)
    X5.pack(side=RIGHT)
    X5.insert(END, creaperso[5])
    X6=Text(F7, height=1)
    X6.pack(side=RIGHT)
    X6.insert(END, creaperso[6])
    X7=Text(F8, height=1)
    X7.pack(side=RIGHT)
    X7.insert(END, creaperso[7])
    X8=Text(F9, height=1)
    X8.pack(side=RIGHT)
    X8.insert(END, creaperso[8])
    X9=Text(F10, height=1)
    X9.pack(side=RIGHT)
    X9.insert(END, creaperso[9])
    X10=Text(F11, height=1)
    X10.pack(side=RIGHT)
    X10.insert(END, creaperso[10])
    X11=Text(F12, height=1)
    X11.pack(side=RIGHT)
    X11.insert(END, creaperso[11])
    X12=Text(F13, height=1)
    X12.pack(side=RIGHT)
    X12.insert(END, creaperso[12])
    X13=Text(F14, height=1)
    X13.pack(side=RIGHT)
    X13.insert(END, creaperso[13])
    X14=Text(F15, height=1)
    X14.pack(side=RIGHT)
    X14.insert(END, creaperso[14])
    X15=Text(F16, height=1)
    X15.pack(side=RIGHT)
    X15.insert(END, creaperso[15])
    X16=Text(F17, height=1)
    X16.pack(side=RIGHT)
    X16.insert(END, creaperso[16])
    X17=Text(F19, height=1)
    X17.pack(side=RIGHT)
    X17.insert(END, creaperso[17])
    B19=Button(sections, text="Confirmer", command=confirm)
    B19.pack(side=BOTTOM,fill=X,expand=1)
    sections.mainloop()
#=====Scénario========
def Scenario():
    global NbScenarios, ScenarioTitreE, ScenarioTVar, ScenarioContenu, NbPDF
    ScenarioF=Tk()
    ScenarioF.title('Scénarios')
    ScenarioF.geometry('500x434')
    ScenarioF.resizable(0,0)
    def SConfirmer():
        global NbScenarios, ScenarioTitreE, ScenarioTVar, ScenarioContenu, NbPDF
        ScenarioTitreE[NbScenarios]=ScenarioTitre.get("1.0", "end-1c")
        ScenarioContenu[NbScenarios]=ScenarioTexte.get("1.0", "end-1c")
        ScenarioF.destroy()
        if NbScenarios==0 and NbPDF==0:
            menu3.add_separator()
        NumScenario = GetScenario(NbScenarios)
        menu3.add_command(label=ScenarioTitreE[NbScenarios], command=NumScenario)
        NbScenarios = NbScenarios+1
    ScenarioTitre = Text(ScenarioF, height=1)
    ScenarioTitre.pack(fill=X)
    ScenarioTitre.insert(END, "Entrez le titre du scénario...")
    ScenarioTexte = Text(ScenarioF)
    ScenarioTexte.pack(fill=BOTH)
    ScenarioTexte.insert(END, "Entrez le contenu de votre scénario ici...")
    ScenarioConfirmer = Button(ScenarioF, text="Confirmer", command=SConfirmer).pack(fill=X)
    ScenarioF.mainloop()
def GetScenario(NbScenarios):
    def inner():
        global ScenarioTitreE, ScenarioTVar, ScenarioContenu
        def SConfirmer():
            global ScenarioTitreE, ScenarioTVar, ScenarioContenu
            menu3.delete(ScenarioTitreE[NbScenarios])
            ScenarioTitreE[NbScenarios]=ScenarioTitre.get("1.0", "end-1c")
            ScenarioContenu[NbScenarios]=ScenarioTexte.get("1.0", "end-1c")
            NumScenario = GetScenario(NbScenarios)
            menu3.add_command(label=ScenarioTitreE[NbScenarios], command=NumScenario)
        ScenarioF=Tk()
        ScenarioF.title(ScenarioTitreE[NbScenarios])
        ScenarioF.geometry('500x434')
        ScenarioF.resizable(0,0)
        ScenarioTitre = Text(ScenarioF, height=1)
        ScenarioTitre.pack(fill=X)
        ScenarioTitre.insert(END,ScenarioTitreE[NbScenarios])
        ScenarioTexte = Text(ScenarioF)
        ScenarioTexte.pack(fill=BOTH)
        ScenarioTexte.insert(END,ScenarioContenu[NbScenarios])
        ScenarioConfirmer = Button(ScenarioF, text="Confirmer", command=SConfirmer).pack(fill=X)
        ScenarioF.mainloop()
    return inner
def ScenarioPDF():
    global NbScenarios, NbPDF, ScenariosPDF
    CheminScenarioPDF = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PDF','.pdf')])
    if NbScenarios==0 and NbPDF==0:
        menu3.add_separator()
    menu3.add_command(label=CheminScenarioPDF, command=ReadPDF(CheminScenarioPDF))
    ScenariosPDF[NbPDF]=CheminScenarioPDF
    NbPDF = NbPDF+1
def ReadPDF(CheminScenarioPDF):
    def inner():
        webbrowser.open(os.path.realpath(CheminScenarioPDF))
    return inner
#=====Cartes=========
def cartes():
    global Fond_label, imgdict, NbCartes
    NbCartes=NbCartes+1
    numcarte= Fond(NbCartes)
    CheminImage = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
    photo = ImageTk.PhotoImage(file=CheminImage)
    menu4.add_command(label=NbCartes,command=numcarte)
    imgdict[NbCartes] = photo
    Fond_label['image']=photo
def Fond(NbCartes):
    global imgdict
    def inner():
        Fond_label['image']=imgdict[NbCartes]
    return inner
#======Objets=====
def Objets():
    global Image, NbObjets, ImagesObjets, DescriptionsObjets, ObjImg, DescriptionObj,  TitreObj, TitresObjets, PathObjImg
    def confirmer():
        global NbObjets, ImagesObjets, DescriptionsObjets, ObjImg, DescriptionObj, TitreObj,  TitresObjets, PathObjImg
        if  NbObjets==0:
            menu5.add_separator()
        ImagesObjets[NbObjets]=PathObjImg
        DescriptionsObjets[NbObjets]=DescriptionObj.get("1.0", "end-1c")
        TitresObjets[NbObjets]=TitreObj.get("1.0", "end-1c")
        FuncObj = GetObj(NbObjets)
        menu5.add_command(label=TitresObjets[NbObjets], command=FuncObj)
        NbObjets=NbObjets+1
        ObjetF.destroy()
    def ImgObj():
        global Image, ObjImg, PathObjImg
        PathObjImg = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
        ObjImg = ImageTk.PhotoImage(file=PathObjImg)
        Image['image'] = ObjImg
    ObjetF = Toplevel()
    ObjetF.resizable(False, False)
    ObjetF.title("Objets")
    PathObjImg='question.gif'
    ObjImg = PhotoImage(file=PathObjImg)
    ObjF1 = Frame(ObjetF)
    ObjF1.pack(side=LEFT, fill=BOTH)
    ObjF2 = Frame(ObjetF)
    ObjF2.pack(side=RIGHT, fill=BOTH)
    Image = Label(ObjF1, height=300, width=300, image=ObjImg)
    Image.pack(side=TOP, fill=BOTH)
    TitreObj = Text(ObjF2, height=1, width=50 )
    TitreObj.pack(side=TOP, fill=X)
    TitreObj.insert(END, "Entrez le nom de l'objet ici...", 'color')
    DescriptionObj = Text(ObjF2, height=17.5, width=50)
    scroll = Scrollbar(ObjF2, command=DescriptionObj.yview)
    DescriptionObj.configure(yscrollcommand=scroll.set)
    DescriptionObj.insert(END, "Entrez la description de l'objet ici...", 'color')
    scroll.pack(side=RIGHT, fill=Y)
    DescriptionObj.pack(side=TOP, fill=X)
    ImageObj = Button(ObjF1, text="Changer l'image", command=ImgObj)
    ImageObj.pack(side=BOTTOM,fill=X)
    EnregistrerObj = Button(ObjF2, text="Confirmer", command=confirmer)
    EnregistrerObj.pack(side=BOTTOM,fill=X)
    ObjetF.mainloop()
def GetObj(NbObjets):
    def inner():
        global Image, ImagesObjets, DescriptionsObjets, ObjImg, DescriptionObj, TitresObjets, PathObjImg
        def confirmer():
            global ImagesObjets, DescriptionsObjets, ObjImg, DescriptionObj, TitresObjets, PathObjImg
            menu5.delete(TitresObjets[NbObjets])
            ImagesObjets[NbObjets]= PathObjImg
            TitresObjets[NbObjets]=TitreObj.get("1.0", "end-1c")
            DescriptionsObjets[NbObjets]=DescriptionObj.get("1.0", "end-1c")
            FuncObj = GetObj(NbObjets)
            menu5.add_command(label=TitresObjets[NbObjets], command=FuncObj)
        def ImgObj():
            global Image, ObjImg, PathObjImg
            PathObjImg = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
            ObjImg = ImageTk.PhotoImage(file=PathObjImg)
            Image['image'] = ObjImg
        ObjetF = Toplevel()
        ObjetF.resizable(False, False)
        ObjetF.title(TitresObjets[NbObjets])
        ObjImg = PhotoImage(file=ImagesObjets[NbObjets])
        ObjF1 = Frame(ObjetF)
        ObjF1.pack(side=LEFT, fill=BOTH)
        ObjF2 = Frame(ObjetF)
        ObjF2.pack(side=RIGHT, fill=BOTH)
        Image = Label(ObjF1, height=300, width=300, image=ObjImg)
        Image.pack(side=TOP, fill=BOTH)
        TitreObj = Text(ObjF2, height=1, width=50 )
        TitreObj.pack(side=TOP, fill=X)
        TitreObj.insert(END, TitresObjets[NbObjets])
        DescriptionObj = Text(ObjF2, height=18.5, width=50)
        scroll = Scrollbar(ObjF2, command=DescriptionObj.yview)
        DescriptionObj.configure(yscrollcommand=scroll.set)
        DescriptionObj.insert(END, DescriptionsObjets[NbObjets])
        scroll.pack(side=RIGHT, fill=Y)
        DescriptionObj.pack(side=TOP, fill=X)
        ImageObj = Button(ObjF1, text="Changer l'image", command=ImgObj)
        ImageObj.pack(side=BOTTOM,fill=X)
        EnregistrerObj = Button(ObjF2, text="Confirmer", command=confirmer)
        EnregistrerObj.pack(side=BOTTOM,fill=X)
        ObjetF.mainloop()
    return inner
#=====Ennemis====
def Ennemis():
    global NbEnnemis, EImg, PathImgE
    def imageennemis():
        global EImg, PathImgE
        PathImgE = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers JPEG','.jpg'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
        EImg = ImageTk.PhotoImage(file=PathImgE)
        L7['image'] = EImg
    def confirmer():
        global NbEnnemis, NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, EImg, imge, PathImgE
        NomE[NbEnnemis]=X1.get("1.0", "end-1c")
        NiveauE[NbEnnemis]=X2.get("1.0", "end-1c")
        ResistanceE[NbEnnemis]=X3.get("1.0", "end-1c")
        DegatsE[NbEnnemis]=X4.get("1.0", "end-1c")
        BonusE[NbEnnemis]=X5.get("1.0", "end-1c")
        DescriptionE[NbEnnemis]=X6.get("1.0", "end-1c")
        imge[NbEnnemis]= PathImgE
        if NbEnnemis ==0:
            menu6.add_separator()
        CommandEnnemis = GetEnnemis(NbEnnemis)
        menu6.add_command(label=NomE[NbEnnemis], command=CommandEnnemis)
        NbEnnemis = NbEnnemis+1
        ennemis.destroy()
    ennemis = Toplevel()
    ennemis.geometry('300x626')
    ennemis.title('Créer')
    F1 = Frame(ennemis)
    F1.pack(side=TOP)
    F2 = Frame(ennemis)
    F2.pack(side=TOP)
    F3 = Frame(ennemis)
    F3.pack(side=TOP)
    F4 = Frame(ennemis)
    F4.pack(side=TOP)
    F5 = Frame(ennemis)
    F5.pack(side=TOP)
    F6 = Frame(ennemis)
    F6.pack(side=TOP)
    L1= Label(F1, text=creaennemis[0])
    L1.pack(side=LEFT)
    X1= Text(F1, height=1)
    X1.pack(side=RIGHT)
    L2=Label(F2, text=creaennemis[1])
    L2.pack(side=LEFT)
    X2=Text(F2, height=1)
    X2.pack(side=RIGHT)
    L3=Label(F3, text=creaennemis[2])
    L3.pack(side=LEFT)
    X3=Text(F3, height=1)
    X3.pack(side=RIGHT)
    L4=Label(F4,text=creaennemis[3])
    L4.pack(side=LEFT)
    X4=Text(F4, height=1)
    X4.pack(side=RIGHT)
    L5=Label(F5,text=creaennemis[4])
    L5.pack(side=LEFT)
    X5=Text(F5, height=1)
    X5.pack(side=RIGHT)
    L6=Label(F6,text=creaennemis[5])
    L6.pack(side=LEFT)
    X6=Text(F6, height=10)
    X6.pack(side=RIGHT)
    PathImgE='question.gif'
    EImg = PhotoImage(file=PathImgE)
    L7=Label(ennemis, height=300, width=300, image=EImg)
    L7.pack(fill=BOTH)
    B19=Button(ennemis,text="Changer l'image", command=imageennemis)
    B19.pack(fill=X)
    B20=Button(ennemis,text="Confirmer", command=confirmer)
    B20.pack(side=BOTTOM, fill=X)
    ennemis.mainloop()
def GetEnnemis(NbEnnemis):
    def inner():
        global NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, PathImgE
        def imageennemis():
            global EImg, PathImgE
            PathImgE = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers JPEG','.jpg'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
            EImg = ImageTk.PhotoImage(file=PathImgE)
            L7['image'] = EImg
        def confirmer():
            global NomE, NiveauE, ResistanceE, DegatsE,  BonusE, DescriptionE, EImg, imge, PathImgE
            menu6.delete(NomE[NbEnnemis])
            NomE[NbEnnemis]=X1.get("1.0", "end-1c")
            NiveauE[NbEnnemis]=X2.get("1.0", "end-1c")
            ResistanceE[NbEnnemis]=X3.get("1.0", "end-1c")
            DegatsE[NbEnnemis]=X4.get("1.0", "end-1c")
            BonusE[NbEnnemis]=X5.get("1.0", "end-1c")
            DescriptionE[NbEnnemis]=X6.get("1.0", "end-1c")
            imge[NbEnnemis]= PathImgE
            CommandEnnemis = GetEnnemis(NbEnnemis)
            menu6.add_command(label=NomE[NbEnnemis], command=CommandEnnemis)
        ennemis = Toplevel()
        ennemis.geometry('300x626')
        ennemis.title(NomE[NbEnnemis])
        photo = PhotoImage()
        F1 = Frame(ennemis)
        F1.pack(side=TOP)
        F2 = Frame(ennemis)
        F2.pack(side=TOP)
        F3 = Frame(ennemis)
        F3.pack(side=TOP)
        F4 = Frame(ennemis)
        F4.pack(side=TOP)
        F5 = Frame(ennemis)
        F5.pack(side=TOP)
        F6 = Frame(ennemis)
        F6.pack(side=TOP)
        L1= Label(F1, text=creaennemis[0])
        L1.pack(side=LEFT)
        X1= Text(F1, height=1)
        X1.pack(side=RIGHT)

        L2=Label(F2, text=creaennemis[1])
        L2.pack(side=LEFT)
        X2=Text(F2, height=1)
        X2.pack(side=RIGHT)

        L3=Label(F3, text=creaennemis[2])
        L3.pack(side=LEFT)
        X3=Text(F3, height=1)
        X3.pack(side=RIGHT)

        L4=Label(F4,text=creaennemis[3])
        L4.pack(side=LEFT)
        X4=Text(F4, height=1)
        X4.pack(side=RIGHT)

        L5=Label(F5,text=creaennemis[4])
        L5.pack(side=LEFT)
        X5=Text(F5, height=1)
        X5.pack(side=RIGHT)

        L6=Label(F6,text=creaennemis[5])
        L6.pack(side=LEFT)
        X6=Text(F6, height=10)
        X6.pack(side=RIGHT)
        EImg = PhotoImage(file=imge[NbEnnemis])
        L7=Label(ennemis, height=300, width=300, image=EImg)
        L7.pack(fill=BOTH)
        B19=Button(ennemis,text="Changer l'image", command=imageennemis)
        B19.pack(fill=X)
        B20=Button(ennemis,text="Confirmer", command=confirmer)
        B20.pack(side=BOTTOM, fill=X)
        X1.insert(END,NomE[NbEnnemis])
        X2.insert(END,NiveauE[NbEnnemis])
        X3.insert(END,ResistanceE[NbEnnemis])
        X4.insert(END,DegatsE[NbEnnemis])
        X5.insert(END,BonusE[NbEnnemis])
        X6.insert(END,DescriptionE[NbEnnemis])
        ennemis.mainloop()
    return inner
#==Editer sections Ennemis==
def sectionsE():
    global creaennemis
    def confirm():
        creaennemis[0]=X0.get("1.0", "end-1c")
        creaennemis[1]=X1.get("1.0", "end-1c")
        creaennemis[2]=X2.get("1.0", "end-1c")
        creaennemis[3]=X3.get("1.0", "end-1c")
        creaennemis[4]=X4.get("1.0", "end-1c")
        sectionsE.destroy()
    sectionsE=Tk()
    sectionsE.title("Editer les sections")
    sectionsE.resizable(0,0)
    sectionsE.geometry('200x150')
    F1 = Frame(sectionsE)
    F1.pack(side=TOP)
    F2 = Frame(sectionsE)
    F2.pack(side=TOP)
    F3 = Frame(sectionsE)
    F3.pack(side=TOP)
    F4 = Frame(sectionsE)
    F4.pack(side=TOP)
    F5 = Frame(sectionsE)
    F5.pack(side=TOP)
    X0= Text(F1, height=1)
    X0.pack(side=RIGHT)
    X0.insert(END, creaennemis[0])
    X1=Text(F2, height=1)
    X1.pack(side=RIGHT)
    X1.insert(END, creaennemis[1])
    X2=Text(F3, height=1)
    X2.pack(side=RIGHT)
    X2.insert(END, creaennemis[2])
    X3=Text(F4, height=1)
    X3.pack(side=RIGHT)
    X3.insert(END, creaennemis[3])
    X4=Text(F5, height=1)
    X4.pack(side=RIGHT)
    X4.insert(END, creaennemis[4])
    B19=Button(sectionsE, text="Confirmer", command=confirm)
    B19.pack(side=BOTTOM,fill=X,expand=1)
    sectionsE.mainloop()
#======Crédits=====
def apropos():
    Fenetre1=Tk()
    L1F1 = Label(Fenetre1, text="Réalisation Antoine Joly, Nello Gothuey, Brayan Desmurger.")
    L1F1.pack()
    L2F1 = Label(Fenetre1, text="Tous droits réservés. Copyright 2017.")
    L2F1.pack()
    Fenetre1.title("A Propos")
    Fenetre1.geometry('400x90')
    Fenetre1.resizable(False, False) #Empécher de modifier la taille de la fenêtre
    B1F1 = Button(Fenetre1, height=10, text="Fermer",command=Fenetre1.destroy).pack(fill=X)
    Fenetre1.mainloop()
#============Interface Graphique==============
imgdict={}
root = Tk()
root.title('JDR')
menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichiers", menu=menu1)
menu1.add_command(label="Exporter sauvegardes", command=export)
menu1.add_command(label="Importer sauvegardes", command=import_sauvegarde)
menu1.add_command(label="Importer module", command=importmodule)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Créer", command=perso)
menu2.add_command(label="Editer sections", command=sections)
menubar.add_cascade(label="Personnages", menu=menu2)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Créer", command=Scenario)
menu3.add_command(label="Créer un raccourci PDF", command=ScenarioPDF)
menubar.add_cascade(label="Scénarios", menu=menu3)
menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="Ouvrir", command=cartes)
menubar.add_cascade(label="Cartes", menu=menu4)
menu5 = Menu(menubar, tearoff=0)
menu5.add_command(label="Créer", command=Objets)
menubar.add_cascade(label="Objets", menu=menu5)
menu6 = Menu(menubar, tearoff=0)
menu6.add_command(label="Créer", command=Ennemis)
menu6.add_command(label="Editer sections", command=sectionsE)
menubar.add_cascade(label="Ennemis", menu=menu6)
menu7 = Menu(menubar, tearoff=0)
menu7.add_command(label="A propos", command=apropos)
menu7.add_command(label="Informations sur l'utilisation du logiciel", command=help)
menu7.add_separator()
menu7.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Aide", menu=menu7)
CheminImage = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('Fichiers PNG','.png'),('Fichiers JPEG','.jpg'),('Fichiers GIF','.gif'),('Tous les fichiers','.*')])
photo = ImageTk.PhotoImage(file=CheminImage)
menu4.add_separator()
numcarte= Fond(NbCartes)
menu4.add_command(label=NbCartes, command=numcarte)
imgdict[NbCartes]= photo
Fond_label = Label(root, image=photo)
Fond_label.pack(fill=BOTH, expand=1)
root.config(menu=menubar)
root.mainloop()
