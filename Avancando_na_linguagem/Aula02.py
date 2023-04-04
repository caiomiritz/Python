------------------------TUPLES--------------------------------

sabemos que lista, string e ranges são sequencias de valores / caracteres ordenados
compartilham algumas funcionalidades, ex:
len() -> mostra o tamanho d sequencia
min() -> mostra o mínimo da lista
max() -> mostra o maximo

podemos acessar seus índices pelo []
das Sequence Types, apenas list é mutável, str, range e tuple sao imutaveis

na documentação da list, tuple e range: Sequence Type
vamos supor que queremos definir uma lista fixa, inalterável, imutavel. Podemos usar o tuple
ex: dias da semana, em vez das [] colocamos (), também em uma variável

dias_da_semana = ("Segunda", "Terça",....) -> nao podemos mudar seus índices,contudo, como é uma sequence type
ainda podemos usar algumas funcionalidades, menos as que fazem alteração como pop() e del(lista[indice])

--------------------LISTS + TUPLES---------------------------

Dentro da lista, cada elemento pode ser um tuple, podemos armazenar variaveis tuples dentro da lista
Os tuples podem ter valores misturados, como strings e ints dentro
ex: t1, t2, t3 são variaveis tuples com valores dentro
  
lista = [t1, t2, t3] -> 3 tuples dentro dessa lista

Isso é tipo uma matriz, então podemos acessar a tuple que quizermos pelo indice da lista e pelo indice do tuple
ex: lista[0][3] -> acesso ao primeiro tuple na lista e isso acessando a quarta variavel do tuple [3]
  
append(....) -> uma função que coloca um valor dentro de um tuple ou list
tuple(lista) -> função que transforma uma list em um tuple ( retorno da função ), onde devemos armazenar em alguma variavel
list(tuple) -> mesma coisa, mas agora um tuple se transforma em uma lista

Conversao de sequencias imutaveis para mutaveis e vice versa -> ambas as funções são build-in







