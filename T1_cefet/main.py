import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
from scipy.stats import norm
import random

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
                 names=["age", "workclass", "final weight", "education", "education-num", "martial-status ",
                        "occupation", "relationship", "race", "sex", "capital-gain ", "capital-loss ",
                        "hours-per-week ", "native-country", "income"])

df.head()

# Set figure size
boxplot = plt.figure(figsize=(10, 5))

# Plot boxplot of sample - 1ª questão
plt.boxplot(df["age"])
plt.show()

# print(df[(df.income.str.contains(">50K"))])
# print(df.sex)

# 2ª questão
total_samples = len(df)
maior_50k = len(df[df.income.str.contains(">50K")])
oitenta_dado_salary_maior_50000 = len(df[(df['age'] > 80) & df.income.str.contains(">50K")])
# print(oitenta_dado_salary_maior_50000)
P_intersecao = oitenta_dado_salary_maior_50000 / total_samples

P_salario_maior_50k = maior_50k / total_samples

print(f"len(df): {total_samples}\n"
      f"len(oitenta_dado_salary_maior_50000): {oitenta_dado_salary_maior_50000}\n"
      f"Probabilidade - interseção de pessoas com mais de 80 anos e com salário superior a 50K = {P_intersecao}\n"
      f"Probabilidade - salário maior que 50K: {P_salario_maior_50k}\n")

print(f"Probabilidade de uma pessoa ter mais de 80 anos (ou seja, Age > 80) "
      f"dado que tem Salary > 50000): {P_intersecao / P_salario_maior_50k}\n")

print(f"Probabilidade de uma pessoa ter mais de 80 anos e salário maior que 50000: "
      f"{P_intersecao}")

workclass_occupation_sex = len(df[(df.workclass.str.contains("State-gov")) &
                                  (df.occupation.str.contains("Adm-clerical")) & (df.sex.str.contains("Male"))])
P_workclass_occupation_sex = workclass_occupation_sex / total_samples
print(f"Pr(Workclass = State-gov, Occupation = Adm-clerical, Sex = Male): {P_workclass_occupation_sex}")

workclass_occupation_sex2 = len(df[(df.workclass.str.contains("Self-emp-inc")) &
                                   (df.occupation.str.contains("Exec-managerial")) & (df.sex.str.contains("Male"))])
P_workclass_occupation_sex2 = workclass_occupation_sex2 / total_samples
print(f"Pr(Workclass = Self-emp-inc, Occupation = Exec-managerial, Sex = Male): {P_workclass_occupation_sex2}")

# --------------------------------------------- CASO 1 ---------------------------------------------------
print("\nCASO 1:\n")
# Média populacional
# media = df["age"].mean()
# print(f"média = {media}")
# Desvio padrão populacional
media_populacional = st.mean(df["age"])
variancia_populacional = st.variance(df["age"])
desv_pad_populacional = st.stdev(df["age"])
print(f"media população: {media_populacional}\ndesvpad populacional: {desv_pad_populacional}")
# print(
#     f"variância populacional: {variancia_populacional}\ndesvio-padrão populacional: {desv_pad_populacional}\nmédia populacional: {media_populacional}")
caso_1_negativo = media_populacional - desv_pad_populacional
caso_1_positivo = media_populacional + desv_pad_populacional
prob_neg = norm.cdf(caso_1_negativo, media_populacional, desv_pad_populacional)
prob_pos = norm.cdf(caso_1_positivo, media_populacional, desv_pad_populacional)
probabilidade_caso_1 = prob_pos - prob_neg
print(f"Probabilidade do caso 1 (populacional): {probabilidade_caso_1}")

# ---------------------------------------------- Amostra com 10 valores ----------------------------------
sample_10 = df["age"].sample(n=10)
# print(sample_10)
media_amostra_10 = st.mean(sample_10)
variancia_amostra_10 = st.variance(sample_10)
desv_pad_amostra_10 = st.stdev(sample_10)
print(f"media 10: {media_amostra_10}\ndesvpad 10: {desv_pad_amostra_10}")

caso_1_negativo_amostra_10 = media_amostra_10 - desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

# ---------------------------------------------- Amostra com 10000 valores ----------------------------------
sample_10K = df["age"].sample(n=10000)
# print(sample_10K)
media_amostra_10K = st.mean(sample_10K)
variancia_amostra_10K = st.variance(sample_10K)
desv_pad_amostra_10K = st.stdev(sample_10K)
print(f"media 10K: {media_amostra_10K}\ndesvpad populacional: {desv_pad_amostra_10K}")

caso_1_negativo_amostra_10K = media_amostra_10K - desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 2 ---------------------------------------------------
print("\nCASO 2:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 1.282 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 1.282 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 1.282 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 1.282 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 3 ---------------------------------------------------
print("\nCASO 3:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 1.645 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 1.645 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 1.645 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 1.645 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 4 ---------------------------------------------------
print("\nCASO 4:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 1.96 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 1.96 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 1.96 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 1.96 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 5 ---------------------------------------------------
print("\nCASO 5:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 2 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 2 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 2 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 2 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 6 ---------------------------------------------------
print("\nCASO 6:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 2.57 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 2.57 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 2.57 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 2.57 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

# --------------------------------------------- CASO 7 ---------------------------------------------------
print("\nCASO 7:\n")
caso_1_negativo_amostra_10 = media_amostra_10 - 3 * desv_pad_amostra_10
caso_1_positivo_amostra_10 = media_amostra_10 + 3 * desv_pad_amostra_10
prob_neg_amostra_10 = norm.cdf(caso_1_negativo_amostra_10, media_amostra_10, desv_pad_amostra_10)
prob_pos_amostra_10 = norm.cdf(caso_1_positivo_amostra_10, media_amostra_10, desv_pad_amostra_10)
probabilidade_caso_1_amostra_10 = prob_pos_amostra_10 - prob_neg_amostra_10
print(f"Probabilidade do caso 1 (amostra 10): {probabilidade_caso_1_amostra_10}")

caso_1_negativo_amostra_10K = media_amostra_10K - 3 * desv_pad_amostra_10K
caso_1_positivo_amostra_10K = media_amostra_10K + 3 * desv_pad_amostra_10K
prob_neg_amostra_10K = norm.cdf(caso_1_negativo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
prob_pos_amostra_10K = norm.cdf(caso_1_positivo_amostra_10K, media_amostra_10K, desv_pad_amostra_10K)
probabilidade_caso_1_amostra_10K = prob_pos_amostra_10K - prob_neg_amostra_10K
print(f"Probabilidade do caso 1 (amostra 10K): {probabilidade_caso_1_amostra_10K}")

