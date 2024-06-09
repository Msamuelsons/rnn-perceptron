# Perceptron

Este repositório contém uma implementação básica de um perceptron em Python utilizando a biblioteca `numpy`. Um perceptron é um tipo de neurônio artificial usado para tarefas de classificação binária.

## O que é um Perceptron?

O Perceptron é uma unidade básica de uma rede neural artificial inspirada no funcionamento do neurônio biológico. Ele recebe entradas, aplica pesos às entradas, soma-as e passa o resultado através de uma função de ativação para produzir uma saída. Essa saída é usada para fazer uma previsão ou tomar uma decisão.

## Estrutura do Perceptron

Um perceptron consiste em:

- **Entradas**: Valores que o perceptron recebe como entrada.
- **Pesos**: Cada entrada é multiplicada por um peso correspondente.
- **Soma ponderada**: As entradas multiplicadas pelos pesos são somadas.
- **Função de Ativação**: A soma ponderada é passada através de uma função de ativação para produzir a saída do perceptron.

## Funcionamento do Perceptron

1. **Inicialização**: Os pesos do perceptron são inicializados aleatoriamente.
2. **Treinamento**: Os pesos são ajustados iterativamente com base nos erros de previsão. Durante o treinamento, os dados de entrada são alimentados ao perceptron, e os pesos são atualizados para minimizar os erros de saída.
3. **Predição**: Uma vez treinado, o perceptron pode ser usado para fazer previsões para novos dados de entrada.

## Arquivos do Projeto

- `perceptron.py`: Contém a implementação da classe Perceptron com métodos para treinamento, predição e avaliação de acurácia.
- `README.md`: Este arquivo, fornecendo uma visão geral do projeto e instruções sobre como utilizá-lo.

## Requisitos

- Python 3.x
- numpy

Você pode instalar o `numpy` usando pip:



## Explicação do Código

Este código realiza o treinamento de um perceptron utilizando os dados de entrada `variaveis` e os alvos `target`, em seguida, realiza a predição para cada par de valores de entrada e calcula a acurácia do modelo.

## Funcionamento do Código

Este código implementa um exemplo de treinamento e utilização de um perceptron para realizar a classificação de dados. Aqui está uma explicação passo a passo do que o código faz:

1. Importa a classe `Perceptron` do arquivo `perceptron.py` e a biblioteca `numpy`.
2. Define os dados de treinamento `variaveis` e os alvos `target`. `variaveis` representa os pares de valores de entrada, e `target` representa os valores alvo correspondentes.
3. Inicializa um objeto `Perceptron` com dois neurônios de entrada.
4. Chama o método `treinamento` do perceptron, passando os dados de treinamento, uma taxa de aprendizado de 0.1 e 100 épocas de treinamento. Isso ajusta os pesos do perceptron com base nos dados de treinamento fornecidos.
5. Realiza a predição para cada par de valores de entrada (0, 0), (0, 1), (1, 0) e (1, 1) usando o método `predicao` do perceptron com os pesos calculados no passo anterior.
6. Calcula a acurácia do perceptron usando o método `acuracia`, comparando as predições com os valores alvo.
7. Imprime as predições para cada par de valores de entrada e a acurácia do modelo.

O objetivo final é demonstrar como um perceptron pode ser treinado e utilizado para realizar a classificação de dados e avaliar sua precisão.
