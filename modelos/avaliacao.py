class Avaliacao:
    """
    Classe utilizada para armazenar as avaliações de cada cliente em instancias.
    Classe é chamada na classe "Restaurante" por cada instancia e assim é utilizada para armazenar o 
    valor de cada cliente em uma lista.

    Inputs:
    -Cliente
    -Nota

    Outputs:
    -Cliente
    -Nota
    """

    def __init__(self, cliente, nota):
        """
        Metodo construtor da classe que permite ler o nome do cliente a sua nota em sua construção
        """
        self._cliente = cliente
        if nota > 5:
            self._nota = 5
        elif nota < 0:
            self._nota = 0
        else:
            self._nota = nota
        

    def __str__(self):
        """
        Metodo especial que permite entregar os valores a instancia mencionada
        """
        pass
        