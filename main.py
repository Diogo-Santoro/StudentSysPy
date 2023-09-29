from tkinter import *


def salvar_dados():
    m = (p1 + p2) / 2
    media.config(state="normal")
    media.insert(0, str(m))
    media.config(state="readonly")


tela = Tk()

Label(tela, text="Identificador").grid(column=0, row=0)
n1 = Entry(tela)
n1.grid(column=1, row=0)

Label(tela, text="Nome").grid(column=0, row=1)
n2 = Entry(tela)
n2.grid(column=1, row=1)

Label(tela, text="Rua").grid(column=0, row=2)
n2 = Entry(tela)
n2.grid(column=1, row=2)

Label(tela, text="Bairro").grid(column=0, row=3)
n2 = Entry(tela)
n2.grid(column=1, row=3)

Label(tela, text="Cidade").grid(column=0, row=4)
n2 = Entry(tela)
n2.grid(column=1, row=4)

Label(tela, text="Bairro").grid(column=0, row=5)
n2 = Entry(tela)
n2.grid(column=1, row=5)

Label(tela, text="Estado").grid(column=0, row=6)
media = Entry(tela, state="readonly")
media.grid(column=1, row=6)

Label(tela, text="CEP").grid(column=0, row=7)
n2 = Entry(tela)
n2.grid(column=1, row=7)

Label(tela, text="Celular").grid(column=0, row=8)
n2 = Entry(tela)
n2.grid(column=1, row=8)

Label(tela, text="E-mail").grid(column=0, row=9)
n2 = Entry(tela)
n2.grid(column=1, row=9)

Label(tela, text="CPF").grid(column=0, row=10)
n2 = Entry(tela)
n2.grid(column=1, row=10)

Label(tela, text="RG").grid(column=0, row=11)
n2 = Entry(tela)
n2.grid(column=1, row=11)


btn_calc = Button(tela, text="Cadastrar", command=salvar_dados)
btn_calc.grid(column=0, row=12)

Button(tela, text="FIM", command=quit).grid(column=1, row=12)

tela.mainloop()