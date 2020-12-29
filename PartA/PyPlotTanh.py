import numpy as np
'''
import matplotlib as mpl
mpl.use('Agg')
'''
import matplotlib.pyplot as plt
x = np.linspace(-100, 100, 1000)

y = np.tanh(x)

plt.plot(x, y, label = "label", color = "red", linewidth = 2)
plt.xlabel("abscissa")
plt.ylabel("ordinate")
plt.title("tanh Example")
plt.show()