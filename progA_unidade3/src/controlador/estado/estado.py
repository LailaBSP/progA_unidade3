from abc import ABC, abstractmethod

class Estado(ABC):

    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    @abstractmethod
    def mouse_arrastado(self, event):
        pass

    @abstractmethod
    def mouse_solto(self, event):
        pass

    @abstractmethod
    def duplo_clique(self, event):
        pass