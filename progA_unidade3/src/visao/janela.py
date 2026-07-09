#Interface

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class JanelaPrincipal:
    def __init__(self, modelo_desenho):
        self.modelo = modelo_desenho
        self.controlador = None 
        
        self.root = Tk()
        self.root.title("Projeto UFS - Programação A")
        
        self.frame = Frame(self.root)
        self.frame.pack()
        
        self.tipo_figura_var = StringVar(self.root, value='Linha')
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

        # Associa os eventos passando as referências para o controlador
        self.canvas.bind('<ButtonPress-1>', lambda e: self.controlador.gerenciar_clique(e, self.tipo_figura_var.get()))
        self.canvas.bind('<B1-Motion>', lambda e: self.controlador.atualizar_movimento(e))
        self.canvas.bind('<ButtonRelease-1>', lambda e: self.controlador.soltar_clique(e, self.tipo_figura_var.get()))
        self.canvas.bind('<Double-Button-1>', lambda e: self.controlador.duplo_clique(e, self.tipo_figura_var.get()))

    def associar_controlador(self, controlador):
        self.controlador = controlador

    def atualizar_tela(self):
        self.canvas.delete("all")
        # Lê as figuras diretamente do modelo
        for fig in self.modelo.obter_figuras():
            fig.desenhar(self.canvas, tracejado=False)
        if self.modelo.figura_nova:
            self.modelo.figura_nova.desenhar(self.canvas, tracejado=True)

    def iniciar(self):
        self.root.mainloop()

    def salvar(self):
        nome_arquivo = filedialog.asksaveasfilename( #abre janela pra escolher onde salvar
            defaultextension=".txt", 
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        if nome_arquivo:
            self.controlador.salvar_desenho(nome_arquivo)


    def abrir(self):
        nome_arquivo = filedialog.askopenfilename( #abre janela pra escolher arquivo
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        if nome_arquivo:
            self.controlador.abrir_desenho(nome_arquivo)
