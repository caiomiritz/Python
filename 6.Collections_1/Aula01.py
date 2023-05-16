--------------------COLEÇÕES E LISTAS---------------------

Coleções quando quero trabalhar com diversos valores do tipo base igual, como números inteiros
Lista, por exemplo, permite adicionar diversos elementos, de preferencia do mesmo tipo base

Lista, "Array" de maneira genérica, uma sequncia de valores que podem ser acessados aleatoriarmente
a Lista, pode ter seus valores alterados, deletados, adicionados

idades.append(valor) -> o append serve para adicionar algum valor no final da lista
Podemos passar por todos os elementos, podemos printar a lista, aparecendo todos os elementos

idades.remove(valor) -> remove um valor da lista. Se um elemento for repetido, ele remove a primeira aparição do valor
Para mais métodos e manipulações basta ver a documentação

idades.insert(valor, posição) -> podemos escolher o valor e sua posição que queremos inserir

podemos fazer uma "gambiarra" para adicionar mais de um elemento na lista usando o append
ex: idades.append([27, 19]) -> mas isso fica uma lista dentro de outro lista, o que não queremos
  
idades.extend(valor1, valor2, ...) -> dessa maneira extendemos a lista e adicionamos os valores que queremos

Como visto antes, podemos fazer a compreensão da lista, usando interadores e condicionais dentro da criação de uma lista

