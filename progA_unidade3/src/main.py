from modelo.desenho import Desenho
from visao.janela import JanelaPrincipal
from controlador.controlador import ControladorDesenho

# 1. Instancia o Modelo
modelo = Desenho()

# 2. Instancia a Visão passando o modelo
visao = JanelaPrincipal(modelo)

# 3. Instancia o Controlador integrando ambos
controlador = ControladorDesenho(modelo, visao)

# 4. Conecta o controlador à visão
visao.associar_controlador(controlador)

# 5. Inicia a aplicação
if __name__ == '__main__':
    visao.iniciar()
