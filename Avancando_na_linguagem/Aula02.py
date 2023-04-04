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

--------------LIST COMPREHENSION------------------------------

Quando inicializamos uma list pre definida, sempre colocamos [coisas] dentro
contudo, quando queremos que ela seja dinamica, dependendo da relação que vamos colocar, podemos colocar um for dentro dela

ex: lista = ["_" for letra in palavra] -> dessa maneira, fazemos um for e para cada letra da variavel palavra é colocado os valores na lista
onde nesse caso, o valor é "_"

como a palavra é uma variavel string e str é uma sequencia de valores, a variavel interna do loop "letra", para cada interação, vale a letra ( valor ) da 
variável "palavra"

Além disso, podemos colocar condicionais dentro da instancia da list. ex:
  
list[x for x in inteiros if x % 2 == 0] --> nesse caso, estamos apenas adicionando os números pares dentro da lista, o loop percorre
uma outra lista "inteiros" e aplica um condicional para saber se é par, assim essa list só recebe como valores os numeros pares da lista "inteiros"






