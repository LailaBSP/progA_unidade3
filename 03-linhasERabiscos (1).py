from tkinter import *
from tkinter import ttk
import abc

COR_BORDA = 'black'
COR_PREENCHIMENTO = 'lightblue'

# --- Classes das Figuras (POO) ---

class Figura(abc.ABC):
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1

    def atualizar(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    @abc.abstractmethod
    def desenhar(self, canvas, tracejado=False):
        pass

    def esta_incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


class Linha(Figura):
    def desenhar(self, canvas, tracejado=False):
        dash = (4, 2) if tracejado else None
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=COR_BORDA, dash=dash)


class Rabisco(Figura):
    def __init__(self, x1, y1):
        super().__init__(x1, y1)
        self.pontos = [(x1, y1)]

    def atualizar(self, x2, y2):
        self.pontos.append((x2, y2))

    def desenhar(self, canvas, tracejado=False):
        if len(self.pontos) > 1:
            dash = (4, 2) if tracejado else None
            canvas.create_line(self.pontos, fill=COR_BORDA, dash=dash)

    def esta_incompleta(self):
        return len(self.pontos) <= 1


class Retangulo(Figura):
    def desenhar(self, canvas, tracejado=False):
        dash = (4, 2) if tracejado else None
        preenchimento = None if tracejado else COR_PREENCHIMENTO
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                                fill=preenchimento, outline=COR_BORDA, dash=dash)


class Oval(Figura):
    def desenhar(self, canvas, tracejado=False):
        dash = (4, 2) if tracejado else None
        preenchimento = None if tracejado else COR_PREENCHIMENTO
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                            fill=preenchimento, outline=COR_BORDA, dash=dash)


class Circulo(Figura):
    def atualizar(self, x2, y2):
        lado = max(abs(x2 - self.x1), abs(y2 - self.y1))
        self.x2 = self.x1 - lado if x2 < self.x1 else self.x1 + lado
        self.y2 = self.y1 - lado if y2 < self.y1 else self.y1 + lado

    def desenhar(self, canvas, tracejado=False):
        dash = (4, 2) if tracejado else None
        preenchimento = None if tracejado else COR_PREENCHIMENTO
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                            fill=preenchimento, outline=COR_BORDA, dash=dash)


# --- Controle dos Eventos (Mouse) ---

def iniciar_figura_nova(event):
    global figura_nova
    tipo = tipo_figura_var.get()

    classes_figuras = {
        'Linha': Linha,
        'Rabisco': Rabisco,
        'Retângulo': Retangulo,
        'Oval': Oval,
        'Circulo': Circulo
    }

    classe_escolhida = classes_figuras.get(tipo, Linha)
    figura_nova = classe_escolhida(event.x, event.y)


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova:
        figura_nova.atualizar(event.x, event.y)
        desenhar_tudo()


def incluir_figura_nova(event):
    global figura_nova
    if figura_nova and not figura_nova.esta_incompleta():
        figuras.append(figura_nova)
    figura_nova = None
    desenhar_tudo()


def desenhar_tudo():
    canvas.delete("all")
    for fig in figuras:
        fig.desenhar(canvas, tracejado=False)
    if figura_nova:
        figura_nova.desenhar(canvas, tracejado=True)


# --- Inicialização da Interface ---

figuras = []
figura_nova = None

root = Tk()
# Título atualizado
root.title('Projeto UFS - Programação A - IA - 2026')

frame = Frame(root)
paddings = {'padx': 5, 'pady': 5}

# Texto e Menu de opções
label = ttk.Label(frame, text='Escolha o que vai desenhar:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(
    frame, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Circulo'
)
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área do desenho modificada para rosa (pink)
canvas = Canvas(frame, bg='pink', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Cliques do mouse
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
