from tkinter import *
from tkinter import ttk

import eventos


root = Tk()
root.title("Projeto UFS - Programação A - IA - 2026")

frame = Frame(root)
frame.pack()

ttk.Label(
    frame,
    text="Escolha o que vai desenhar:"
).grid(row=0, column=0, padx=5, pady=5)

eventos.tipo_figura_var = StringVar(root)

ttk.OptionMenu(
    frame,
    eventos.tipo_figura_var,
    "Linha",
    "Linha",
    "Rabisco",
    "Retângulo",
    "Oval",
    "Circulo",
    "Polígono"
).grid(row=0, column=1, padx=5, pady=5)

eventos.canvas = Canvas(
    frame,
    bg="pink",
    width=600,
    height=600
)

eventos.canvas.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=5,
    pady=5
)

eventos.canvas.bind("<ButtonPress-1>", eventos.gerenciar_clique)
eventos.canvas.bind("<B1-Motion>", eventos.atualizar_figura_nova)
eventos.canvas.bind("<ButtonRelease-1>", eventos.incluir_figura_nova)
eventos.canvas.bind("<Double-Button-1>", eventos.finalizar_poligono)

root.mainloop()
