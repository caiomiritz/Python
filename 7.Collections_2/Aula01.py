---------------------CONJUNTOS 'set'-------------------------------

Além das listas, tuplas, temos outras maneiras de fazer conjuntos de valores, objetos, etc
Ex: temos situações que queremos um conjunto de elementos sem repetição, usamos o 'set'

set(listaX) -> nessa situação, transformamos uma lista em um set, nesse caso ele tira os elementos repetidos
para criar um conjunto set, usamos {}, onde o acesso sequencial não é importante, a ordem não importa

uasuarios = {1, 6, 33, 3} -> nesse caso ele fica como {1, 3, 6, 33}

Como não existe posição no conjunto 'set' não conseguimos acessar o "indice" pois não tem ordem, apenas os elementos
assim, nao conseguimos pergar um elemento específico, mas podemos iterar no conjunto, pois ele é um iterável

A união de conjuntos, temos que usar a operação 'ou' -> '|' ex: asuarios | contas -> dessa maneira temos a união deles
a operação '&' ele aparece os elementos que são iguais dos conjuntos
a operação '-' mostra apenas os elementos de um conjunto que não esta no outro
assim como tudo, a documentação mostra outras operações de conjuntos que podemos fazer
