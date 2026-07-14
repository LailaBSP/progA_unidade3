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

    def gerenciar_clique(self, event, tipo_figura):
        """Trata o primeiro clique do mouse, criando uma figura nova
        do tipo escolhido no menu.

        O Polígono é tratado diferente: cada clique novo adiciona um
        vértice na figura, em vez de criar uma figura do zero a cada
        clique (só cria uma nova no primeiro clique, quando ainda não
        tem nenhum polígono em construção).

        @author Laila Beatriz
        @param event evento do Tkinter com as coordenadas do clique (event.x, event.y).
        @param tipo_figura o tipo escolhido no menu ('Linha', 'Rabisco', 'Retângulo', 'Oval', 'Circulo' ou 'Polígono').
        """
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
        """Chamado toda vez que o mouse se move com o botão apertado.
        Vai atualizando a figura que tá sendo criada no momento.

        @param event evento do Tkinter com a posição atual do mouse.
        """
        if self.modelo.figura_nova:
            self.modelo.figura_nova.atualizar(event.x, event.y)
            self.visao.atualizar_tela()

    def soltar_clique(self, event, tipo_figura):
        """Chamado quando o usuário solta o botão do mouse — é aqui
        que a figura é finalizada e vai pro modelo. Exceção é o
        Polígono, que só termina no duplo clique, então esse método
        não faz nada nesse caso.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao soltar do clique.
        @param tipo_figura tipo da figura que tava sendo criada.
        """
        if tipo_figura == 'Polígono':
            return

        if self.modelo.figura_nova and not self.modelo.figura_nova.esta_incompleta():
            self.modelo.adicionar_figura(self.modelo.figura_nova)
        self.modelo.figura_nova = None
        self.visao.atualizar_tela()

    def duplo_clique(self, event, tipo_figura):
        """Só faz alguma coisa quando o tipo é 'Polígono' — é o duplo
        clique que fecha o polígono em construção e manda ele pro
        modelo.

        @author Laila Beatriz
        @param event evento do Tkinter associado ao duplo clique.
        @param tipo_figura tipo da figura sendo criada (só funciona quando é 'Polígono').
        """
        if tipo_figura == 'Polígono' and self.modelo.figura_nova:
            if not self.modelo.figura_nova.esta_incompleta():
                self.modelo.adicionar_figura(self.modelo.figura_nova)
            self.modelo.figura_nova = None
            self.visao.atualizar_tela()

    def salvar_figuras(nome_arquivo):
        """Chama o modelo pra salvar as figuras num arquivo.

        @author Laila Beatriz
        @param nome_arquivo caminho ou nome do arquivo onde vai salvar.
        """
        self.modelo.salvar_figuras(nome_arquivo)

    def abrir_figuras(nome_arquivo):
        """Chama o modelo pra abrir um arquivo salvo antes, e depois
        atualiza a tela pra mostrar as figuras carregadas.

        @author Laila Beatriz
        @param nome_arquivo caminho ou nome do arquivo a ser lido.
        """
        self.modelo.abrir_figuras(nome_arquivo)
        self.visao.atualizar_tela()
