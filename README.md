# progA_unidade3

# Projeto da Terceira Unidade

Neste projeto será elaborado um programa para construir desenhos no estilo das apps **Google Drawings** e **LibreOffice Draws**.

O projeto deverá utilizar o **Tkinter**, a biblioteca padrão de Python para construção de GUIs. Dia **22/06/26** será disponibilizada uma implementação inicial do projeto, simples e incompleta, estruturada imperativamente.

O projeto deverá ser desenvolvido em equipes de dois ou três alunos (preferencialmente três). Serão dadas tarefas específicas para serem feitas no código do projeto. Essas tarefas serão cobradas gradualmente na forma de entregas feitas em dias pré-determinados.

## Entre outras coisas, as equipes deverão:

* Refatorar o projeto para uma estrutura de programa Orientada a Objetos.
* Adicionar funcionalidades.
* Aplicar alguns padrões arquiteturas e de projeto.
* Desenvolver o sistema utilizando as ferramentas Git e Github para trabalho colaborativo.

As entregas devem ser feitas criando **tags de versionamento** do projeto no Git/Github.

* Algumas entregas exigirão o registro de commits individuais no Github.
* Atrasos nas entregas serão penalizados. Cada dia de atraso tirará **0,5 pontos**.

---

# Etapa 1

* Leitura sobre Git e GitHub.
* Estudo sobre Tkinter.
* Criação do projeto no GitHub.
* A partir do código inicialmente dado, adicionar funcionalidades que permitam:

  * Desenhar retângulos.
  * Desenhar ovais.
  * Desenhar círculos.
  * Que os desenhos individuais possam ter bordas com cor.
  * Que os desenhos individuais possam ter cor de preenchimento.

## Material de estudo sobre Tkinter

### Tutoriais

* TKinter tutorial: https://www.pythontutorial.net/tkinter/
* Python GUI Programming: Your Tkinter Tutorial: https://realpython.com/python-gui-tkinter/
* Tkinter Canvas. Disponível em: https://www.pythontutorial.net/tkinter/tkinter-canvas/

### Manuais de referência

* TKinter — Python interface to Tcl/Tk. Disponível em: https://docs.python.org/3/library/tkinter.html
* Graphical user interfaces with Tk. Disponível em: https://docs.python.org/3/library/tk.html
* Canvas. Disponível em: https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html

## Material de estudo sobre Git e GitHub

* Manual de referência do Git: https://git-scm.com/docs
* Documentação do Github: https://docs.github.com/en

### Entrega

**27/06/26** — Tag: `imperativa.1`

---

# Etapa 2

Refatorar o sistema para que siga uma abordagem Orientada a Objetos:

* Definir uma hierarquia de classes (`Figura`) para contemplar os diversos tipos de desenhos: retângulos, mão livre, etc.
* Adequar o programa para utilizar a hierarquia de figuras (`Figura`).
* Adicionar desenhos de polígonos.
* Separar o código em módulos (Classe `Figura` e subclasses em um arquivo separado, por exemplo).

### Entrega

**01/07/26** — Tag: `OO.1`

---

# Etapa 3

Refatorar para o padrão MVC:

* Definir as classes do modelo (Figuras, Desenho, ...).
* Definir uma classe ou classes para a visão.
* Definir uma classe ou classes para o(s) controlador(es).

## Recomendação

Usar a seguinte estrutura de arquivos e pastas:

```text
nome-do-projeto/
├── .git/                     # Controlado pelo Git
├── .gitignore                # Arquivos e pastas ignorados pelo Git
├── src/                      # Código-fonte principal do projeto
│   └── nome_do_projeto/      # Pacote Python
│       ├── main.py           # O programa principal
│       ├── modelo/           # Classes do Model
│       │   └── ...
│       ├── visao/            # Classes da View
│       │   └── ...
│       └── controlador/      # Classes Controllers
│           └── ...
```

### Entrega

**08/07/26** — Tag: `OO.MVC.1`

---

## Observação

Demais etapas e entregas serão especificadas nesse documento ao longo do projeto.
