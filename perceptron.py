import numpy as np
# conselho: pode criar um método para sigmoide
class Perceptron:
    def __init__(self, numero_entradas):
        self.w1 = np.random.rand(1)
        self.w2 = np.random.rand(1)
        self.bias = np.random.rand(1, 1)

    def treinamento(self, variaveis, target, taxa_aprendizado, epocas):
        for i in range(epocas):
          for j in range(len(variaveis)):
            sigmoid = 1 / (1 + np.exp(- ((variaveis[j][0] * self.w1) + (variaveis[j][1] * self.w2) + self.bias)))

            self.w1 = self.w1 + (taxa_aprendizado * (target[j][0] - sigmoid) * variaveis[j][0])
            self.w2 = self.w2 + (taxa_aprendizado * (target[j][0] - sigmoid) * variaveis[j][1])  # Correção aqui
            self.bias = self.bias + (taxa_aprendizado * (target[j][0] - sigmoid))

            print(f'Época: {i} - Erro: {target[j][0] - sigmoid} - w1: {self.w1} - w2: {self.w2} - bias: {self.bias}')
        return self.w1, self.w2, self.bias  

    def predicao(self, pesos, x1, x2):
      sigmoid = 1 if 1 / (1 + np.exp(-(x1 * pesos[0] + (x2 * pesos[1]) + pesos[2]))) > 0.5 else 0
      return sigmoid

    def acuracia(self, variaveis, target, pesos):
      acertos = 0
      for i in range(len(variaveis)):
        sigmoid = 1 if 1 / (1 + np.exp(-(variaveis[i][0] * pesos[0] + (variaveis[i][1] * pesos[1]) + pesos[2]))) > 0.5 else 0
        if sigmoid == target[i][0]:
          acertos += 1
      return f"Acurácia: {acertos/len(variaveis) * 100:.2f}%"



