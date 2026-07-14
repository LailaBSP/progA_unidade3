from tkinter import *
import abc

COR_BORDA = 'black'
COR_PREENCHIMENTO = 'lightblue'


class Figura(abc.ABC):
    """Classe abstrata que serve de base pra todas as figuras que dá pra
    desenhar no programa (linha, rabisco, retângulo, oval, círculo e
    polígono).

    Ela guarda as coordenadas do primeiro clique (x1, y1) e do ponto
    atual do mouse (x2, y2), que toda figura usa. O método desenhar()
    é abstrato porque cada figura desenha de um jeito diferente no
    canvas, então quem implementa isso são as subclasses.

    Não pode ser instanciada direto, só serve pra ser herdada.

    @author Laila Beatriz
    @version 1.0
    @since 1.0
    """
    def __init__(self, x1, y1):
        """Cria a figura a partir do primeiro clique do usuário.

        No começo x2 e y2 ficam iguais a x1 e y1, porque o usuário
        ainda não arrastou o mouse pra dar tamanho à figura.

        @param x1 coordenada x de onde o usuário clicou.
        @param y1 coordenada y de onde o usuário clicou.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1

    def atualizar(self, x2, y2):
        """Atualiza o ponto final da figura. É chamado toda vez que o
        mouse se move enquanto o usuário tá desenhando.

        @param x2 nova posição x.
        @param y2 nova posição y.
        """
        self.x2 = x2
        self.y2 = y2

    @abc.abstractmethod
    def desenhar(self, canvas, tracejado=False):
        """Desenha a figura no canvas. Método abstrato — cada subclasse
        implementa do seu jeito, já que cada figura tem uma forma
        diferente.

        @param canvas o Canvas do Tkinter onde a figura vai ser desenhada.
        @param tracejado se True, desenha em modo de prévia (tracejado), indicando que a figura ainda tá sendo criada.
        """
        pass

    def esta_incompleta(self):
        """Diz se a figura ainda não foi "desenhada de verdade" — ou
        seja, o usuário só clicou e ainda não arrastou o mouse pra dar
        tamanho a ela.

        @return True se o ponto inicial e o final ainda são iguais; False caso contrário.
        """
        return (self.x1, self.y1) == (self.x2, self.y2)


class Linha(Figura):
    """A figura mais simples: uma linha reta do ponto inicial até o
    ponto final que o usuário arrastou.

    @version 1.0
    @see Figura
    @since 1.0
    """
    def desenhar(self, canvas, tracejado=False):
        """Desenha a linha no canvas.

        @param canvas onde a linha vai ser desenhada.
        @param tracejado se True desenha tracejado (é a prévia enquanto o usuário ainda tá arrastando).
        """
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
    """Desenho livre, tipo quando dá pra desenhar à mão com o mouse.
    Fica guardando todos os pontos por onde o mouse passa enquanto o
    usuário arrasta, formando um traço com vários segmentos.

    @version 1.0
    @see Figura
    @since 1.0
    """
    def __init__(self, x1, y1):
        """Começa o rabisco guardando o primeiro ponto do traço.

        @param x1 coordenada x inicial.
        @param y1 coordenada y inicial.
        """
        super().__init__(x1, y1)
        self.pontos = [(x1, y1)]

    def atualizar(self, x2, y2):
        """Aqui é diferente das outras figuras: em vez de só trocar
        x2 e y2, vai adicionando cada ponto novo numa lista, pra
        formar o traço todo.

        @param x2 coordenada x do novo ponto do traço.
        @param y2 coordenada y do novo ponto do traço.
        """
        self.pontos.append((x2, y2))

    def desenhar(self, canvas, tracejado=False):
        """Desenha o traço ligando todos os pontos guardados. Só
        desenha se tiver mais de um ponto, porque com um ponto só não
        dá pra formar nenhuma linha.

        @param canvas onde o rabisco vai ser desenhado.
        @param tracejado se True desenha o traço tracejado (prévia).
        """
        if len(self.pontos) > 1:
            dash = (4, 2) if tracejado else None
            canvas.create_line(self.pontos, fill=COR_BORDA, dash=dash)

    def esta_incompleta(self):
        """Considera o rabisco incompleto se só tiver 1 ponto (ainda
        não formou traço nenhum).

        @return True se a lista de pontos tiver 1 ou menos.
        """
        return len(self.pontos) <= 1


class Retangulo(Figura):
    """Retângulo desenhado entre o ponto inicial e o ponto final do
    clique/arraste do usuário.

    @version 1.0
    @see Figura
    @since 1.0
    """
    def desenhar(self, canvas, tracejado=False):
        """Desenha o retângulo. Quando tá em modo de prévia (tracejado)
        não preenche com a cor, mostra só o contorno.

        @param canvas onde o retângulo vai ser desenhado.
        @param tracejado se True fica sem preenchimento e com a borda tracejada.
        """
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
    """Oval (elipse) desenhado dentro da área retangular formada pelo
    ponto inicial e pelo ponto final.

    @version 1.0
    @see Figura
    @see Circulo
    @since 1.0
    """
    def desenhar(self, canvas, tracejado=False):
        """Desenha o oval. Igual ao retângulo, em modo de prévia fica
        sem preenchimento.

        @param canvas onde o oval vai ser desenhado.
        @param tracejado se True fica sem preenchimento e tracejado.
        """
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
    """Praticamente igual ao Oval, mas força a largura e a altura
    serem iguais, pra sempre sair um círculo certinho em vez de uma
    elipse torta.

    @author Laila Beatriz
    @version 1.0
    @see Figura
    @see Oval
    @since 1.0
    """
    def atualizar(self, x2, y2):
        """Pega a maior distância entre x e y em relação ao ponto
        inicial e usa esse mesmo valor pros dois lados — é assim que
        força virar um quadrado por baixo dos panos (e por isso o
        oval desenhado dentro sai redondo).

        @author Laila Beatriz
        @param x2 posição x atual do mouse.
        @param y2 posição y atual do mouse.
        """
        lado = max(abs(x2 - self.x1), abs(y2 - self.y1))

        self.x2 = self.x1 - lado if x2 < self.x1 else self.x1 + lado
        self.y2 = self.y1 - lado if y2 < self.y1 else self.y1 + lado

    def desenhar(self, canvas, tracejado=False):
        """Desenha o círculo (na verdade usa create_oval, só que como
        o lado já foi forçado a ser igual, sai redondo).

        @author Laila Beatriz
        @param canvas onde o círculo vai ser desenhado.
        @param tracejado se True fica sem preenchimento e tracejado.
        """
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
    """Polígono com quantos lados o usuário quiser. Diferente das
    outras figuras, não é feito só com um clique e arraste — cada
    clique novo vira um vértice, e só termina quando dá um duplo
    clique.

    @author Laila Beatriz
    @version 1.0
    @see Figura
    @since 1.0
    """
    def __init__(self, x1, y1):
        """Cria o polígono com o primeiro vértice (o primeiro clique
        do usuário).

        @author Laila Beatriz
        @param x1 coordenada x do primeiro vértice.
        @param y1 coordenada y do primeiro vértice.
        """
        super().__init__(x1, y1)
        self.pontos = [(x1, y1)]
        self.x_temp = x1
        self.y_temp = y1

    def atualizar(self, x2, y2):
        """Não mexe nos vértices já confirmados, só guarda onde o
        mouse tá agora (x_temp, y_temp) pra desenhar a linha de
        prévia até a posição atual.

        @author Laila Beatriz
        @param x2 posição x atual do mouse.
        @param y2 posição y atual do mouse.
        """
        self.x_temp = x2
        self.y_temp = y2

    def adicionar_ponto(self, x, y):
        """Confirma um vértice novo no polígono. Chamado a cada clique
        novo do usuário, depois do primeiro (que já é feito no
        construtor).

        @author Laila Beatriz
        @param x coordenada x do vértice novo.
        @param y coordenada y do vértice novo.
        """
        self.pontos.append((x, y))

    def desenhar(self, canvas, tracejado=False):
        """Desenha o polígono. Em modo de prévia (tracejado) desenha
        só as linhas ligando os vértices já confirmados até a posição
        atual do mouse. Fora disso, desenha o polígono fechado e
        preenchido.

        @author Laila Beatriz
        @param canvas onde o polígono vai ser desenhado.
        @param tracejado se True mostra só o contorno em construção, ainda aberto.
        """
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
        """Um polígono precisa de pelo menos 3 pontos pra fechar uma
        área, então considera incompleto enquanto tiver menos que
        isso.

        @author Laila Beatriz 
        @return True se tiver menos de 3 vértices.
        """
        return len(self.pontos) < 3
