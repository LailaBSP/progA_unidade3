from figuras import *


figuras = []
figura_nova = None
canvas = None
tipo_figura_var = None


def desenhar_tudo():
    canvas.delete("all")

    for fig in figuras:
        fig.desenhar(canvas)

    if figura_nova:
        figura_nova.desenhar(canvas, True)


def gerenciar_clique(event):
    global figura_nova

    tipo = tipo_figura_var.get()

    classes = {
        "Linha": Linha,
        "Rabisco": Rabisco,
        "Retângulo": Retangulo,
        "Oval": Oval,
        "Circulo": Circulo,
        "Polígono": Poligono
    }

    if tipo == "Polígono":

        if figura_nova is None:
            figura_nova = Poligono(event.x, event.y)
        else:
            figura_nova.adicionar_ponto(event.x, event.y)

    else:
        figura_nova = classes[tipo](event.x, event.y)

    desenhar_tudo()


def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova:
        figura_nova.atualizar(event.x, event.y)
        desenhar_tudo()


def incluir_figura_nova(event):
    global figura_nova

    if tipo_figura_var.get() == "Polígono":
        return

    if figura_nova and not figura_nova.esta_incompleta():
        figuras.append(figura_nova)

    figura_nova = None
    desenhar_tudo()


def finalizar_poligono(event):
    global figura_nova

    if tipo_figura_var.get() == "Polígono" and figura_nova:

        if not figura_nova.esta_incompleta():
            figuras.append(figura_nova)

        figura_nova = None
        desenhar_tudo()
