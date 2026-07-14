from modelo import figuras

class Desenho:
    """Essa é a classe do Modelo (parte do padrão MVC). Guarda as
    figuras que já foram desenhadas e controla qual figura tá sendo
    criada no momento (ainda incompleta).

    Attributes:
        _figuras: lista com as figuras que já foram confirmadas.
        figura_nova: a figura que tá sendo desenhada agora, ou None se não tiver nenhuma no momento.
    @author Carolina Aragão
    @version 1.0
    @since 1.0
    """
    def __init__(self):
        """Começa sem nenhuma figura desenhada ainda.
        @author Carolina Aragão
        """
        self._figuras = []        
        self.figura_nova = None  

    def adicionar_figura(self, figura):
        """Adiciona uma figura já pronta na lista de figuras.

        @author Carolina Aragão
        @param figura a figura (Linha, Retangulo, Circulo etc) já finalizada.
        """
        self._figuras.append(figura)

    def obter_figuras(self):
         """Retorna todas as figuras que já foram desenhadas.

        @author Lavínia Cerqueira
        @return lista com as figuras do desenho.
        """
         return self._figuras
    
    def limpar_figuras(self):
         """Apaga todas as figuras do desenho, deixando a lista vazia.

         @author Lavínia Cerqueira
         """
         self._figuras.clear()

#opcao para salvar o desenho em um arquivo de texto
    def salvar_desenho(self, nome_arquivo):
        """Salva o desenho num arquivo de texto. Pra Rabisco e
        Poligono salva todos os pontos do traço, porque essas duas
        têm vários pontos; pras outras figuras (Linha, Retangulo,
        Oval, Circulo) salva só as coordenadas x1, y1, x2, y2.

        @author Laila Beatriz
        @param nome_arquivo caminho do arquivo onde o desenho vai ser salvo.
        """
        with open(nome_arquivo, "w") as arquivo: #W = write, cria o arquivo se não existir e sobrescreve se existir
            for figura in self._figuras:
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

    def abrir_figuras(self, nome_arquivo):
        """Lê um arquivo salvo antes e reconstrói as figuras a partir
        dele, olhando o tipo de cada linha (Linha, Retangulo, Oval,
        Circulo, Rabisco ou Poligono).

        @author Laila Beatriz
        @param nome_arquivo caminho do arquivo a ser aberto.
        """
        self._figuras.clear()
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
                    self._figuras.append(figura)
                elif tipo == "Retangulo":
                    figura = figuras.Retangulo(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    self._figuras.append(figura)
                elif tipo == "Oval":
                    figura = figuras.Oval(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    self._figuras.append(figura)
                elif tipo == "Circulo":
                    figura = figuras.Circulo(
                        int(dados[1]),
                        int(dados[2])
                    )
                    figura.atualizar(
                        int(dados[3]),
                        int(dados[4])
                    )
                    self._figuras.append(figura)
                elif tipo == "Rabisco":
                    primeiro = dados[1].split(",")
                    figura = figuras.Rabisco(
                        int(primeiro[0]),
                        int(primeiro[1])
                    )
                    figura.pontos = []
                    for ponto in dados[1:]:
                        x, y = ponto.split(",")
                        figura.pontos.append(
                            (int(x), int(y))
                        )
                    self._figuras.append(figura)
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
                    self._figuras.append(figura)
