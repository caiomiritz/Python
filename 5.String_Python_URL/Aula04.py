--------------------MÉTODOS ESPECIAIS-----------------------

São métodos chamados durante a execução do programa pelo próprio Python "Indiretamente"
Quando um objeto não possui métodos como len(), precisamos implementar na classe

def __len__(self):
  return len(objeto que possui len) -> ex: pode ser self.url um atributo da classe que é uma String

dir(objeto) -> retorna uma lista de strings com todos os métodos e atributos do obejto passado

__str__ -> por default, quando printamos um objeto, ele retorna a String de endereço de memória onde o objeto esta alocado

Se quizermos printar um objeto propriamente, devemos implementar __str__() dentro da classe, seguido do que printar

def __str__(self):
  return self.variavel

---------------------------IGUALDADE E IDENTIDADE------------------

__eq__ é um método interno do python de "equalit" para comparar se os objetos são iguais, ele compara o endereço de memória
para ver se o obejto é igual, usando como parâmetro o mesmo atributo, devemos implementar na nossa classe

def __eq__(self, other):
  return self.variavel == other.variavel     --> o other é o outro objeto que esta sendo comparado

Assim, para comparar Strings ( que é um objeto ), precisamos usr métodos específicos para isso

Mesmo sobrescrevendo o método __eq__ eles não são identicos, pois o método id() mostra a indentificação do objeto
Precisamos usar o comparador "is" para verificar se eles tem a mesma identidade, mesmo local da memória Ex: 1 is True
  
É muito importante também verificar se os tipos dos objetos são iguais para validar sua igualdade também, porque podemos 
ter classes diferentes mas com atributos iguais, e para não fazer a comparação ( exemplo, de código ), precisamos ver se o tipo é igual
