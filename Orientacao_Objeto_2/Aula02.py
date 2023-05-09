-------------------POLIMORFISMO----------------------

As classes filhas, sao do mesmo tipo da classe mãe
Ex: podemos colocar classes diferentes, mas que vem da mesma mãe em uma lista ou método
  
Esse relacionamento pode ser dado como 'é um' -> 'filme é um programa'
O polimorfismo nos permite usar diferentes classes em um mesmo método
Ex: percorrer uma lista onde contem classes do mesmo supertipo, onde o for não se preocupa com o tipo dentro da lista

Não precisamos verificar qual é o tipo desse objeto, ja que são da mesma superclasse

detalhes = programa.duracao if hasattr(programa, 'duracao') -> isso ve em tempo de execução se aquele objeto tem um atributo específico
mas imaginamos uma classe com varios atributos específicos, essa variável ficaria muito grande

hasattr(objeto, 'atributoX') -> isso verifica se um objeto tem um determinado atributo

-------------------REDUZINDO OS IF---------------------

Podemos sobreescrever os métodos da superclasse, onde a classr filho pode deixar com suas especificidades
Cria o metodo para cada uma das classes, onde não vai importar qual o tipo do pragrama

No for each, percorremos a lista com obejtos com a mesma sueprclasse, se vamos usar um método nesse for ele não 
vai se preocupar sobre qual tipo vai ser, porque cada um vai ter um método específico sobreescrito

Esse método é igual ao método da superclasse

--------------------REPRESENTAÇÃO TEXTUAL DE OBJETOS-----------------


