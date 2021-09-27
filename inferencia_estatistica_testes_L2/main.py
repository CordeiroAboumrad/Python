from scipy._lib._ccallback_c import plus1_t
from scipy.stats import t, norm
import statistics as st
import math
import pandas as pd

# for x in range(31):
#     v1 = t.ppf(0.025, x - 1)
#     print(-v1 / math.sqrt(x))
#
# print(v1)

# v2 = t.ppf(0.05, 10)
# print(v2)

# v3 = norm.ppf(0.05)
# print(v3)

t_score = (261.79 - 261.5) / (7 / math.sqrt(11))
p_value = t.cdf(t_score, df=10)
# p_value = norm.cdf(t_score)

print(t_score)
print(p_value)
