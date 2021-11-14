import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix
import pandas as pd

data = pd.read_excel("dataset.xlsx",header=0)


y = data["評価"]
x = data["データ"]
print(y[::])

#clf = svm.SVC(kernel="linear")

#clf.fit(x,y)
