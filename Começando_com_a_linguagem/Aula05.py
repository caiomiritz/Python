#---------------IMPORT-------------------------

podemos importar outros arquivos .py nos nossos codigos, com o comando import, dessa maneira conseguimos relacionar
um aqurivo .py com outro

para fazermos a utilização exata do arquivo importado, nao basta apenas importar, pois o python ja começa a executar o codigo dos import
queremos apenas executar esses aquivos quando quizermos
geralmente usamos funções para realização disso

#------------------DEF----------------------------

dentro dos aquivos .py, se quizermos dps utilizar em outro arquivo atraves do import, precisamos criar uma def
def 'nome_da_função():'

isso é a criação de uma função, como as outras precisamos espaçar 4 linhas também. Agora basta chamar essa função
quando usamos o import, so conseguimos usar a função que criamos com uma sintaxe diferente:

Ex: import forca ---> forca.jogo_forca()  --> dessa maneira, estamos acessando a função jogo_forca da import forca

#----------------ARQUIVO EXECUTAVO != IMPORTADO-----------------

Se executamos o .py diretamente que foi importado o pyhton cria uma variavel '__name__' e importa esse arquivo e pode atrapalhar
usamos uma sintaxe diferente e uma comparação para a __main__

temos que colcoar dentro da .py que foi importada o condicional de comparação
dependendo de como executamos, essa variavel __main__ vai ser diferente