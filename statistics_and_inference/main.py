from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 13)
print(x)

norm.pdf(0, scale=1, loc=0)  # scale = variância, loc = média

ig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
stdvs = [1.0, 2.0, 3.0, 4.0]
for s in stdvs:
    ax.plot(x, norm.pdf(x, scale=s), label='stdv=%.1f' % s)

ax.set_xlabel('x')
ax.set_ylabel('pdf(x)')
ax.set_title('Normal Distribution')
ax.legend(loc='best', frameon=True)
ax.set_ylim(0, 0.45)
ax.grid(True)

norm.rvs(scale=5, loc=10, size=10)

fig, ax = plt.subplots()
xs = norm.rvs(scale=2, loc=0, size=1000000)
x = np.linspace(-10, 10, 10000)
p = norm.pdf(x, scale=2)
v = np.var(xs)
m = np.mean(xs)
ax = fig.add_subplot(111)
ax.hist(xs, bins=100, alpha=0.5, density=True)
ax.plot(x, p, 'r-', lw=2)
ax.set_xlabel('x')
ax.set_ylabel('pdf(x)')
ax.set_title(f'mean={m:.2f}, var={v:.2f}')
ax.grid(True)

x = np.linspace(-0, 100, 20)
print(x)

fig, ax = plt.subplots()
x = np.arange(-4, 4, 0.001)
ax.set_title('N(0,$1^2$)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.plot(x, norm.pdf(x))
ax.set_ylim(0, 0.45)

# Mudar o valor da média tem o efeito de transladar a curva para a esquerda ou para a direita, mantendo sua forma
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
means = [0.0, 1.0, 2.0, 5.0]
for mean in means:
    ax.plot(x, norm.pdf(x, loc=mean), label='mean=%.1f' % mean)

ax.set_xlabel('x')
ax.set_ylabel('pdf(x)')
ax.set_title('Normal Distribution')
ax.legend(loc='best', frameon=True)
ax.set_ylim(0, 0.45)
ax.grid(True)
plt.show()

# funções de distribuições acumuladas
x = np.linspace(-5, 5, 10000)

cdf_values = norm.cdf(x, scale=2)
pdf_values = norm.pdf(x, scale=2)

# plt.plot(x, pdf_values, x, cdf_values)

plt.plot(x, pdf_values, '-b', label='pdf')
plt.plot(x, cdf_values, '--r', label='cdf')

plt.grid(True)

plt.legend(loc='upper left', frameon=False)
plt.show()

# Distribuição Normal Padrão
fig, ax = plt.subplots()
x = np.arange(-4, 4, 0.001)
ax.set_title('N(0,$1^2$)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.plot(x, norm.pdf(x))
ax.set_ylim(0, 0.45)
plt.show()
