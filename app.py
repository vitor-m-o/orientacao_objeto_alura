from modelos.restaurante import Restaurante
"""
Importar a classe Restaurante do arquivo modelos/restaurante.py
"""

def main():
    """
    Função principal do arquivo, que instancia os restaurantes "Praça" e "Mexican Food", colocando suas respectivas categorias,
    após é inserido as avaliações dos restaurantes com o nome dos clientes com o valor das suas avaliações
    após é listado os restaurantes, possuindo os nomes, categorias, avaliações e status de cada.

    Inputs:
    - Nome dos restaurantes
    - Categoria dos restaurantes
    - Nome dos clientes avaliadores
    - Valor das avaliações

    Outputs:
    - Listagem dos restaurantes com nome, categoria, avaliação e status de cada
    """
    restaurante_praca = Restaurante('Praça', 'Gourmet')
    restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')

    restaurante_praca.receber_avaliacao('Gui', 5)
    restaurante_praca.receber_avaliacao('Lais', 5)
    restaurante_praca.receber_avaliacao('Emy', 5)

    restaurante_mexicano.receber_avaliacao('Lais', 1)
    restaurante_mexicano.receber_avaliacao('Emy', 1)

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    """
    Função que determina este arquivo como principal, não podendo ser importado para outro
    """
    main()