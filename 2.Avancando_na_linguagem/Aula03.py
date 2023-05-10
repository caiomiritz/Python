----------------------- ESCREVENDO EM ARQUIVOS -------------------------------

Algumas partes do código queremos que venha de arquivos externos, por exemplo uma palavra que queremos mudar
sem precisa mudar dentro do código, e sim pegar de um arquivo

open("nome_do_arquivo.extensão", modificador) é uma função build-in onde aqueles são seus parâmetros
o modo de trabalho (modificador) podem ser: acrescentar("a") escrita("w") (ele sobreescreve o arquivo) e leitura ("r")
leitura não deixa escrever no arquivo

.read() lê o arquivo inteiro, mas dps se chamar novamente, não haverá conteúdo, porque ja foi lido tudo
ai precisa fechar e depois abrir o arquivo

a leitura linha por linha, podemos fazer um for -> "for linha in arquivo"
.redline() é uma função que lê apenas uma linha. o "\n" também é lido pela função

ex: se fizermos um print da linha do arquivo ( que ja contem \n ) ele vai pular mais ainda, pois dentro do print, existe um \n
podemos usar um .strip() para tirar o \n ( além de tirar os espaços )
  
isso retorna um arquivo, onde colocamos o mesmo em uma variável, dessa variável, podemos utilizar funcionalidades, ex:
.write("oq queremos escrever") -> mas isso, escreve tudo em uma mesma linha no arquivo, precisamos colocar \n para pular linha

OBS: como abrimos um arquivo, também precisamos fechá-lo, dessa maneira usamos um .close()
é importante que o arquivo fique na mesma pasta do projeto que está o código

----------------------------------ESCOLHENDO UMA LINHA / PALAVRA DO ARQUIVO -----------------------

precisamos guardar as palavras dentro de uma lista onde cada linha do for seria uma palavra
adicionaríamos essa palavra na lista, tirando o \n com o .strip()

OBS: vale lembrar que um arquivo txt com palavras separadas em linhas, possuem "\n" após a mesma
Para nao dar problema na hora da abertura de um arquivo, podemos fazer uma sintaxe diferente:
 
with open("palavras.txt") as arquivo:
    for linha in arquivo:
      
dessa maneira, não precisamos nem dar .close() no arquivo, pois o python se encarrega disso sozinho com essa sintaxe
