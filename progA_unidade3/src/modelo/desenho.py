class Desenho:
    def __init__(self):
        self._figuras = []        
        self.figura_nova = None  

    def adicionar_figura(self, figura):
        self._figuras.append(figura)

    def obter_figuras(self):
        return self._figuras
