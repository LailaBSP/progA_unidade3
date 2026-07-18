from controlador.estado.estado import Estado
from modelo.figuras import Linha

class EstadoLinha(Estado):
    """Representa o estado de construção de uma figura do tipo Linha.

    Gerencia o ciclo de vida da criação de uma linha na tela através dos 
    eventos de mouse, interagindo diretamente com o modelo e a visão.

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador_desenho.ControladorDesenho
    @see modelo.figuras.Linha
    @since 1.0
    """

    def __init__(self, controlador):
        """Inicializa o estado da linha com uma referência ao controlador principal.

        @param controlador O controlador de desenho que gerencia o estado.
        """
        self.controlador = controlador

    def mouse_pressionado(self, event):
        """Cria uma nova instância de Linha com base nas coordenadas iniciais do clique.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição x e y inicial do mouse.
        """
        self.controlador.modelo.figura_nova = Linha(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        """Atualiza a coordenada final da linha conforme o mouse é arrastado.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        """Finaliza a linha atual, adicionando-a ao modelo caso esteja válida.

        Reseta a referência de nova figura após o processo e solicita a 
        atualização da tela.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao momento em que o botão é solto.
        """
        if self.controlador.modelo.figura_nova and not self.controlador.modelo.figura_nova.esta_incompleta():
            self.controlador.modelo.adicionar_figura(self.controlador.modelo.figura_nova)
        self.controlador.modelo.figura_nova = None
        self.controlador.visao.atualizar_tela()

    def duplo_clique(self, event):
        """Método não utilizado para a ferramenta de Linha.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        """
        pass