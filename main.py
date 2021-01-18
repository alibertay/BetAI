import numpy as np
data = np.genfromtxt('data.csv', delimiter=',')
target = np.genfromtxt('target.csv')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

home = input("Ev sahibi takımının ELO ratingi: ")
away = input("Deplasman takımının ELO ratingi: ")

X_new = np.array([[int(home), int(away)]])
predict = knn.predict(X_new)

y_predict = knn.predict(X_test)

print("{probablity} ihtimalle maçın skoru: {score}".format(probablity=np.mean(y_predict==y_test), score=predict))
