import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, confusion_matrix, plot_confusion_matrix, roc_curve, \
    f1_score, recall_score, precision_score, classification_report

heart_data = pd.read_csv("/home/yuxuan/kaggle/heart_failure_clinical_records_dataset.csv")
heart_data.head()

accuracy_list = []

X = heart_data.iloc[:, 0:11]
X = StandardScaler().fit_transform(X)
y = heart_data['DEATH_EVENT']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, random_state=1)

sv_clf = SVC(kernel="linear",random_state=1)
sv_clf.fit(X_train, y_train)
sv_clf_pred = sv_clf.predict(X_test)
sv_clf_acc = accuracy_score(y_test, sv_clf_pred)
sc_clf_f1 = f1_score(y_test, sv_clf_pred)
sc_clf_recall = recall_score(y_test, sv_clf_pred)
sc_clf_precision = precision_score(y_test, sv_clf_pred)

# sv_clf_default = SVC(random_state=1)
# sv_clf_default.fit(X_train, y_train)
# sv_clf_pred_default = sv_clf_default.predict(X_test)
# sv_clf_acc_default = accuracy_score(y_test, sv_clf_pred_default)


accuracy_list.append(round(sv_clf_acc, 2))
# accuracy_list.append(round(sv_clf_acc_default, 2))
accuracy_list.append(round(sc_clf_f1, 2))
accuracy_list.append(round(sc_clf_recall, 2))
accuracy_list.append(round(sc_clf_precision, 2))

print(accuracy_list)
print(classification_report(y_test, sv_clf_pred))
