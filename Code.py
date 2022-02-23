from PIL import ImageTk,Image
from tkinter import *
import webbrowser


tela=Tk()
tela.title("Ultima Ceia")




def home():
    url="https://github.com/RoadMapPython"
    new=1
    webbrowser.open(url,new=new) 

def pedraPapelTesoura():
    
    url="https://github.com/RoadMapPython/Pedra-papel-e-tesoura"
    new=1
    webbrowser.open(url,new=new)


def webScraping():
    url="https://github.com/RoadMapPython/Web-Scraping"
    new=1
    webbrowser.open(url,new=new)


def pedraGUI():
    url="https://github.com/RoadMapPython/RoadMapPython/blob/main/Interface%20gr%C3%A1fica%20jokenpo.png"
    new=1
    webbrowser.open(url,new=new)



def simuladorDesenvolvedor():
    url="https://github.com/RoadMapPython/Simulador-Vida-de-um-des"
    new=1
    webbrowser.open(url,new=new)  



def FiltroInstagram():

    url="https://github.com/RoadMapPython/Filtros-de-Instagram"
    new=1
    webbrowser.open(url,new=new)  


def PyautoGUI():

    url="https://github.com/RoadMapPython/PyAutoGUI"
    new=1
    webbrowser.open(url,new=new)  


def Forca():
   
    url="https://github.com/RoadMapPython/Live-jogo-da-forca"
    new=2
    webbrowser.open(url,new=new)


def Minicursos():
   
    url="https://github.com/RoadMapPython/Minicurso-python"
    new=2
    webbrowser.open(url,new=new)


def ManipulandoDoc():
   
    url="https://github.com/RoadMapPython/Manipulando-documentos-em-python"
    new=2
    webbrowser.open(url,new=new)

def RelogioGIT():
   
    url="https://github.com/RoadMapPython/Relogio-Grafico-e-GIT"
    new=2
    webbrowser.open(url,new=new)




logo=PhotoImage(file="logodacc(1).png")
pedraPapel=PhotoImage(file="1.png",width=200,height=113)
webScra=PhotoImage(file="webScraping.png",width=200,height=113)
pedraGU=PhotoImage(file="pedraGUI.png",width=200,height=113)
simulador=PhotoImage(file="simuladorDesenvolvedor.png",width=200,height=113)
filtro=PhotoImage(file="Filtros de Instagram.png",width=200,height=113)
Pyauto=PhotoImage(file="PyautoGUI.png",width=200,height=113)
Minicurso=PhotoImage(file="Minicurso Python.png",width=200,height=113)
Manipulando=PhotoImage(file="Manipulando Documentos.png",width=200,height=113)
Relogio=PhotoImage(file="Relógio gráfico e introdução ao GIT.png",width=200,height=113)
forca=PhotoImage(file="Jogo da forca.png",width=200,height=113)

botao=Button(tela,image=logo,command=home)
botao.place(x=100,y=100)

botao1=Button(tela,image=webScra,command=webScraping)
botao1.place(x=350,y=100)

botao2=Button(tela,image=pedraGU,command=pedraGUI)
botao2.place(x=600,y=100)

botao3=Button(tela,image=simulador,command=simuladorDesenvolvedor)
botao3.place(x=850,y=100)


botao4=Button(tela,image=filtro,command=FiltroInstagram)
botao4.place(x=350, y=280)

botao5=Button(tela,image=Pyauto,command=PyautoGUI)
botao5.place(x=600, y=280)

botao6=Button(tela,image=forca,command=Forca)
botao6.place(x=850,y=280)

botao7=Button(tela,image=Minicurso,command=Minicursos)
botao7.place(x=350,y=460)


botao8=Button(tela,image=Manipulando,command=ManipulandoDoc)
botao8.place(x=600,y=460)

botao9=Button(tela,image=Relogio,command=RelogioGIT)
botao9.place(x=850,y=460)






Titulo=Label(tela,font=("Super Mario 256",20),text="RoadMap Python",anchor="center",background="#F9EAC3",foreground="Green").place(x=550,y=10, width=300,height=80)
HOME=Label(tela,font=("Super Mario 256",20),text="GitHUB Dacc",background="#F9EAC3",foreground="#012161").place(x=95,y=300, width=215,height=80)


Agradecimento=Label(tela,font=("Super Mario 256",20),text="Obrigado Por Tudo Pessoal",foreground="Red",background="#F9EAC3").place(x=400,y=600, width=550,height=130)








tela.geometry("1200x600+0+0")
tela.configure(background="#F9EAC3")
tela.mainloop()

