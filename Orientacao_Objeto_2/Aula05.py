--------------------------HERANÇA MULTIPLA-----------------------

class Junior(Alura)  -> dessa maneira ele apenas herda as características da superclasse Alura
class Pleno(Alura, Caelum) -> assim, essa classe Pleno herda caracteristicas de 2 superclasses

Funciona da mesma maneira tudo, o acesso a metodos e atributos...Contudo, pode dar muito problema
Como saber qual meotodo chamar, quando ambas as superclasses tem metodos "iguais"

O Python funciona de uma maneira a qual segue uma ordem epecífica de seleção de métodos de cascata
#pleno > alura > funcionario > caelum > funcionario

Assim como o Java, a busca é de baixa para cima, sendo Funcionario a ultima superclasse
Algoritimo MRO -> leva em consideração as repetições de superclasse, ele verifica se a superclasse é uma 'good head'

Ele verifica se tem uma outra classe na mesma hierarquia de Funcionario se ele pode utilizar, assim dessa maneira
ele verifica Caelum antes de Funcionario #pleno > alura > caelum > funcionario

Tudo isso porque Alura esta na frente de Caelum na implementação da classe la em cima...

----------------------------MIXINS---------------------------------

