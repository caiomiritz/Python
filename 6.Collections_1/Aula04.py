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

Tudo isso segue uma ordem natural que a máquina segue, ex: Strings se diferenciam de maiúsculas e minúsculas

Ordenação sem ordem natural segue uma maneira diferente, ex: uma lista de objetos do tipo "Contas" 
a chave para fazer pode ser feita por uma key no parâmetro de sorted(). 

Ex: sorted(contas, key=método):  -> nesse caso, o método retorna a compração que quizer, reduzindo o objeto a um valor comparável
Abordagem funcional

from operator import attrgetter
Nesse caso, não precisamos criar o método na key, pois esse import consegue pegar o atributo do objeto

Ex: sorted(contas, key=attrgetter("_saldo", "_codigo")):  -> nesse caso, ele pega o atributo protect _saldo como primeiro
se empatar, usamos o atributo _codigo para desempate
    
Problema, como o atributo é protected, não queremos alterar ou acessar esses atributos, pois não é permitido.
Para podemos fazer um sorted direto, ou alguma comparação que envolva '<' ou algo do tipo, podemos sobrescrever o metodo __lt__ (less than)
nesse caso, podemos fazer a ordenação natural

def __lf__(self, other): -> nessa sobrescrição ela faz a comparação que quizermos 
  
para desempatar, usando o __lt__ podemos complexar o código com condicionais para fazer as análises

functools -> essa biblioteca da para uma classe uma série de utilidades
from functools import total_ordering

Dessa maneira, apenas precisamos implementar as funções __eq__ e __lt__ que a propria biblioteca nos da uma série decomparações prontas, usando
métodos prontos, tendo assim uma ordenação total sobre essa comparação de objetos, '<' '>' '<=' '==' etc.

@total_ordering
class Conta():     -> temos que sinalizar que essa conta possui o aspecto de ordenação total


