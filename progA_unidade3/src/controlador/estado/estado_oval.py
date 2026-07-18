from controlador.estado.estado import Estado
from modelo.figuras import Oval

class EstadoOval(Estado):
    """Representa o estado de construção de uma figura do tipo Oval.

    Gerencia o ciclo de vida da criação de uma elipse/oval na tela através dos 
    eventos de mouse, interagindo diretamente com o modelo e a visão.

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador_desenho.ControladorDesenho
    @see modelo.figuras.Oval
    @since 1.0
    """

    def __init__(self, controlador):
        """Inicializa o estado da oval com uma referência ao controlador principal.

        @param controlador O controlador de desenho que gerencia o estado.
        """
        self.controlador = controlador

    def mouse_pressionado(self, event):
        """Cria uma nova instância de Oval com base nas coordenadas iniciais do clique.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição x e y inicial do mouse.
        """
        self.controlador.modelo.figura_nova = Oval(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        """Atualiza as dimensões delimitadoras da oval conforme o mouse é arrastado.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        """Finaliza a oval atual, adicionando-a ao modelo caso esteja válida.

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
        """Método não utilizado para a ferramenta de Oval.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        """
        pass
