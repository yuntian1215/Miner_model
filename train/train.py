import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt #导入作图库
import joblib

good_train=pd.read_csv("./Dataset/goodtrain.csv")
bad_train=pd.read_csv("./Dataset/badtrain.csv")
good_test=pd.read_csv("./Dataset/goodtest.csv")
bad_test=pd.read_csv("./Dataset/badtest.csv")
train=pd.concat([good_train,bad_train],ignore_index=True)
# train=train.append(good_train,ignore_index=True)
# train=train.append(bad_train,ignore_index=True)
test=pd.concat([good_test,bad_test],ignore_index=True)
# test=test.append(good_test,ignore_index=True)
# test=test.append(bad_test,ignore_index=True)
train.to_csv("train.csv")
test.to_csv("test.csv")
# train=pd.read_csv("train.csv")
# test=pd.read_csv("test.csv")

X_train=train.drop(["Label","URL"],axis=1)
X_test=test.drop(["Label","URL"],axis=1)
X_train=X_train.drop(X_train.columns[0],axis=1)
X_test=X_test.drop(X_test.columns[0],axis=1)
y_train=train["Label"]
y_test=test["Label"]

model_RF = RandomForestClassifier(n_estimators=50)#参数是随机森林中的决策树数量，可进行更改
model_RF.fit(X_train, y_train)
y_pred = model_RF.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
joblib.dump(model_RF,"model.pkl")
print("Accuracy:", accuracy)
