from abc import ABC, abstractmethod

class Estado(ABC):
    """Classe abstrata que representa um estado do controlador de desenho.

    Cada estado define como o controlador deve reagir aos eventos do
    mouse para uma ferramenta específica (Linha, Rabisco, Retângulo,
    Oval, Círculo ou Polígono).

    @author Laila Beatriz
    @version 1.0
    @see controlador.controlador.ControladorDesenho
    @since 1.0
    """

    @abstractmethod
    def mouse_pressionado(self, event):
        """Trata o evento de pressionar o botão do mouse.

        @author Laila Beatriz
        @param event evento do Tkinter contendo as coordenadas do clique.
        """
        pass

    @abstractmethod
    def mouse_arrastado(self, event):
        """Trata o movimento do mouse com o botão pressionado.

        @author Laila Beatriz
        @param event evento do Tkinter contendo a posição atual do mouse.
        """
        pass

    @abstractmethod
    def mouse_solto(self, event):
        """Trata o evento de soltar o botão do mouse.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao término da interação.
        """
        pass

    @abstractmethod
    def duplo_clique(self, event):
        """Trata o evento de duplo clique do mouse.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao duplo clique.
        """
        pass
