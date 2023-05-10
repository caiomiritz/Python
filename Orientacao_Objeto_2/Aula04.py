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

--------------------------------INTERFACES--------------------------------------

A interface do Python é diferente de Java / C++, em python é apenas obrigado a implementar métodos

Abstract Base Classes (ABC) são classes abstratas que servirão de base, pois não é muito comum criar do zero
classes abstratas. Se quizermos criar uma classe que depende de outra, vemos se ja existe uma base pronta

from abc import ABC
from collections.abc import MutableSequence

Dessa mandeira, importamos uma sequencia mutavel de uma classe base. Assim, basta herdar do que queremos
Mas precisamos implemnetar método que irão fazer parte da MutableSequence para se comportar como uma classe ABC

Isso veio para complementar o Duck Typing, mas as vezes queremos que a classe tenha outros comportamentos garantidos
porque o ABC força a validação para ver se realmente a classe se comporta dessa maneira

from numbers import Complex -> é um exemplo onde a classe vai ser tratada como numero complexo

Instanciando um objeto, vai dar um erro mostrando quais metodos precisamos implementar para funcionar da menria correta
As vezes a classe de métodos abstratos ja tem os metodos implementados na superclasse, assim podemos reaproveitar 

Ex: def __getitem__(self, item):
    super().__getitem__()               --> dessa maneira o metodo é implementado na superclasse, e estamos apenas reaproveitando

Mas claro, podemos implementar nós mesmos, sobreescrevendo os métodos

