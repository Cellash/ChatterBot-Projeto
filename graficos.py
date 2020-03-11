import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read(arquivo):
    leitura = pd.read_csv(arquivo, encoding='utf-8', sep=';')
    return leitura


dataset = read('dados1.csv')
dataset = dataset.drop()
print(dataset)





# height = [3, 12, 5, 18, 45]
# bars = ('A', 'B', 'C', 'D', 'E')
# y_pos = np.arange(len(bars))
#
# # Create bars
# plt.bar(y_pos, height)
#
# # Create names on the x-axis
# plt.xticks(y_pos, bars)
#
# # Show graphic
# plt.show()
