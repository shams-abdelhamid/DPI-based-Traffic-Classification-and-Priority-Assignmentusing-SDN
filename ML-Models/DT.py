from preprocessing import x,y
from sklearn import metrics
from preprocessing import X_train,y_train,X_test,y_test



from sklearn.tree import DecisionTreeClassifier 
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)


#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeClassifier 
#kf = KFold(n_splits=20)
#clf_tree=DecisionTreeClassifier()
#scores = cross_val_score(clf_tree, x, y, cv=kf)

#avg_score = np.mean(scores)
#print(avg_score)