#-------------------ELIF---------------------------

elif é outro condicional igual ao else if, para tirar os if aninhados
esse aceita condição, diferente do else que é apenas a sobra

#--------------------WHILE-------------------------

while executa uma condição enquanto ela é verdadeira, assim como o if, else e elif, depois do parametro de condição
ele tem o ":" que representa o bloco depois e tambem necessita mais de 4 espaços nesse bloco

então tudo que tem dentro, precisa estar 4 espaços para frente

#--------------FOR----------------------------------

for é um laço de repetição, contudo, no python ele nao tem parametros, mas sim, usamos a função 'in range(inicio, final, step)'
o 'final' dentro do parametro é exclusivo ou seja, num print por exemplo ele nao printa (poderiamos colocar o 'final+1' para realmenrte pegar)
o 'step' é um numero que representa os passos dentro desse conjunto de numeros
sem o 'range' podemos usar [1,2,3,4] por exemplo: for in [1,2,3] ele apenas roda 3 vezes
o for não possui parenteses, alem disso, precisamos colocar oq queremos fazer o loop, por exemplo: for rodada in range(1,tentativas+1)
essa rodada, vai ficar acrescentando de um em um, pois por padrão, o step é 1

#--------------FIM DO LAÇO--------------------

break faz uma interrupção abrupta, contudo, ele não é muito recomendado
continue é um tipo de interrupção da interação, contudo o laço não é quebrado, ele apenas nao executa as linhas abaixo do continue e volta para a proxima interação