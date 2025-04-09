#Sorteador para um Bingo

import customtkinter
from tkinter import *

#Configurando a tela
customtkinter.set_appearance_mode("dark")
tela = customtkinter.CTk()
tela.geometry("500x400")
tela.title("Sorteador para bingo")
tela.resizable(False, False) #não é possível redimensionar width ou height da tela

img = PhotoImage(file="")
label_img = customtkinter.CTkLabel(master=tela, image=img)
label_img.place(x=220, y=65)

tela.mainloop()