------------------UTILIZANDO METODOS--------------------------

Como encontrar a posição de uma string ? Usando o método find()
ex: texto = 'abcd' -> aplicando texto.find('b') retornará a posição da letra, nesse caso 1

Podemos usar isto na hora de fatiar as strings. Vale lembrar que podemos omitir um dos parametros do fatiamento
ex: texto[:5] -> nesse caso ela pega o inicio da URL e vai até a posição 4, ja que é exclusivo o final
ex: texto[0:] -> nesse caso, ela pega do incio até o final da String, claro, isso tudo pode ser ajustado
  
find também pode achar uma string completa find('Caio') retornando a prosição da primeira evidencia 
Podemos usar o len() de alguma string específica para podermos trabalhar junto com o find. Ex: len('Caio')
  
find() também tem parametros não obrigatorios, onde tu pode colocar o inicio e o fim da busca
find('&', 10) -> ele vai começar a buscar '&' pela posição 10 para frente

Dessa maneira, podemos fatiar a URL com inúmeros parâmetros, usando condicionais para fazer a busca
Assim, independente da ordem, podemos pegar cara um dos parametros da URL
