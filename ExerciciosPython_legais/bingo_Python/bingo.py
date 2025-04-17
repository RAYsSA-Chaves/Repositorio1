#Sorteador para um Bingo

import customtkinter
from tkinter import *
import os  #permite interagir com o sistema, arquivos e pastas

var = 1
lista = [1, 2, 3]

#O Python não estava conseguindo localizar a imagem, então corrigindo isso:
current_dir = os.path.dirname(__file__)
image_path1 = os.path.join(current_dir, "capa.png")

#Configurando a tela:
customtkinter.set_appearance_mode("dark")
tela = customtkinter.CTk()
tela.geometry("500x400")
tela.title("Sorteador para bingo")
tela.resizable(False, False)  #desabilita redimensionar a tela

#Imagem da tela:
img = PhotoImage(file=image_path1)
label_img = customtkinter.CTkLabel(master=tela, image=img)
label_img.place(relx=0.5, y=65, anchor="center")

#Exibiindo o valores sorteado e que já foram:
label_lista = customtkinter.CTkLabel(master=tela, text=f"{lista}", font=("Roboto", 16))
label_lista.place(relx=0.5,y=130, anchor="center")
label_num = customtkinter.CTkLabel(master=tela, text=var, font=("Roboto", 50))
label_num.place(relx=0.5, y=200, anchor="center")

tela.mainloop()