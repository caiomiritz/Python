-------------------------------------OUTROS BUILTINS-------------------------------------------

Enumerate é uma funcionalidade para fazer sequencias interaveis, sendo um gerador #lazy
Para gerar a lista do enumerate, mostrando o indice e o valor respectivamente

list(enumerate(idades)) -> onde idades é uma lista. 
Podemos dar um unpaking da tupla gerada num for, com 2 variáveis, sendo cada varíavel representando algo da tupla

sequencias dentro de um for enumerado, ou msm tupla, é útil desempacotar os valores. 
Se quizermos ignorar algum valor dessa tupla, basta colocar um "_"

for nome, _, _ in usuarios:   -> cada variável do for representa os valores da tupla, nesse caso estamos ignorando 2
  print(nome)


