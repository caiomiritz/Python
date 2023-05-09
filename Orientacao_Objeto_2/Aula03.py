--------------------REAPROVEITANDO UM LIST---------------

Podemos deixar uma classe iterable, ou seja, podemos fazer loops diretos com o objeto da classe
não tendo a necessidade de acessar diretamente um atributo list da classe

Ex: class Playlist(list):
    
Como Playelist é uma list, precisamos inicizaliar o construtor da superclassse 'list'
super().__init__(listaX)

Essa 'listaX' é uma lista passada por parametro, e agora como Playlist herda as características de list
podemos iterar diretamente a classe no for

for variavel in variavelPlaylist:  -> assim estamos acessando cada um dos objetos dessa lista
  
Ex: print(f 'Tamanho da Playlist: {len(variavelPlaylist}' ) -> pegamos o tamanho da lista 

Como Playlist herdou características de list, podemos usar métodos e funcionalidades da list, como len()

--------------------FUGINDO DA COMPLEXIDADE-------------

Ao fazer esssa herança, criamos uma complexidade também, a melhor coisa é ter parcialmente as funcionalidades
Para tirar a complexidade basta desfazer a herança, perdendo muita coisa

Mas com essa herança, não sabemos o quao grande ficaria e complexo essa herança
list é uma classe gigantesca com muitos métodos que podem trazer problemas na nossa classe iterável


