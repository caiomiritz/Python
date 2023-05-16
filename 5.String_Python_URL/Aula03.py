----------------VALIDANDO COM EXCEÇÃO--------------------

Validamos a URl dentro de um if, com o condicional de limpeza dos dados, com o lançamento de uma exceção
Limpeza "Sanitização da URL" -> tiramos os espaços

url = url.replace(1, 2) -> 1: parametro o qual caractere queremos tirar da String. 2: o que queremos substituir do lugar
url = url.strip() -> esse método retira todos os espaços em branco dentro da String

url seria uma variável para armazenar a URL sanitizada
if url == "": verifica se a url é vazia

raise ValueError("mensagem de erro")

----------------------
