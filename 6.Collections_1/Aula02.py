------------------LISTAS DE OBJETOS---------------------

Podemos fazer listas e passar objetos instanciados para a mesma, contudo vale lembrar que
apenas criamos uma variável que faz referencia para a o local de memória onde este objeto foi 
instanciado, nós não instanciamos objetos novos, quando passamos eles por parâmetro

Assim, podemos mudar esse objeto, usando outras variáveis, ou seja, um mesmo objeto pode ter
mais de uma variável que referencia-o, o que pode causar problemas devido a mutabilidade e a facilidade
de acesso a esse objeto, métodos e atributos

----------------------------TUPLAS----------------------

Quando queremos trabalhar com sequencias diferentes, onde cada posição representa algo diferente
usamos as tuplas, ja que a representação é imutável

Diferente da lista, as tuplas são imutáveis, fixas, determinadas apenas quando inicializamos
uma tupla não tem método append() por exemplo, por que não podemos adicionar, remover valores dentro dela

Quando temos muitos valores e funções diferentes na tupla, as classes são muito mais recomendadas
Podemos acessar os valores, mas não podemos altera-la

Unica coisa que podemos fazer é criar métodos que retornam uma tupla usando os valores de outras tuplas
Assim podemos reatribuir esse retorno na tupla existente

--------------TUPLAS + LISTAS /  OBJETO----------------

Podemos ter uma lista de tuplas, onde a lista é mutável, podendo adicionar mais tuplas, ou deleta-las da lista
para acessar uma lista de tuplas, é tipo uma matriz. Ex: usuarios[0][1] -> retorno da primeira tupla, com seu segundo valor
  
Assim, podemos ter tuplas de listas também, e tuplas de objetos, onde podemos alterar os objetos, pois ele é mutável
a tupla em si não pode ser mudada

Não é muito comum usar tuplas nesses cenários
