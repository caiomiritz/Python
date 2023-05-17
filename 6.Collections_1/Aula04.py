-------------------------------------OUTROS BUILTINS-------------------------------------------

Enumerate é uma funcionalidade para fazer sequencias interaveis, retornando um iterador #lazy
Para gerar a lista do enumerate, mostrando o indice e o valor respectivamente

list(enumerate(idades)) -> onde idades é uma lista, e esse retorno é uma lista de tuplas
Podemos dar um unpaking da tupla gerada num for, com 2 variáveis, sendo cada varíavel representando algo da tupla

sequencias dentro de um for enumerado, ou msm tupla, é útil desempacotar os valores. 
Se quizermos ignorar algum valor dessa tupla, basta colocar um "_"

for nome, _, _ in usuarios:   -> cada variável do for representa os valores da tupla, nesse caso estamos ignorando 2
  print(nome)

------------------------------ORDENAÇÃO----------------------------------

sorted(lista) -> devolve uma ordenação dentro da lista, comparando os valores, dentro do parametro podemos colocar reversed=True
reversed(lista) -> faz a mesma coisa, mas ao contrário de sorted() ele não retorna uma lista como o sorted(), mas sim devolve um iterador #lazy

Claro, a prórpia lista tem métodos que fazem isso, contudo list.sort() ordena diretamente a lista, ja que é mutável
diferente do sorted() ela não retorna nada, apenas altera no local (inplace) a lista

