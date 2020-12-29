


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

normal = np.random.rand(12, 15)


sns.heatmap(normal, vmin=0, vmax=1)

plt.show()
