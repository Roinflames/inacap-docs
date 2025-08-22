'''
Aprendizaje supervisado
Entrenamiento
Python y Machine Learning
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")

# Preprocesamiento básico
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})
train['Age'] = train['Age'].fillna(train['Age'].median())
test['Age'] = test['Age'].fillna(train['Age'].median())

X = train[['Pclass', 'Sex', 'Age']]
y = train['Survived']

clf = RandomForestClassifier(n_estimators=100, verbose=1)
clf.fit(X, y)

# Predicciones
pred = clf.predict(test[['Pclass', 'Sex', 'Age']])
print(pred)
output = pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': pred})
output.to_csv('submission.csv', index=False)