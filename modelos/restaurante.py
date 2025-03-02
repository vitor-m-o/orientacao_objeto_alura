from modelos.avaliacao import Avaliacao
"""
Importanto a classe "Avaliacao" do outro arquivo para poder utiliza-la
"""

class Restaurante:
    """
    Classe criada para poder realizar as funções de um aplicativo de restaurantes.

    Inputs:
    - Nome 
    - Categoria

    Outputs:
    - Nome e Categoria de cada restaurante
    - Listagem dos restaurantes
    - Verificação de disponibilidade
    - Manuseio da disponibilidade dos restaurantes
    - recebimento e leitura das avaliações em formato de média
    """
    restaurantes = []
    """
    Lista utilizada para armazenar os restaurantes
    """

    def __init__(self, nome, categoria):
        """
        Metodo construtor da classe, utilizado para atribuir valores a cada instancia em sua inicialização

        Inputs:
        - Nome
        - Categoria
        
        Outputs:
        - Propriedade ativo como falso
        - Avaliação como vazio
        - Armazenamento do restaurante na lista restaurantes
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Metodo especial utilizado para entregar uma resposta mais visual à quem for chamar 
        o objeto sem nenhuma propriedade ou metodo

        Output:
        - Nome e Categoria do restaurante instanciado mencionado
        """
        return f'Restaurante: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Metodo de classe utilizado para listar os restaurantes instanciados nesta classe

        Outputs:
        - Nome, Categoria, Avaliação e Status de cada restaurante instanciado na classe
        """
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Propriedade de cada instancia que devolve um valor mais visual ao usuário ao invés de 
        true ou false para a propriedade original _ativo

        Output:
        - Retornar "emoji de correto" ou "emoji de incorreto" de acordo com o status do restaurante
        """
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        """
        Metodo de instancia que alterna o estado da instancia mencionada

        Output:
        - Inverter valor booleano da variavel _ativo
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Metodo de instancia que recebe avaliacao de um cliente e o armazena

        Inputs:
        - Nome do cliente
        - Nota escolhida
        
        Outputs:
        - Instanciamento da classe "Avaliacao" para armazenar o valor da avaliação
        - Armazenamento da instancia da classe utilizando uma lista chamada "_avaliacao"
        """
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Propriedade de instancia que retorna a media das avaliações da instancia mencionada

        Outputs:
        - Caso não ouver avaliações, retornar valor "nulo" representado por "-"
        - Caso ouver avaliações realizar a contagem de avaliações, soma das notas das avaliações,
        realizar a média das notas e assim retornar
        """
        if not self._avaliacao:
            return '-'
        quantidade_de_notas = len(self._avaliacao)
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)

        return media