from scipy.stats import expon, norm
import matplotlib.pyplot as plt
import statistics as st
import seaborn as sns

# n = quantidade de valores a gerar
# lambda= taxa (rate)
# 1/lambda = média da distribuição exponencial

lam = 0.2
n = 40

variancias = []
simulacoes = []
for x in range(1, 1001):
    amostra = expon.rvs(size=n, loc=(1 / lam), scale=(1 / lam))
    media_amostra = st.mean(amostra)
    variancia_amostra = st.variance(amostra)
    simulacoes.append(media_amostra)
    variancias.append(variancia_amostra)

# print(simulacoes)
# plt.hist(simulacoes)
# plt.xlim([0, 20])


# Density Plot and Histogram of all arrival delays
sns.distplot(simulacoes, hist=True, kde=True,
             bins=5, color='darkblue',
             hist_kws={'edgecolor': 'black'},
             kde_kws={'linewidth': 4})

plt.plot()
plt.show()
# print(media_amostra)

media_teorica = 1 / lam
variancia_teorica = 1 / (lam * lam)
media = st.mean(simulacoes)
variancia = st.mean(variancias)

print(f"Média Teórica: {media_teorica}\nMédia: {media}\n"
      f"Variância Teórica: {variancia_teorica}\nVariância: {variancia}")
