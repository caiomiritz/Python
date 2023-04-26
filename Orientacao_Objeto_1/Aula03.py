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
