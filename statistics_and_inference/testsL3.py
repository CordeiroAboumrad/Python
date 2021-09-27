import numpy as np
from scipy.stats import norm, t

amostra = np.array([14.4, 12.9, 15.0, 13.7, 13.5])

s = np.std(amostra, ddof=1)
m = np.mean(amostra)

print(s)
print(m)
print('-----------------------')

t_score = 3.25
print(f"t-score: {t_score}")

# repare que é um teste bicaudal
pvalue = 1 - t.cdf(t_score, df=19)
print(f"p-valor: {pvalue}")
