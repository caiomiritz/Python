------------------ METODOS PRIVADOS / ESTATICOS ----------------------

Quando criamos métodos apenas para melhorar a compreensão e não queremos usar ele diretamente
deixamos o método disponível para ser usado apenas dentro da classe, geralmente eles se encontram 
dentro de outros métodos para melhorar o código

Como as variáveis privadas, mudamos o seu nome com '__' também
Ex: def __pode_sacar(self, parametroX)
  
Dentro da classe conseguimos usar, mas fora dela não, servindo apenas para auxiliar em outros métodos
Seprar partes para o código não ficar "macarrão"

Metodos estáticos são da classe, não precisamos de um objeto, como o @property temos uma sintaxe
Ex: @staticmethod
    def metodo():
        ...
  
Dessa maneira, temos um método de classe, útil quando algo for fixo para todos os objetos
Temos que ser cautelozos usando esses métodos, em apenas alguns casos fazem sentido
Geralmente quando todos os objetos compartilham de uma mesma coisa em comum




