#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

tabuleiro = np.tile([1, 0], (8, 4))

for i in range(tabuleiro.shape[0]):
    tabuleiro[i] = np.roll(tabuleiro[i], i % 2)

mapa_cores = ListedColormap(['#000000', '#FFFFFF'])
plt.matshow(tabuleiro, cmap=mapa_cores)
plt.xticks([])
plt.yticks([])
plt.show()

