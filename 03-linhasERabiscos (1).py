from tkinter import *
from tkinter import ttk

COR_BORDA = 'black'
COR_PREENCHIMENTO = 'lightblue'

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova

    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))

    elif tipo_figura_var.get() == 'Rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)])

    elif tipo_figura_var.get() == 'Retângulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y))

    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ("oval", (event.x, event.y, event.x, event.y))

    else:  # Círculo
        figura_nova = ("circulo", (event.x, event.y, event.x, event.y))


# Quando mouse é movido com botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    elif figura_nova[0] == "circulo":
        x1, y1 = figura_nova[1][0], figura_nova[1][1]

        lado = max(abs(event.x - x1), abs(event.y - y1))

        if event.x < x1:
            x2 = x1 - lado
        else:
            x2 = x1 + lado

        if event.y < y1:
            y2 = y1 - lado
        else:
            y2 = y1 + lado

        figura_nova = ("circulo", (x1, y1, x2, y2))

    else:
        figura_nova = (
            figura_nova[0],
            (figura_nova[1][0], figura_nova[1][1], event.x, event.y)
        )

    desenhar_figuras()
    desenhar_figura_nova()


# Quando mouse é solto
def incluir_figura_nova(event):
    if not incompleta(figura_nova):
        figuras.append(figura_nova)

    desenhar_figuras()


# Desenha todas as figuras salvas
def desenhar_figuras():
    canvas.delete("all")

    for fig, values in figuras:

        if fig == "linha":
            canvas.create_line(values, fill=COR_BORDA)

        elif fig == "rabisco":
            canvas.create_line(values, fill=COR_BORDA)

        elif fig == "retangulo":
            canvas.create_rectangle(values, fill=COR_PREENCHIMENTO, outline=COR_BORDA)

        elif fig == "oval":
            canvas.create_oval(values, fill=COR_PREENCHIMENTO, outline=COR_BORDA)

        elif fig == "circulo":
            canvas.create_oval(values, fill=COR_PREENCHIMENTO, outline=COR_BORDA)


# Desenha figura em construção
def desenhar_figura_nova():
    fig, values = figura_nova

    if fig == "linha":
        canvas.create_line(values, dash=(4, 2), fill=COR_BORDA)

    elif fig == "rabisco":
        canvas.create_line(values, dash=(4, 2), fill=COR_BORDA)

    elif fig == "retangulo":
        canvas.create_rectangle(values, dash=(4, 2), outline=COR_BORDA)

    elif fig == "oval":
        canvas.create_oval(values, dash=(4, 2), outline=COR_BORDA)

    elif fig == "circulo":
        canvas.create_oval(values, dash=(4, 2), outline=COR_BORDA)


# Verifica se figura está incompleta
def incompleta(figura):
    fig, values = figura

    if fig == "rabisco":
        return len(values) <= 1

    return (values[0], values[1]) == (values[2], values[3])


# ******** MAIN ******** #

figuras = []
figura_nova = None

root = Tk()
root.title('Exemplo de aplicação')

frame = Frame(root)

paddings = {'padx': 5, 'pady': 5}

# Label
label = ttk.Label(frame, text='Escolha o que vai desenhar:')
label.grid(column=0, row=0, sticky=W, **paddings)

# Menu de opções
tipo_figura_var = StringVar(root)

option_menu = ttk.OptionMenu(
    frame,
    tipo_figura_var,
    'Linha',
    'Linha',
    'Rabisco',
    'Retângulo',
    'Oval',
    'Circulo'
)

option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
