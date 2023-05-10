-----------------------DUCK TYPING------------------------

Herança x Composição -> as vezes a herança pode não ser a melhor opção

É possivel implementar uma interação em uma classe, sem precisar recorrer a herança na list
Podemos criar um método para deixar a classe interável, sem ter a herança

MAGIC METHODS
def __getitem__(self, item):
  return self._listaInterna[item]

repassando um item com uma lista interna no __init__ da classe, assim podemos iterar a lista
que no nosso exemplo, são as listas de programas ( a lista é um dos atributos da classe )

Dessa maneira, podemos ganhar várias características da lista e métodos também. Pois queremos que a classe
tenha caracteristicas de lista sem ter a herança direta da list

Quando fazemos herança, nós temos muito acoplhamento, podemos fazer uma composição para diminuir isso
Composição: Playlist tem um list

Dessa maneira conseguimos as vantagens de uma classe sem ter um acoplamento muito forte

-----------------------MODELOS DE DADOS PYTHON----------------------------

Para a classe se comportar como Sized ou algo que tenha tamanho, precisamos implementar um magic

def __len__(self):
  return len(self._listaInterna)

dessa maneira conseguimos usar o len(classe) diretamente, pois tornamos a classe Playlist um sized
assim podemos utilizar funções que se aplicam em classes sized

Inicialização: __init__
Representação: __str__, __repr__
Container, sequencia: __contains__, __iter__, __len__, __getitem__
Numéricos: __add__, __sub__, __mul__, __mod__
  
São inúmeros dada methods, mas esses são os principais -> um tipo "append" por exemplo é herdade do __add__
São tipo de interface, mas é mais uma ideia de protocolo, onde o objeto precisa se comportar daquele jeito
assim precisamos implementar métodos magic para trabalhar com esses aspectos da linguagem

