'''
este arquivo é somete para ler o arquivo abc.json que é complementar a aula
'''
import json

with open('abc.json', 'r') as file:
    d1_json = file.read() #aqui o código realiza a leitura do dicionário, mas não acontece o acesso as chaves e valores
    d1_json = json.loads(d1_json) #neste ponto volta a ser dicionário

for k,v in d1_json.items():#neste laço for apresentará a chave
    print(k)

    for k1, v1 in v.items(): #neste laço for apresentará a chave e seus valores
        print(k1, v1)
