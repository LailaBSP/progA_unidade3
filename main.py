# Interface e eventos do mouse

from tkinter import *
from tkinter import ttk

from figuras import (
    Linha,
    Rabisco,
    Retangulo,
    Oval,
    Circulo,
    Poligono
)

# Controle dos eventos

def gerenciar_clique(event):
    global figura_nova

    tipo = tipo_figura_var.get()

    classes_figuras = {
        'Linha': Linha,
        'Rabisco': Rabisco,
        'Retângulo': Retangulo,
        'Oval': Oval,
        'Circulo': Circulo,
        'Polígono': Poligono
    }

    if tipo == 'Polígono':

        if figura_nova is None:
            figura_nova = Poligono(event.x, event.y)
        else:
            figura_nova.adicionar_ponto(event.x, event.y)

    else:

        classe = classes_figuras.get(tipo, Linha)
        figura_nova = classe(event.x, event.y)

    desenhar_tudo()


def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova:
        figura_nova.atualizar(event.x, event.y)
        desenhar_tudo()


def incluir_figura_nova(event):
    global figura_nova

    if tipo_figura_var.get() == 'Polígono':
        return

    if figura_nova and not figura_nova.esta_incompleta():
        figuras.append(figura_nova)

    figura_nova = None
    desenhar_tudo()


def finalizar_poligono(event):
    global figura_nova

    if tipo_figura_var.get() == 'Polígono' and figura_nova:

        if not figura_nova.esta_incompleta():
            figuras.append(figura_nova)

        figura_nova = None
        desenhar_tudo()


def desenhar_tudo():

    canvas.delete("all")

    for figura in figuras:
        figura.desenhar(canvas)

    if figura_nova:
        figura_nova.desenhar(canvas, True)


# -----------------------------
# Interface
# -----------------------------

figuras = []
figura_nova = None

root = Tk()
root.title("Projeto UFS - Programação A - IA - 2026")

frame = Frame(root)
frame.pack()

ttk.Label(
    frame,
    text="Escolha o que vai desenhar:"
).grid(row=0, column=0, padx=5, pady=5)

tipo_figura_var = StringVar(root)

ttk.OptionMenu(
    frame,
    tipo_figura_var,
    "Linha",
    "Linha",
    "Rabisco",
    "Retângulo",
    "Oval",
    "Circulo",
    "Polígono"
).grid(row=0, column=1, padx=5, pady=5)

canvas = Canvas(
    frame,
    width=600,
    height=600,
    bg="pink"
)

canvas.grid(row=1, column=0, columnspan=2)

canvas.bind("<ButtonPress-1>", gerenciar_clique)
canvas.bind("<B1-Motion>", atualizar_figura_nova)
canvas.bind("<ButtonRelease-1>", incluir_figura_nova)
canvas.bind("<Double-Button-1>", finalizar_poligono)

root.mainloop()