from tkinter import Canvas
from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono
from controlador.estado.estado_linha import EstadoLinha

class ControladorDesenho:
    """Este é o Controlador do padrão MVC. 
    
    Atua como intermediário entre a tela (visão) e o modelo, tratando os 
    eventos de mouse (clique, arrastar, soltar, duplo clique) e transformando-os 
    em ações sobre as figuras do modelo.

    Attributes:
        modelo: O Desenho que armazena as figuras do sistema.
        visao: A JanelaPrincipal que exibe a tela para o usuário.

    @author Laila Beatriz
    @version 1.0
    @see modelo.desenho.Desenho
    @see visao.janela.JanelaPrincipal
    @since 1.0
    """

    def __init__(self, modelo_desenho, visao_janela):
        """Armazena as referências do modelo e da visão que o controlador vai utilizar.

        @param modelo_desenho O Desenho usado no programa.
        @param visao_janela A JanelaPrincipal usada no programa.
        """
        self.modelo = modelo_desenho
        self.visao = visao_janela
        self.estado = EstadoLinha(self)

    def gerenciar_clique(self, event):
        """Encaminha o evento do primeiro clique do mouse para o estado atual do controlador.

        O estado ativo é responsável por decidir como tratar o clique, de acordo 
        com a ferramenta selecionada (Linha, Rabisco, Retângulo, Oval, Círculo ou Polígono).

        @author Laila Beatriz
        @param event Evento do Tkinter com as coordenadas do clique (event.x, event.y).
        """
        self.estado.mouse_pressionado(event)

    def atualizar_movimento(self, event):
        """Chamado continuamente enquanto o mouse se move com o botão pressionado.

        Atualiza em tempo real a figura que está sendo criada no momento.

        @author Laila Beatriz
        @param event Evento do Tkinter contendo a posição atual do mouse.
        """
        self.estado.mouse_arrastado(event)

    def soltar_clique(self, event):
        """Chamado quando o usuário solta o botão do mouse para finalizar a figura.

        Neste momento, a figura concluída é enviada para o modelo. A única exceção 
        é o Polígono, que exige um duplo clique para ser finalizado; portanto, 
        este método não realiza ações para esse caso.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao momento em que o botão é solto.
        """
        self.estado.mouse_solto(event)

    def duplo_clique(self, event):
        """Trata o evento de duplo clique para fechamento de geometrias complexas.

        Atua especificamente quando o tipo de figura é 'Polígono', momento em que 
        conclui o polígono em construção e o envia para o modelo.

        @author Laila Beatriz
        @param event Evento do Tkinter associado ao duplo clique.
        """
        self.estado.duplo_clique(event)

    def salvar_desenho(self, nome_arquivo):
        """Solicita ao modelo a exportação e salvamento das figuras em um arquivo.

        @author Laila Beatriz
        @param nome_arquivo Caminho ou nome do arquivo de destino.
        """
        self.modelo.salvar_desenho(nome_arquivo)

    def abrir_desenho(self, nome_arquivo):
        """Solicita ao modelo a leitura de um arquivo salvo e atualiza a interface de exibição.

        @author Laila Beatriz
        @param nome_arquivo Caminho ou nome do arquivo a ser lido.
        """
        self.modelo.abrir_figuras(nome_arquivo)
        self.visao.atualizar_tela()

    def trocar_estado(self, novo_estado):
        """Modifica o estado atual do controlador para gerenciar uma nova ferramenta.

        @author Laila Beatriz
        @param novo_estado A nova instância de Estado que assumirá o controle das ações.
        """
        self.estado = novo_estado
