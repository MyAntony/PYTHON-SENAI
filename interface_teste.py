from tkinter import *
from tkinter import messagebox

def hello():
    messagebox.showinfo("Mensagem", "Olá, mundo!")

menu_inicial = Tk()

menu_inicial.title("Meu primeiro software")
menu_inicial.geometry("500x500+700+200")
menu_inicial.resizable(width=False, height=False)
menu_inicial.iconbitmap("icone.ico")
menu_inicial ['bg'] = "#7FFF00"

# Label
label1 = Label(menu_inicial, text = "Programa teste", fg = "red", font= "Arial 20 italic")
label1.pack() 

# Botão
botao = Button(menu_inicial, text = "OK", bg = "DarkGray", fg = "blue", font = "Arial 20 bold", command = hello)
botao.pack()

botao_sair = Button(menu_inicial, text = "Sair", bg = "DarkGray", fg = "blue", font = "Arial 20 bold", command = menu_inicial.quit)
botao_sair.pack()

menu_inicial.mainloop()