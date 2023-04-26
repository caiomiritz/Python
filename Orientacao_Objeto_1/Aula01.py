-------------------CLASSE E OBJETO------------------------------

Classe basicamente é a receita de um objeto que representa algo no mundo real
Para definirmos uma classe, usamos 'class' seguido do nome da classe com ':'

Ex: class Carro:
    
Seguimos o padrão de usar a letra maiúscula para representar o nome da classe
'pass' é uma palavra chave para deixar a classe em branco, para depois escrevermos a "receita" nela

Por exemplo Carro() é o endereço, referencia da classe Carro, se quizermos guardar o endereço 
em alguma variável é possível

----------------------CONSTRUTOR-----------------------------

Como uma classe é uma "receita", ela precisa ter uma função que atribui os valores dos atributos
A função construtora tem uma sintaxe diferente.

def __init__(self, parametro1, parametro2, ...): -> 
  self.atributo1 = ...
  self.atributo2 = ...
  
Quando formos criar um objeto dessa classe, armazenamos o mesmo em uma variável e passamos os parâmetros
Ex: variavel = Carro(atributo1, atributo2, ...)
  
Nesse caso, instanciamos um objeto da classe Carro e passamos os parametros da construtora
Quando um dos atributos é fixo, podemos colocar o parametro fixo na construtora

OBS: Se formos instanciar um objeto com atributo fixo não precisamos passar o mesmo por parametro
  




