---------------------ATRIBUTOS PRIVADOS---------------------------

Sem a privativa dos atributos, podemos acessar diretamente o atributo pela varável
Geralmente quando a gente quer acessar ou mudar um atributos, precisamos de métodos que fazem isso

Para tirar o acesso direto dos atributos do objeto, deixamos eles privados, para deixar mais encapsulado
No método construtor, mudamos o nome do atributo com '__' para deixar privado

Ex: self.__nome -> esse atributo agora é privadoe possui esse nome mesmo
OBS: para acessar ou mudar em métodos construtores, usamos o nome mesmo com '__' 
  
Esses atributos são acessíveis apenas dentro da classe mesmo, o pyhton avisa que esses atributos são privados
ele não impede de acessar diretamente ( apenas dentro da mesma classe ), mas ele avisa

OBS: Em outras classes, quando usamos as variáveis desses objetos, não consguimos acessos diretos 
  
---------------------------GET E SET------------------------------

São métodos que acessam atributos, geralmente usados em atributos privados
Assim como temos os acessos, temos os métodos modificadores ( setters )
Dessa maneira conseguimos manter o código encapsulado e coeso, sem acessar diretamente os atributos

-------------------------PROPRIEDADES---------------------------

Embora tenhamos o os getter e setters, podemos usar propriedades, para usar o mesmo conceito
sem usar esses métodos, apenas usando diretamente de uma variável

usamos '@property' onde o método se trata de uma propriedade, e executa um método por "debaixo dos panos"

Ex: @property
    def nome(self):
      return self.__nome
 
Dessa maneira não precisamos chamar o método diretamente com variável.nome(), podemos usar sem parenteses
Ex: variavel.nome -> dessa maneira ele executa aquele método da mesma maneira
  
Ele parece que acessa o atributo diretamente, mas como é uma property ele apenas executa aquele método escondido
Funciona para os setters também, contudo a definição é diferente e a aplicação do valor não é por paramentro mas sim por '='

Ex: @nome.setter
    def nome(self, nome):
      self.__nome = nome

Dessa maneira temos o nosso setter, mas como eles são muito parecidos, diferenciando de um parametro, usamos '=' para atribuir o valor
que queremos. Ex: variavel.nome = "Caio"

Dessa maneira estamos usando o setter. Se usarmos apenar variavel.nome vamos usar o getter, e vai ter apenas o retorno desse atributo




