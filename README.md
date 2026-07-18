Projeto UFS - Programação A

## Integrantes
- Laila Beatriz de Souza Pereira
- Lavínia Almeida Cerqueira dos Santos
- Carolina Aragão Céu Melo

## Descrição do sistema
Este projeto consiste no desenvolvimento de um programa para criação de desenhos, inspirado em aplicativos como Google Drawings e LibreOffice Draw. A aplicação foi desenvolvida em Python utilizando a biblioteca Tkinter para a construção da interface gráfica (GUI). O sistema permite ao usuário desenhar diferentes figuras geométricas, como linhas, rabiscos, retângulos, ovais, círculos e polígonos, por meio da interação com o mouse. O sistema também permite salvar o desenho em um arquivo de texto e abrir o mesmo desenho depois.

## Quantidade de classes documentadas
1. Figura
2. Linha
3. Rabisco
4. Retangulo
5. Oval
6. Circulo
7. Poligono
8. Desenho
9. ControladorDesenho
10. JanelaPrincipal

## Quantidade de métodos documentados
Métodos das classes (18)
Classe Figura (4)
__init__()
atualizar()
desenhar()
esta_incompleta()
Classe Linha (1)
desenhar()
Classe Rabisco (4)
__init__()
atualizar()
desenhar()
esta_incompleta()
Classe Retangulo (1)
desenhar()
Classe Oval (1)
desenhar()
Classe Circulo (2)
atualizar()
desenhar()
Classe Poligono (5)
__init__()
atualizar()
adicionar_ponto()
desenhar()
esta_incompleta()
Total: 18 métodos

Funções do controlador (8)
Em controlador.py:
__init__()
gerenciar_clique()
atualizar_movimento()
soltar_clique()
duplo_clique()
salvar_desenho()
abrir_desenho()
trocar_estado()
Total: 8 funções

Funções da visão (7)
Em janela.py:
__init__()
ao_mudar_ferramenta()
associar_controlador()
atualizar_tela()
iniciar()
salvar()
abrir()
Total: 7 funções

Total do projeto
18 métodos (classes de figuras e desenho)
15 funções/métodos (controlador.py + janela.py)

## Como visualizar a documentação
A documentação HTML gerada pelo Pydoc está na pasta:

progA_unidade3/docs

Abra o arquivo `index.html` com o navegador. Nessa página existem links
para a documentação de todos os módulos do sistema
