from modelo.figuras import (Linha,Rabisco,Retangulo,Oval,Circulo,Poligono)

#estado do desenho
figuras = []
figura_nova = None

#pq as funcoes usam canvas tipo_figura_var
def organizacaoDaVariavel(canvas_recebido, tipo_recebido):
    global canvas, tipo_figura_var
    canvas = canvas_recebido
    tipo_figura_var = tipo_recebido


def gerenciar_clique(event):
    global figura_nova

    tipo = tipo_figura_var.get()

    classes_figuras = {
        'Linha': Linha,
        'Rabisco': Rabisco,
        'Retângulo': Retangulo,
        'Oval': Oval,
        'Circulo': Circulo,
        'Polígono': Poligono
    }

    if tipo == 'Polígono':

        if figura_nova is None:
            figura_nova = Poligono(event.x, event.y)
        else:
            figura_nova.adicionar_ponto(event.x, event.y)

    else:

        classe = classes_figuras.get(tipo, Linha)
        figura_nova = classe(event.x, event.y)

    desenhar_tudo()

def atualizar_figura_nova(event):
   global figura_nova
   if figura_nova:
       figura_nova.atualizar(event.x, event.y)
       desenhar_tudo()

def incluir_figura_nova(event):
   global figura_nova
   tipo = tipo_figura_var.get()
  
   # Polígono não deve terminar no soltar do mouse, apenas no clique duplo
   if tipo == 'Polígono':
       return


   if figura_nova and not figura_nova.esta_incompleta():
       figuras.append(figura_nova)
   figura_nova = None
   desenhar_tudo()

def finalizar_poligono(event):
   global figura_nova
   tipo = tipo_figura_var.get()
  
   if tipo == 'Polígono' and figura_nova:
       if not figura_nova.esta_incompleta():
           figuras.append(figura_nova)
       figura_nova = None
       desenhar_tudo()

def desenhar_tudo():
   canvas.delete("all")
   for fig in figuras:
       fig.desenhar(canvas, tracejado=False)
   if figura_nova:
       figura_nova.desenhar(canvas, tracejado=True)
