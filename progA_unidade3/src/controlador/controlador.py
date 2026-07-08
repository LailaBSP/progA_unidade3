from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono

class ControladorDesenho:
    def __init__(self, modelo_desenho, visao_janela):
        self.modelo = modelo_desenho
        self.visao = visao_janela

    def gerenciar_clique(self, event, tipo_figura):
        classes_figuras = {
            'Linha': Linha, 'Rabisco': Rabisco, 'Retângulo': Retangulo,
            'Oval': Oval, 'Circulo': Circulo, 'Polígono': Poligono
        }

        if tipo_figura == 'Polígono':
            if self.modelo.figura_nova is None:
                self.modelo.figura_nova = Poligono(event.x, event.y)
            else:
                self.modelo.figura_nova.adicionar_ponto(event.x, event.y)
        else:
            classe = classes_figuras.get(tipo_figura, Linha)
            self.modelo.figura_nova = classe(event.x, event.y)
        
        self.visao.atualizar_tela()

    def atualizar_movimento(self, event):
        if self.modelo.figura_nova:
            self.modelo.figura_nova.atualizar(event.x, event.y)
            self.visao.atualizar_tela()

    def soltar_clique(self, event, tipo_figura):
        if tipo_figura == 'Polígono':
            return

        if self.modelo.figura_nova and not self.modelo.figura_nova.esta_incompleta():
            self.modelo.adicionar_figura(self.modelo.figura_nova)
        self.modelo.figura_nova = None
        self.visao.atualizar_tela()

    def duplo_clique(self, event, tipo_figura):
        if tipo_figura == 'Polígono' and self.modelo.figura_nova:
            if not self.modelo.figura_nova.esta_incompleta():
                self.modelo.adicionar_figura(self.modelo.figura_nova)
            self.modelo.figura_nova = None
            self.visao.atualizar_tela()
