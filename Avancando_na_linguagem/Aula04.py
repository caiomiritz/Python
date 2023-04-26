-------------------------------FUNÇÕES---------------------------------

Devemos criar funções para separar a reponsabilidade de cada coisa no código pelo 'def'
ex: def imprime_mensagem():
    
Claro, quando queremos usar essa função, basta chamá-la quando quizermos, claro, se a função retorna algo
preisamos armazenar em alguma variável ou fazer outro processo com o uso adequado

Para deixar explícito que queremos retornar algo nessa função, usamos o 'return' seguido do nosso retorno
As variáveis que estão no escopo das funções só podem ser usadas dentro da propria função

Temos parâmetros das funções, que recebem informações a qual vamos utilizar na sua execução
ex: def inicializa_letras(palavra), onde 'palavra' é um parâmetro
Podemos colocar mais de um parâmetro também

Diferente das outras linguagens, não precisamos colocar o tipo do parâmetro
Quando criamos funções com parâmetros, é possível deixar o valor do mesmo padrão

Ex: def carrega_palavra(nome_arquivo="palavras.txt")
Por padrão, o parâmetro vai ser "palavras.txt", mas se chamarmos a funçao e passarmos outro parametro ela vai mudar na execução
Podemos nomear os parametros passados

Inclusive, quando chamamos uma função, podemos colocar o nome do parametro na msm
Ex: carrega_palavra(nome_arquivo="texto.txt") -> nesse caso, ele colocou o nome do parametro e o valor do mesmo explicitando
    
OBS: mesmo não sendo obrigatório, é um bom uso da linguagem.


