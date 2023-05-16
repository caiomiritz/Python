----------------VALIDANDO COM EXCEÇÃO--------------------

Validamos a URl dentro de um if, com o condicional de limpeza dos dados, com o lançamento de uma exceção
Limpeza "Sanitização da URL" -> tiramos os espaços

url = url.replace(1, 2) -> 1: parametro o qual caractere queremos tirar da String. 2: o que queremos substituir do lugar
url = url.strip() -> esse método retira todos os espaços em branco dentro da String

url seria uma variável para armazenar a URL sanitizada
if url == "": verifica se a url é vazia

raise ValueError("mensagem de erro")

----------------------NONE VS EMPTY-----------------------

None -> objeto próprio do Pyhton "NoneType"
None não tem o método Strip da String 

String vazia (empty) e None são diferentes, mas ambos são considerados false
É bom ter um if para verificar se o objeto é um None ou é String vazia

---------------------EXPRESSÕES REGULARES-----------------

import re -> "Regular Expressions" / "ReqEx"
é biblioteca padrão do Pyhton

padrao = re.compile("[]") -> Dentro dos [] mostramos o padrão da escrita, retornando o objeto padrão
pódemos colocar "?" para mostra se o grupo dentro do [] pode aparecer ou não
o obejto padrao tem métodos, como search() retornando #match ou none, caso o padrão não seja achado

busca = padrao.search(String qualquer)
if busca:
  cep = busca.group()  -> retorna a string encontrada com aquele padrão
  print(cep)

----------------------QUANTIFICADORES E INTERVALOS--------------

Podemos passar um número dentro {} para mostra quantas vezes aquele grupo [] aparece no padrão, reduzindo muito o compile()
Ex: busca de cep: padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") -> um cep composto de 5 dígitos de 0 a 9 seguido de um hífen opcional
mais 3 dígitos de 0 a 9 também

{} -> nos quantificadores podemos mostrar quantas vezes ele pode aparecer {0,1} -> pode aparecer 0 ou 1 vez o item no padrão


