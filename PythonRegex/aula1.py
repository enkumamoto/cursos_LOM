import re

# findall search sub
# compile

string = "Analista de infraestrutura com mais de 5 anos de experiência, \
    iniciei a carreira como estagiário de suporte até chegar a Desenvolvedor IaC.\
    Dentro de minhas experiência aprendi a manter serviços web e ERPs, já na parte \
    de infraestrutura física gerenciava servidores Linux e Windows Servers, além de \
    realizar cabeamento estruturado e análise de requisitos. Como desenvolvedor IaC \
    posso criar, revisar, manter, melhorar Kubernetes, AWS, Terraform, Ansible e \
    outras tecnologias envolvidas. Na AWS, dentro da plataforma meu foco é EC2, S3, \
    CloudWatch, Billing, IAM, EKS e outros. Com um ideal em entender serviços e \
    construir IaC usando Terraform associado ao Ansible. Além de monitorar clusters, \
    containers e instâncias, manter e melhorar o pipeline de CI/CD, melhorar o ambiente \
    de monitoramento utilizando ferramentas como Grafana, aplicar boas práticas de \
    segurança e interagir com outros times de desenvolvimento. Eu sou uma pessoa \
    tranquila e constantemente aprendendo e testando. Continuo estudando cada vez \
    mais sobre virtualização, nuvem e começando a me aventurar em outras tecnologias. \
    Estou sempre testando novos softwares para otimizar suas funções de trabalho e \
    obter resultados diferenciados. No meu tempo livre, dedico-me à minha família, \
    estudos musicais e jogos."

print(re.search(r'IaC', string))
print("---")

print(re.findall(r'IaC', string)) # retorna como lista
print("---")

print(re.sub(r'IaC', 'ABCD', string)) # substitui uma coisa pela outra
print("---")

# lembre-se Teste e teste para regex são coisas distintas, ou seja, o regex distingue letras maiúsculas das minúsculas.

regexp = re.compile(r'IaC')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
print("---")