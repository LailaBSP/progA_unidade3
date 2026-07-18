#Interface

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Importação dos estados para permitir a troca dinâmica
from controlador.estado.estado_linha import EstadoLinha
from controlador.estado.estado_rabisco import EstadoRabisco
from controlador.estado.estado_retangulo import EstadoRetangulo
from controlador.estado.estado_oval import EstadoOval
from controlador.estado.estado_circulo import EstadoCirculo
from controlador.estado.estado_poligono import EstadoPoligono

class JanelaPrincipal:
    """Essa é a Visão do padrão MVC — a tela que o usuário vê e mexe.
    Monta a janela, o menu de escolher o tipo de figura, os botões de
    Salvar e Abrir, e o canvas onde os desenhos aparecem.

    Attributes:
        modelo: o Desenho cujas figuras vão aparecer na tela.
        controlador: quem trata os eventos do mouse; só fica definido depois, com associar_controlador().
        root: a janela principal do Tkinter.
        canvas: a área onde as figuras são desenhadas.

    @author Laila Beatriz
    @version 1.0
    @see modelo.desenho.Desenho
    @see controlador.controlador.ControladorDesenho
    @since 1.0
    """
    def __init__(self, modelo_desenho):
        """Monta a janela inteira: o menu de tipos de figura, os
        botões Salvar/Abrir e o canvas, e já liga os eventos do mouse
        do canvas com os métodos do controlador (que só vai existir
        de verdade depois, então essas chamadas ficam "esperando" o
        associar_controlador ser chamado).
        
        @author Carolina Aragão 
        @param modelo_desenho o Desenho que vai fornecer as figuras a serem mostradas na tela.
        """
        self.modelo = modelo_desenho
        self.controlador = None 
        
        self.root = Tk()
        self.root.title("Projeto UFS - Programação A")
        
        self.frame = Frame(self.root)
        self.frame.pack()
        
        self.tipo_figura_var = StringVar(self.root, value='Linha')
        
        # Rastreia as mudanças de seleção no menu para alterar o estado do controlador
        self.tipo_figura_var.trace_add("write", self.ao_mudar_ferramenta)
        
        self.option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Circulo', 'Polígono')
        self.option_menu.grid(column=1, row=0, sticky=W, padx=5, pady=5)

        botao_salvar = ttk.Button(
            self.frame,
            text="Salvar",
            command=self.salvar)
        botao_salvar.grid(column=2, row=0, padx=5, pady=5)
        
        botao_abrir = ttk.Button(
            self.frame,
            text="Abrir",
            command=self.abrir)
        botao_abrir.grid(column=3, row=0, padx=5, pady=5)

        self.canvas = Canvas(self.frame, bg='pink', width=600, height=600)
        self.canvas.grid(column=0, row=1, columnspan=2, sticky=W, padx=5, pady=5)

        self.canvas.bind('<ButtonPress-1>', lambda e: self.controlador.gerenciar_clique(e))
        self.canvas.bind('<B1-Motion>', lambda e: self.controlador.atualizar_movimento(e))
        self.canvas.bind('<ButtonRelease-1>', lambda e: self.controlador.soltar_clique(e))
        self.canvas.bind('<Double-Button-1>', lambda e: self.controlador.duplo_clique(e))

    def ao_mudar_ferramenta(self, *args):
        """Método acionado automaticamente quando o usuário escolhe outra ferramenta no menu.
        Muda o estado do controlador conforme a seleção atual.
        """
        if not self.controlador:
            return
            
        selecao = self.tipo_figura_var.get()
        
        if selecao == 'Linha':
            self.controlador.trocar_estado(EstadoLinha(self.controlador))
        elif selecao == 'Rabisco':
            self.controlador.trocar_estado(EstadoRabisco(self.controlador))
        elif selecao == 'Retângulo':
            self.controlador.trocar_estado(EstadoRetangulo(self.controlador))
        elif selecao == 'Oval':
            self.controlador.trocar_estado(EstadoOval(self.controlador))
        elif selecao == 'Circulo':
            self.controlador.trocar_estado(EstadoCirculo(self.controlador))
        elif selecao == 'Polígono':
            self.controlador.trocar_estado(EstadoPoligono(self.controlador))

    def associar_controlador(self, controlador):
        """Liga o controlador na janela. É feito à parte porque o
        controlador só pode ser criado depois que a janela já existe
        (ver main.py).
        
        @author Lavínia Cerqueira
        @param controlador o ControladorDesenho que vai tratar os eventos do mouse e as ações de salvar/abrir.
        """
        self.controlador = controlador

    def atualizar_tela(self):
        """Redesenha tudo: limpa o canvas e desenha de novo todas as
        figuras que já estão no modelo, incluindo a que tá sendo
        criada no momento (mostrada em modo tracejado, como prévia).

        @author Lavínia Cerqueira 
        """
        self.canvas.delete("all")
        for fig in self.modelo.obter_figuras():
            fig.desenhar(self.canvas, tracejado=False)
        if self.modelo.figura_nova:
            self.modelo.figura_nova.desenhar(self.canvas, tracejado=True)

    def iniciar(self):
        """Inicia o loop principal do Tkinter, deixando a janela
        aberta e escutando os eventos do usuário.
        @author Laila Beatriz
        """
        self.root.mainloop()

    def salvar(self):
        """Chamado quando o usuário clica no botão Salvar. Abre a
        janela padrão do sistema pra escolher onde salvar o arquivo
        de texto e, se um nome for escolhido, manda pro controlador
        salvar o desenho.
        @author Laila Beatriz
        """
        nome_arquivo = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        if nome_arquivo:
            self.controlador.salvar_desenho(nome_arquivo)

    def abrir(self):
        """Chamado quando o usuário clica no botão Abrir. Abre a
        janela padrão do sistema pra escolher o arquivo de texto e,
        se um arquivo for escolhido, manda pro controlador abrir o
        desenho salvo nele.
        @author Laila Beatriz
        """
        nome_arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        if nome_arquivo:
            self.controlador.abrir_desenho(nome_arquivo)
