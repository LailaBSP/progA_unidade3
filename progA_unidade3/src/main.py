from modelo.desenho import Desenho
from visao.janela import JanelaPrincipal
from controlador.controlador import ControladorDesenho

#Instancia o Modelo
modelo = Desenho()

#Instancia a Visão passando o modelo
visao = JanelaPrincipal(modelo)

#Instancia o Controlador integrando ambos
controlador = ControladorDesenho(modelo, visao)

#Conecta o controlador à visão
visao.associar_controlador(controlador)

#Inicia a aplicação
if __name__ == '__main__':
    visao.iniciar()
