#-------------FORMATAÇÃO DE STRINGS-----------------

Dentro do print, quando queremos substutuir algo na frase por alguma variavel, podemos colocar chaves indicando onde vai ser a
substituição.

print("Rodada {} de {}".format(rodada, tentativas)) -> ali, vai ser substituido pelos valores das variáveis, usando a função format
essa função entra como parametros os valores que queremos substituir dentro da string

dentro da {} podemos colocar a ordem que queremos a formatação, ele começa em 0 como o primeiro.
ex: print("Rodada {1} de {0}".format(rodada, tentativas)) -> nesse caso, a tentativa vai na primeira {} pois ela é a segunda no parametro do format

podemos colocar mais coisas dentro da chave. {:.2f} nesse caso, esse espaço esta esperando um float com 2 casas depois do ponto

{:07.2f} nesse caso, quero que o print seja um número com 7 caracteres com 2 depois da virgula. Se colocarmos um numero menor ex: 4.5 naquela chave
o print sera 0004.50 pois aquele 07 representa que o resto vai ser preenchido com zero

{:07d} agora esperamos um inteiro, ex: colocamos 45, vai sair 0000045, se colocarmos apenas {:7d} nesse caso, vai ser preenchido com espaço "     45"
usando datas é muito util, quando o .format e apenas inteiros. ex: .format(3, 11) com {:02d} vai sair assim -> 03 11

#----------------------ALEATORIEDADE-------------------

temos funções 'build-in' que vem junto com o python, que nao precisam importar módulos
a grande maioria vem da importação de módulos (bibliotecas), como por exemplo a criação de numeros aleatorios
temos que dar um import 'módulo' antes

random é a biblioteca, no caso, queremos aleatorizar em uma faixa de numeros: usamos randrange(inicio, fim)
contudo o final é exclusivo. ex: randrange(1, 101) gera de 1 até 100. Podemos colocar o step dentro do parametros, mas por padrão é um

randrange(10) por exemplo, o menor numero é 0 e o maior é 9