# Classe Figura e subclasses

from tkinter import *
import abc

COR_BORDA = 'black'
COR_PREENCHIMENTO = 'lightblue'


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

        canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=COR_BORDA,
            dash=dash
        )


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

        canvas.create_rectangle(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=preenchimento,
            outline=COR_BORDA,
            dash=dash
        )


class Oval(Figura):

    def desenhar(self, canvas, tracejado=False):

        dash = (4, 2) if tracejado else None
        preenchimento = None if tracejado else COR_PREENCHIMENTO

        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=preenchimento,
            outline=COR_BORDA,
            dash=dash
        )


class Circulo(Figura):

    def atualizar(self, x2, y2):

        lado = max(abs(x2 - self.x1), abs(y2 - self.y1))

        self.x2 = self.x1 - lado if x2 < self.x1 else self.x1 + lado
        self.y2 = self.y1 - lado if y2 < self.y1 else self.y1 + lado

    def desenhar(self, canvas, tracejado=False):

        dash = (4, 2) if tracejado else None
        preenchimento = None if tracejado else COR_PREENCHIMENTO

        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=preenchimento,
            outline=COR_BORDA,
            dash=dash
        )


class Poligono(Figura):

    def __init__(self, x1, y1):
        super().__init__(x1, y1)
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
                canvas.create_line(
                    lista,
                    fill=COR_BORDA,
                    dash=dash
                )
            else:
                canvas.create_polygon(
                    lista,
                    outline=COR_BORDA,
                    fill=COR_PREENCHIMENTO
                )

    def esta_incompleta(self):
        return len(self.pontos) < 3