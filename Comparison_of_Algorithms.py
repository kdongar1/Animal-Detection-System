# -*- coding: utf-8 -*-
"""approach_comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/112As6GlVuWjBz3yXwLPLqUKN-wn7llcm
"""

import numpy as np
import matplotlib.pyplot as plt

objects = ('CNN', 'XGB', 'PSO')
train_acc_score  = [99.6, 100, 98.73]
test_acc_score = [98, 96, 100]

y_pos = np.arange(3)
y_val = [x for x in train_acc_score]
plt.bar(y_pos, y_val, align='center', alpha=0.7)
plt.xticks(y_pos, objects)
plt.ylabel('Accuracy Score')
plt.title('Train Accuracy of Models')
plt.show()

y_pos = np.arange(3)
y_val = [x for x in test_acc_score]
plt.bar(y_pos, y_val, align='center', alpha=0.7)
plt.xticks(y_pos, objects)
plt.ylabel('Accuracy Score')
plt.title('Test Accuracy of Models')
plt.show()
