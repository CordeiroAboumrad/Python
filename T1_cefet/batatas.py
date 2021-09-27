from scipy.stats import expon, norm
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
import statistics as st
import random
import math
import seaborn as sns

# Aproximação por LLN
sample = [random.randint(10, 20) for x in range(0, 100000)]
bin_edges = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# print(sample)
plt.hist(sample, density=True, bins=bin_edges)
plt.xlim([0, 30])
plt.xlabel('número de batatas')
plt.ylabel('frequência relativa')
plt.show()

media = (20 + 10) / 2
print(f"Média: {media}")
variancia = ((11 * 11) - 1) / 12
print(f"Variância: {variancia}")
desvio_padrao = math.sqrt(variancia)
print(f"Desvio-padrão: {desvio_padrao}")

# ---------------------------------- DISTRIBUIÇÃO AMOSTRAL PARA AS MÉDIAS AMOSTRAIS --------------------
# Número de sacos é igual a 2
amostras = []
for i in range(10, 21):
    for j in range(10, 21):
        amostras.append((i, j))

medias = [st.mean(x) for x in amostras]
print(amostras)
print(medias)

tamanho_total_medias = len(medias)

valores_medias = []
quantidades_valores_medias = []
for x in set(medias):
    frequencia = medias.count(x)
    print(f"x: {x}\nquantidade: {frequencia}")
    valores_medias.append(x)
    quantidades_valores_medias.append(frequencia)

rounded_medias = [round(x, 1) for x in medias]
print(rounded_medias)

# plt.plot(valores_medias, quantidades_valores_medias)


plt.title('Distribuição Amostral - x médio')
# bins = [x for x in range(10, 21, 1)]

plt.hist(rounded_medias, density=False, bins=21, edgecolor='black')
# plt.xlim([9, 21])
plt.show()

media = (20 + 10) / 2
print(f"Média: {media}")
n = len(set(medias))
print(f"O número n é igual a {n}.")
variancia = ((n * n) - 1) / 12
print(f"Variância: {variancia}")
desvio_padrao = math.sqrt(variancia)
print(f"Desvio-padrão: {desvio_padrao}")

# ---------------------------------- DISTRIBUIÇÃO AMOSTRAL PARA A AMOSTRAL AMOSTRAL --------------------
# Número de sacos é igual a 2
amostras = []
for i in range(10, 21):
    for j in range(10, 21):
        amostras.append((i, j))

amplitudes = [max(x) - min(x) for x in amostras]
print(amostras)
print(amplitudes)

tamanho_total_medias = len(amplitudes)

valores_amplitudes = []
quantidades_valores_amplitudes = []
for x in set(amplitudes):
    frequencia = amplitudes.count(x)
    print(f"x: {x}\nquantidade: {frequencia}")
    valores_amplitudes.append(x)
    quantidades_valores_amplitudes.append(frequencia)

plt.hist(amplitudes, density=False, bins=11, edgecolor='black')
# plt.hist(amplitudes)
# plt.plot(valores_amplitudes, quantidades_valores_amplitudes)
plt.title('Distribuição Amostral - Amplitude')

# bins = [x for x in range(10, 21, 1)]
#
# plt.hist(medias, density=True, bins=bins, edgecolor='black')
# plt.xlim([10, 21])
plt.show()
