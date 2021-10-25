####################### IMPORTANDO AS BIBLIOTECAS #######################
from tkinter import *
from tkinter import ttk

####################### DEFININDO CORES #######################
cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

####################### CRIANDO A JANELA #######################
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x308')
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

####################### CRIANDO AS FUNÇÕES #######################
todos_valores = ''
valor_texto = StringVar()

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


####################### CRIANDO OS BOTÕES #######################
bt_clear = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_clear.place(x=0, y=0)
bt_resto = Button(frame_corpo, command=lambda: entrar_valores("%"), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_resto.place(x=118, y=0)
bt_div = Button(frame_corpo, command=lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_div.place(x=177, y=0)

bt_7 = Button(frame_corpo, command=lambda: entrar_valores("7"), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_7.place(x=0, y=52)
bt_8 = Button(frame_corpo, command=lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_8.place(x=59, y=52)
bt_9 = Button(frame_corpo, command=lambda: entrar_valores("9"), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_9.place(x=118, y=52)
bt_mult = Button(frame_corpo, command=lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_mult.place(x=177, y=52)

bt_4 = Button(frame_corpo, command=lambda: entrar_valores("4"), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_4.place(x=0, y=104)
bt_5 = Button(frame_corpo, command=lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_5.place(x=59, y=104)
bt_6 = Button(frame_corpo, command=lambda: entrar_valores("6"), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_6.place(x=118, y=104)
bt_sub = Button(frame_corpo, command=lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_sub.place(x=177, y=104)

bt_1 = Button(frame_corpo, command=lambda: entrar_valores("1"), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_1.place(x=0, y=156)
bt_2 = Button(frame_corpo, command=lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_2.place(x=59, y=156)
bt_3 = Button(frame_corpo, command=lambda: entrar_valores("3"), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_3.place(x=118, y=156)
bt_adi = Button(frame_corpo, command=lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_adi.place(x=177, y=156)

bt_0 = Button(frame_corpo, command=lambda: entrar_valores("0"), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_0.place(x=0, y=208)
bt_ponto = Button(frame_corpo, command=lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_ponto.place(x=118, y=208)
bt_igual = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt_igual.place(x=177, y=208)


janela.mainloop()
