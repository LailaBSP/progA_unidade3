from tkinter import *
from tkinter import ttk
import abc

COR_BORDA = 'black'
COR_PREENCHIMENTO = 'lightblue'

# --- Classes das Figuras (POO) ---

class Figura(abc.ABC):
    def _init_(self, x1, y1):
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
    def _init_(self, x1, y1):
        super()._init_(x1, y1)
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


class Poligono(Figura):
    def _init_(self, x1, y1):
        super()._init_(x1, y1)
        self.pontos = [(x1, y1)]
        self.x_temp = x1
        self.y_temp = y1

    def atualizar(self, x2, y2):
        self.x_temp = x2
        self.y_temp = y2

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas, tracejado=False):
        dash = (4, 2) if tracejado else None
        pontos = self.pontos.copy()

        if tracejado:
            pontos.append((self.x_temp, self.y_temp))

        if len(pontos) > 1:
            lista = []
            for p in pontos:
                lista.extend(p)

            if tracejado:
                canvas.create_line(lista, fill=COR_BORDA, dash=dash)
            else:
                canvas.create_polygon(lista, outline=COR_BORDA, fill=COR_PREENCHIMENTO)

    def esta_incompleta(self):
        return len(self.pontos) < 3

# --- Controle dos Eventos (Mouse) ---

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
        classe_escolhida = classes_figuras.get(tipo, Linha)
        figura_nova = classe_escolhida(event.x, event.y)
    
    desenhar_tudo()


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova:
        figura_nova.atualizar(event.x, event.y)
        desenhar_tudo()


def incluir_figura_nova(event):
    global figura_nova
    tipo = tipo_figura_var.get()
    
    if tipo == 'Polígono':
        return

    if figura_nova and not figura_nova.esta_incompleta():
        figuras.append(figura_nova)
    figura_nova = None
    desenhar_tudo()


def finalizar_poligono(event):
    global figura_nova
    tipo = tipo_figura_var.get()
    
    if tipo == 'Polígono' and figura_nova:
        if not figura_nova.esta_incompleta():
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
root.title('Projeto UFS - Programação A - IA - 2026')

frame = Frame(root)
paddings = {'padx': 5, 'pady': 5}

label = ttk.Label(frame, text='Escolha o que vai desenhar:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(
    frame, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Circulo', 'Polígono'
)
option_menu.grid(column=1, row=0, sticky=W, **paddings)

canvas = Canvas(frame, bg='pink', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Cliques do mouse 
canvas.bind('<ButtonPress-1>', gerenciar_clique)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
canvas.bind('<Double-Button-1>', finalizar_poligono)  

root.mainloop()
