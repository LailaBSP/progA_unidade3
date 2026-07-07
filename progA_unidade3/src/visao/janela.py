#Interface

from tkinter import *
from tkinter import ttk
from controlador.controlador import (configurar,gerenciar_clique,atualizar_figura_nova,incluir_figura_nova,finalizar_poligono)

def iniciar():
    root = Tk() #criar a janela
    root.title("Projeto UFSProgramação A - IA - 2026")

    frame = Frame(root)
    paddings = {'padx': 5, 'pady': 5}
    frame.pack()

    label = ttk.Label(frame, text='Escolha o que vai desenhar:')
    label.grid(column=0, row=0, sticky=W, **paddings)

    tipo_figura_var = StringVar(root)

    option_menu = ttk.OptionMenu(frame, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Circulo', 'Polígono')
    option_menu.grid(column=1, row=0, sticky=W, **paddings)

    canvas = Canvas(frame, bg='pink', width=600, height=600)
    canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

    configurar(canvas, tipo_figura_var)

    # Cliques do mouse configurados 
    canvas.bind('<ButtonPress-1>', gerenciar_clique)
    canvas.bind('<B1-Motion>', atualizar_figura_nova)
    canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
    canvas.bind('<Double-Button-1>', finalizar_poligono)  # Clique duplo fecha o Polígono

    root.mainloop()