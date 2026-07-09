from modelo import figuras

class Desenho:
    def __init__(self):
        self._figuras = []        
        self.figura_nova = None  

    def adicionar_figura(self, figura):
        self._figuras.append(figura)

    def obter_figuras(self):
        return self._figuras
    
    def limpar_figuras(self):
        self._figuras.clear()

#opcao para salvar o desenho em um arquivo de texto
    def salvar_desenho(nome_arquivo):
        with open(nome_arquivo, "w") as arquivo: #W = write, cria o arquivo se não existir e sobrescreve se existir
            for figura in figuras:
                #Rabisco e poligono possuem vários pontos
                if isinstance(figura, (figuras.Rabisco, figuras.Poligono)):
                    arquivo.write(type(figura).__name__)
                    for x, y in figura.pontos:
                        arquivo.write(f";{x},{y}")
                    arquivo.write("\n")
                #Linha,retângulo,oval e circulo
                else:
                    arquivo.write(
                        f"{type(figura).__name__};"
                        f"{figura.x1};"
                        f"{figura.y1};"
                        f"{figura.x2};"
                        f"{figura.y2}\n"
                    )

    def abrir_figuras(nome_arquivo):
        global figuras
        figuras.clear()
        with open(nome_arquivo, "r") as arquivo: #r = read (leitura)
            for linha in arquivo:
                dados = linha.strip().split(";")
                tipo = dados[0]
                if tipo == "Linha":
                    figura = figuras.Linha(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    figuras.append(figura)
                elif tipo == "Retangulo":
                    figura = figuras.Retangulo(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    figuras.append(figura)
                elif tipo == "Oval":
                    figura = figuras.Oval(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    figuras.append(figura)
                elif tipo == "Circulo":
                    figura = figuras.Circulo(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    figuras.append(figura)
                elif tipo == "Rabisco":
                    primeiro = dados[1].split(",")
                    figura = Rabisco(
                        int(primeiro[0]),
                        int(primeiro[1])
                    )
                    figura.pontos = []
                    for ponto in dados[1:]:
                        x, y = ponto.split(",")
                        figura.pontos.append(
                            (int(x), int(y))
                        )
                    figuras.append(figura)
                elif tipo == "Poligono":
                    primeiro = dados[1].split(",")
                    figura = figuras.Poligono(
                        int(primeiro[0]),
                        int(primeiro[1])
                    )
                    figura.pontos = []
                    for ponto in dados[1:]:
                        x, y = ponto.split(",")
                        figura.pontos.append(
                            (int(x), int(y))
                        )
                    figuras.append(figura)