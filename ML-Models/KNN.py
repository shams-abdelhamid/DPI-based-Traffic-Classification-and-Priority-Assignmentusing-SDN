from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from preprocessing import X_train,y_train,X_test,y_test


#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))