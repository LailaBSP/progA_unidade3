from tkinter import Canvas
from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono

class ControladorDesenho:
    """Essa é o Controlador do padrão MVC. Fica entre a tela (visão) e
    o modelo, tratando os eventos de mouse (clique, arrastar, soltar,
    duplo clique) e transformando isso em ações sobre as figuras do
    modelo.

    Attributes:
        modelo: o Desenho que guarda as figuras do sistema.
        visao: a JanelaPrincipal que mostra a tela pro usuário.

    @author Laila Beatriz
    @version 1.0
    @see modelo.desenho.Desenho
    @see visao.janela.JanelaPrincipal
    @since 1.0
    """
    def __init__(self, modelo_desenho, visao_janela):
        """Guarda as referências do modelo e da visão que o controlador
        vai usar.

        @param modelo_desenho o Desenho usado no programa.
        @param visao_janela a JanelaPrincipal usada no programa.
        """
        self.modelo = modelo_desenho
        self.visao = visao_janela
        self.estado_atual = None  

    def gerenciar_clique(self, event, tipo_figura):
        """Encaminha o evento do primeiro clique do mouse para o estado
        atual do controlador.

        O estado ativo é responsável por decidir como tratar o clique,
        de acordo com a ferramenta selecionada (Linha, Rabisco,
        Retângulo, Oval, Círculo ou Polígono).

        @author Laila Beatriz
        @param event evento do Tkinter com as coordenadas do clique (event.x, event.y).
        @param tipo_figura tipo da ferramenta selecionada no menu.
        """
        self.estado.mouse_pressionado(event, tipo_figura)

    def atualizar_movimento(self, event):
        """Chamado continuamente enquanto o mouse se move com o botão pressionado.

        Atualiza em tempo real a figura que está sendo criada no momento.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        self.estado.mouse_arrastado(event)

    def soltar_clique(self, event, tipo_figura):
        """Chamado quando o usuário solta o botão do mouse para finalizar a figura.

        Neste momento, a figura concluída é enviada para o modelo. A única exceção 
        é o Polígono, que exige um duplo clique para ser finalizado; portanto, 
        este método não realiza ações para esse caso.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao momento em que o botão é solto.
        @param tipo_figura O tipo da figura que estava sendo desenhada.
        """
        self.estado.mouse_solto(event)

    def duplo_clique(self, event, tipo_figura):
        """Trata o evento de duplo clique para fechamento de geometrias complexas.

        Atua especificamente quando o tipo de figura é 'Polígono', momento em que 
        conclui o polígono em construção e o envia para o modelo.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        @param tipo_figura Tipo da figura sendo criada (comportamento restrito a 'Polígono').
        """
        self.estado.duplo_clique(event)

    def salvar_desenho(self, nome_arquivo):
        """Chama o modelo pra salvar as figuras num arquivo.

        @author Laila Beatriz
        @param nome_arquivo caminho ou nome do arquivo onde vai salvar.
        """
        self.modelo.salvar_desenho(nome_arquivo)

    def abrir_desenho(self, nome_arquivo):
        """Chama o modelo pra abrir um arquivo salvo antes, e depois
        atualiza a tela pra mostrar as figuras carregadas.

        @author Laila Beatriz
        @param nome_arquivo caminho ou nome do arquivo a ser lido.
        """
        self.modelo.abrir_figuras(nome_arquivo)
        self.visao.atualizar_tela()

    def trocar_estado(self, novo_estado):
        """Troca o estado atual do controlador para o novo estado.

        @author Laila Beatriz
        @param novo_estado a nova instância de Estado que vai ser usada.
        """
        self.estado_atual = novo_estado
