-------------------POLIMORFISMO E ARRAYS----------------------

Podemos ter uma lista de contas de objetos diferentes, contudo ela tem a mesma superclasse

No python existe o termo Array, o tipo, contudo ele precisa ser importado, sendo muito específico
-> import array as arr

Pra instanciar o array, precisamos passar o tipo do valor que queremos armazenar, seguido dos valores
Ele é muito utilizado para quando estamos trabalhando com números, pois todos os valores seguem um unico tipo

ex: arr.array('d', [1,2,3]) -> nesse caso estamos passando o tipo inteiro, seguido dos valores

O recomendado para trabalhar muito com número, matematica é o numpy -> import numpy as np
Mas ele precisa ser instalado, usando o comando: !pip install numpy    #Usado muito em cienciadedados
  
------------------METODO ABSTRATO--------------------------

Se queremos uma classe mão, onde todos as filhas precisam forçar a criação de um método, podemos criar
uma classe abstrata para isso. importando bibliotecas para isso

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta): -> nesse caso, a classe Conta agora é uma classe abstrata

@abstractmethod
def passa_o_mes(self):      -> isso é um metodo abstrato, onde nas classes filhas precisamos implementar esse método
  pass
  
Não queremos instanciar objetos da classe Conta, ja que ela serve como uma organização
