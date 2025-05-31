# Aspirador de Pó Inteligente (Trabalho de Faculdade)

Este projeto simula um aspirador de pó em um ambiente bidimensional, representado por um tabuleiro de 5x5. A interface gráfica é feita com a biblioteca **Pygame**, e o objetivo principal é implementar um algoritmo de busca pelo **caminho de menor custo** para limpar toda a sujeira espalhada no ambiente.

## Objetivo

Desenvolver uma solução capaz de:

- Representar visualmente o movimento do aspirador no ambiente;
- Identificar e limpar posições com sujeira;
- **Calcular o caminho mais eficiente** para passar por todas as sujeiras e retornar à posição inicial, minimizando a distância total percorrida.

Esse tipo de problema é uma variação do **Problema do Caixeiro Viajante (TSP)**, onde o agente (aspirador) deve visitar todos os pontos de interesse (sujeiras) e retornar à origem, percorrendo a menor distância possível.

## Tecnologias utilizadas

- Python 3
- Pygame

## Como executar

1. Instale as dependências (caso não tenha o pygame):

   ```bash
   pip install pygame
   ```
   ![Demostracao](assets/Aspirador.gif)

