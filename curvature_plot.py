import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)
plt.show()