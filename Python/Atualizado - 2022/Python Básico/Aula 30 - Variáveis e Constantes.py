"""
CONSTANTE = "Variáveis" que não vão mudar
Uma constante no código, por convenção, é escrita em maiúsculo.
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 50  # velocidade atual do carro
local_carro = 100  #local em qeu o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multador_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


if vel_carro_pass_radar_1:
    p("Velocidade carro passou do radar 1.")

if carro_passou_radar_1:
    p("Carro passou radar 1.")

if carro_multador_radar_1:
    p("Carro multado em radar 1.")
