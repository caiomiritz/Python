-----------------------HERANÇA-------------------------

Diminuir a duplicaçaõ de código e ter mais reuso do código
Ligação que classes vão ter de uma classe mãe, com características compartilhadas com outras classes

Ex: Temos uma classe mãe chamada Programa
  
Com isso, temos 2 outras classes que compartilham características de programas
contudo, essas 2 classes tem características próprias também

na criação da classe, temos que dizer qual é a classe mãe. Ex: class Filme(Programa):
nesse caso, a classe mãe é Programa

como temos o privado na classe mãe, temos que arrumar as filhas nas suas construtoras
Contudo, podemos deixar protected, onde somente as classes filhas podem acessar

Na contrutora da mãe, deixamos apenas um '_'. ex: self._nome
Nesse caso, o atributo comum é nome, e com apenas um '_' temos esse atributo protected

------------------REUTILIZAÇÃO------------------------


