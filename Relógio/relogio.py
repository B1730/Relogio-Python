from tkinter import *
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf") #Tentei por fonte e não funcionol, NÃO SEI PQ.

# Cores:
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#ff463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor3  # Caso queira trocar a cor do relogio, é so mudar aqui.

janela = Tk()
janela.title("")  # titulo da janela
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)  # cor de fundo da janela


def relogio():

    tempo = datetime.now()  # hora da maquina

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")  # minusculo pq quero abreviação
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)  # Dps de 200 milesimos vai executar novamente.
    l2.config(text=f"{dia_semana} {dia}/{mes}/{ano}")

# Pra hora:
l1 = Label(janela, text="", font=("digital-7",80), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
# Pra dia, mes e ano:
l2 = Label(janela, text="", font=("digital-7", 20 ), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
