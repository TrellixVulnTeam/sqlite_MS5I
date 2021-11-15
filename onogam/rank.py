import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from sklearn import svm
from sklearn.metrics import confusion_matrix
import pandas as pd

data = pd.read_excel("dataset.xlsx",header=0)

y = data.loc[:,["評価"]]
yy = data["評価"]
x = data.loc[:,["データ"]]
xx = data["データ"]

clf = svm.SVC(kernel="linear")

clf.fit(x,y)

test_x =data.loc[:,["結果データ"]]
test_x = test_x.dropna(how="any",axis=1)
test_y =data.loc[:,["結果"]]

test_y = test_y.dropna(how="any",axis=1)

print(clf.predict(test_x))