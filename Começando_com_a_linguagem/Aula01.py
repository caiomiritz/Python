
#----------------------------PRINT----------------------------

print("mensagem") -> comando basico de print
'sep' é um parametro que é o separardor de cada um dos comentarios dentro do print

print("Caio", "Raphaelli", sep="-") -> esse aqui é o separador. o printf vai sair assim: Caio-Raphaelli
por padrão, o espaço é a separação de cada um
Caio e Raphaelli são os valores, são separados pelo hífen por causa do separador

print("Caio", "Raphaelli", end="\n") -> end é um parametro para demonstrar o que acontece no final da execução do print

#---------------------------VARIAVEIS------------------------

definimos valores fora de alguma execução, como o python nao tem tipagem forte, ele é dinamico, nao precisa colocar o tipo

pais = "Italia" -> aqui essa variavel pais, recebe a string Italia
type(pais) -> esse type mostra o tipo que esse variavel armazenou, no caso uma string

quantidade = 4 -> aqui ele recebe um inteiro 4
type(quantidade) -> vai pritar um int pois ele sabe que é um inteiro

usando a variavel dentro de um print -> print(pais, "ganhou", quantidade, "titulos mundiais"): Italia ganhou 4 titulos mundiais
como esse print nao tem o parametro 'sep', por padrao os valores sao separados por espaço

ex: vamos colocar uma data, criamos variaveis para dia, mes e ano, seguindo o print -> print(dia, mes, ano, sep="/")

OBS: nao é possivel declarar uma variavel estatica no python, obrigatoriarmente precisamos definir um valor inicial para a variavel
ex: int cidade; -> uma variavel estatica em C++ que nao recebeu algum valor

seguiremos o padrão Snake_Case para declarar variaveis. 
ex: Nome_Completo (nome da viarial composta, separada por _)

