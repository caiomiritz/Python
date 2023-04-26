-----------------------------USANDO METODOS----------------------------------

Se quizermos implementar métodos para relacionar os atributos ou algo do tipo
precisamos também colocar como um dos parametros o self

Ex: def getNome(self):
      return self.nome
  
Nesse caso, criamos um método para retornar um dos atributos desse objeto, no caso o nome
A utilização de métodos deixa o código muito mais limpo, diminuindo as chances de erro

Para acessar o método, fazemos o mesmo esquema para acessar os atributos diretamente pelas variáveis
que apontam para os objetos

Ex: variavel.getNome() -> dessa maneira, acessamos a variavel nome do objeto que esta apontado por variavel

Como o objeto que esta sendo apontado recebeu seus respectivos parametros na construtora, temos o retorno
baseado com atributos daquela variável quando instanciamos o objeto

Claro que podemos adicionar outros parametros nesse método, para fazer alteraçoes que quizermos
Ex: def setNome(self, nome):
      self.nome = nome
      
Nesse caso estamos mudando a variável nome através de um método, onde seu valor é passado por parametro

OBS: 'none' é equivalente a 'NULL', podemos atribuir esse valor para variáveis de referencias que nao estao sendo usadas
Visto que em algum momento o pyhton coleta o "lixo", basicamente deleta os objeto que não são usados, objetos perdidos

