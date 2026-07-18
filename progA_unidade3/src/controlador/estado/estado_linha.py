

class EstadoLinha(Estado):
    def mouse_pressionado(self, event):
        self.controlador.modelo.figura_nova = Linha(event.x, event.y)
        self.controlador.visao.atualizar_tela()

    def mouse_arrastado(self, event):
        if self.controlador.modelo.figura_nova:
            self.controlador.modelo.figura_nova.atualizar(event.x, event.y)
            self.controlador.visao.atualizar_tela()

    def mouse_solto(self, event):
        if self.controlador.modelo.figura_nova and not self.controlador.modelo.figura_nova.esta_incompleta():
            self.controlador.modelo.adicionar_figura(self.controlador.modelo.figura_nova)
        self.controlador.modelo.figura_nova = None
        self.controlador.visao.atualizar_tela()

    def duplo_clique(self, event):
        # O duplo clique não é usado aqui
        pass