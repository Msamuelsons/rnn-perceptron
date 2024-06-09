from perceptron import Perceptron 
import numpy as np

# Dados de treinamento
variaveis = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target = np.array([[0], [1], [1], [1]])

perceptron = Perceptron(2)  # Duas entradas

# Treinamento
pesos = perceptron.treinamento(variaveis, target,0.1, 100)  

# Teste
print("Predição (0, 0):", perceptron.predicao(pesos, 0, 0))
print("Predição (0, 1):", perceptron.predicao(pesos, 0, 1))
print("Predição (1, 0):", perceptron.predicao(pesos, 1, 0))
print("Predição (1, 1):", perceptron.predicao(pesos, 1, 1))

# Acurácia
acuracia = perceptron.acuracia(variaveis, target, pesos)
print(acuracia)