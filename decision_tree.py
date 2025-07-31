from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(x_train, y_train)

y_pred = dtree.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
classification = classification_report(y_test, y_pred)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(12,6))
plot_tree(dtree, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()