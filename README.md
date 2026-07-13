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

• quantidade de métodos documentados;
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
Funções do controlador (6)
configurar()
gerenciar_clique()
atualizar_figura_nova()
incluir_figura_nova()
finalizar_poligono()
desenhar_tudo()
Total: 6 funções
Função da visão (1)
Em janela.py:
iniciar()
Total: 1 função
Total do projeto
18 métodos (classes)
7 funções (controlador.py + janela.py)

## Como visualizar a documentação
A documentação HTML gerada pelo Pydoc está na pasta:

progA_unidade3/docs

Abra o arquivo `index.html` com o navegador. Nessa página existem links
para a documentação de todos os módulos do sistema
