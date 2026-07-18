from controlador.estado.estado import Estado
from modelo.figuras import Rabisco

class EstadoRabisco(Estado):
    """Representa o estado de construção de uma figura do tipo Rabisco.

    Gerencia o ciclo de vida da criação de um rabisco na tela através
    dos eventos de mouse, interagindo diretamente com o modelo e a visão.

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador.ControladorDesenho
    @see modelo.figuras.Rabisco
    @since 1.0
    """

    def __init__(self, controlador):
        """Inicializa o estado do rabisco.

        @author Laila Beatriz
        @param controlador controlador de desenho.
        """
        self.controlador = controlador

    def mouse_pressionado(self, event):
        """Cria um novo rabisco.

        @author Laila Beatriz
        @param event evento do Tkinter contendo a posição inicial do mouse.
        """
        self.controlador.modelo.figura_nova = Rabisco(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        """Atualiza o rabisco conforme o mouse é movimentado.

        @author Laila Beatriz
        @param event evento do Tkinter contendo a posição atual do mouse.
        """
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        """Finaliza o rabisco e o adiciona ao modelo.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao botão do mouse.
        """
        if self.controlador.modelo.figura_nova and not self.controlador.modelo.figura_nova.esta_incompleta():
            self.controlador.modelo.adicionar_figura(self.controlador.modelo.figura_nova)

        self.controlador.modelo.figura_nova = None
        self.controlador.visao.atualizar_tela()

    def duplo_clique(self, event):
        """O rabisco não utiliza o evento de duplo clique.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao duplo clique.
        """
        pass