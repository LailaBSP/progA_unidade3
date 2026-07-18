from controlador.estado.estado import Estado
from modelo.figuras import Poligono


class EstadoPoligono(Estado):
    """Representa o estado de construção de uma figura do tipo Polígono.

    Gerencia o ciclo de vida da criação de um polígono na tela através dos
    eventos de mouse, interagindo diretamente com o modelo e a visão.
    Diferente da Linha, o Polígono é construído por múltiplos cliques
    (um por vértice) e finalizado apenas no duplo clique.

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador_desenho.ControladorDesenho
    @see modelo.figuras.Poligono
    @since 1.0
    """

    def __init__(self, controlador):
        """Inicializa o estado do polígono com uma referência ao controlador principal.

        @param controlador O controlador de desenho que gerencia o estado.
        """
        self.controlador = controlador

    def mouse_pressionado(self, event):
        """Cria um novo polígono no primeiro clique ou adiciona um vértice
        nos cliques seguintes.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição x e y do clique.
        """
        if self.controlador.modelo.figura_nova is None:
            self.controlador.modelo.figura_nova = Poligono(event.x, event.y)
        else:
            self.controlador.modelo.figura_nova.adicionar_ponto(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        """Atualiza a posição de prévia (x_temp, y_temp) conforme o mouse
        se move, sem confirmar nenhum vértice novo.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        """Método não utilizado para a ferramenta de Polígono, pois a
        confirmação de vértices ocorre no clique, não ao soltar o botão.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao momento em que o botão é solto.
        """
        pass

    def duplo_clique(self, event):
        """Finaliza o polígono atual, adicionando-o ao modelo caso já
        tenha pelo menos 3 vértices, e reseta a referência de nova figura.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        """
        if self.controlador.modelo.figura_nova and not self.controlador.modelo.figura_nova.esta_incompleta():
            self.controlador.modelo.adicionar_figura(self.controlador.modelo.figura_nova)
        self.controlador.modelo.figura_nova = None
        self.controlador.visao.atualizar_tela()
