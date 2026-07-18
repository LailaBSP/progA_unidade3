from controlador.estado.estado import Estado
from modelo.figuras import Retangulo

class EstadoRetangulo(Estado):
    """Representa o estado de construção de uma figura do tipo Retângulo.

    Gerencia o ciclo de vida da criação de um retângulo na tela através dos 
    eventos de mouse, interagindo diretamente com o modelo e a visão.

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador.ControladorDesenho
    @see modelo.figuras.Retangulo
    @since 1.0
    """

    def __init__(self, controlador):
        """Inicializa o estado do retângulo com uma referência ao controlador principal.

        @param controlador O controlador de desenho que gerencia o estado.
        """
        self.controlador = controlador

    def mouse_pressionado(self, event):
        """Cria uma nova instância de Retângulo com base nas coordenadas iniciais do clique.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição x e y inicial do mouse.
        """
        self.controlador.modelo.figura_nova = Retangulo(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        """Atualiza as dimensões delimitadoras do retângulo conforme o mouse é arrastado.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        """Finaliza o retângulo atual, adicionando-o ao modelo caso esteja válido.

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
        """Método não utilizado para a ferramenta de Retângulo.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        """
        pass