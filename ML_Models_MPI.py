#!/usr/bin/env python
# coding: utf-8

# IMPORTS

# In[23]:


from mpi4py import MPI
import sys
import time



# In[9]:


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("World Size: " + str(size) + "   " + "Rank: " + str(rank))


# In[10]:


# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics 
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.feature_selection import VarianceThreshold
from imblearn.combine import SMOTETomek
from imblearn.combine import SMOTEENN
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


# READING DATASET AND EXAMINING LABEL
# 

# In[11]:


dataset = pd.read_csv("c:/Darknet_all.csv" , low_memory=False) 
df = pd.DataFrame(dataset)
#display(df)


# After examining the Label values , we found out some duplicate classes so we dropped them .

# In[12]:





dup_values = ['Video-streaming', 'AUDIO-STREAMING','File-transfer' ]
df = df[df.Label.isin(dup_values) == False]    #returing df without duplicated classes



# Missing data is data which is not available ( NULL) or infinite values , we will remove the rows which contain any missing data. This shall not affect the model as the dataset is big enough.

# In[13]:




df.replace([np.inf, -np.inf], np.nan, inplace=True) #replace infinity values with NaN
df.dropna(inplace=True) #dropping rows with missing values  



# Dropping unneccassory features like id ,and converting ips to binary then int..

# In[14]:


df.drop('Flow ID', axis=1, inplace=True)


i=0
for ip in df['Src IP'].values:
    z = 0
    parts = ip.split('.')
    z = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    ip= z
    df['Src IP'].values[i]=ip
    i=i+1



i=0    
for ip in df['Dst IP'].values:
    z = 0
    parts = ip.split('.')
    z = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    ip= z
    df['Dst IP'].values[i]=ip
    i=i+1


# Removing 0 variance features..

# In[15]:





df_nolabel = df.iloc[:,:-1].values

sel = VarianceThreshold(threshold=0)    
sel.fit_transform(df_nolabel)
arr=sel.get_support()

arr1=np.argwhere(arr == 0)

features_to_remove=[]
for i in arr1 :
    features_to_remove.append((df.columns[i].values[0]))

df.drop(features_to_remove, axis=1, inplace=True)

# Features scaling and splitting the dataset into training and testing subsets.

# In[16]:


count=df.shape[1]
x = df.iloc[:,:-1].values
y = df.iloc[:, count-1].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


MPIstart = time.time()
TtimeMPI=0

if rank == 0:
    XsliceTR = np.array_split(X_train, 3)
    YsliceTE = np.array_split(y_train, 3)


    comm.send(dest=1, obj=[XsliceTR[0],YsliceTE[0]])
    comm.send(dest=2, obj=[XsliceTR[1],YsliceTE[1]])
    comm.send(dest=3, obj=[XsliceTR[2],YsliceTE[2]])
    
if rank != 0:
    slice = comm.recv(source=0)
    TRslice=slice[0]
    TEslice=slice[1]
    
    clf=RandomForestClassifier(n_estimators=100)

    clf = clf.fit(TRslice, TEslice)
    
    comm.send(dest=0, obj=clf)
    
if rank == 0:
    
    
    Slice1_clf = comm.recv(source=1)
    Slice2_clf = comm.recv(source=2)
    Slice3_clf = comm.recv(source=3)

    super_clf=Slice1_clf
    
    total_ests = Slice1_clf.estimators_ + Slice2_clf.estimators_ + Slice3_clf.estimators_
    
    
    super_clf.estimators_ = total_ests
    
    y_pred = super_clf.predict(X_test)
    #print(classification_report(y_test, y_pred))
    
    MPIend = time.time()

    TtimeMPI = MPIend-MPIstart

    print("time taken MPI= ",TtimeMPI)
    
    
    
# SMOTE technique to overcome dataset imbalance ..

# In[17]:



#counter = Counter(y_train) 
#print('Before', counter) 
#smtom = SMOTEENN () 
#X_train_smtom, y_train_smtom = smtom.fit_resample (X_train, y_train)
#counter = Counter(y_train_smtom) 
#print('After', counter)


# In[19]:



# Train Decision Tree Classifer
#clf = DecisionTreeClassifier()
#clf = clf.fit(X_train_smtom, y_train_smtom)
#clf = clf.fit(X_train, y_train)
#Predict the response for test dataset
#y_pred = clf.predict(X_test)

#print(classification_report(y_test, y_pred))


# In[ ]:




#Create KNN Classifier
#knn = KNeighborsClassifier(n_neighbors=5)

#Train the model using the training sets
#knn.fit(X_train_smtom, y_train_smtom)

#Predict the response for test dataset
#y_pred = knn.predict(X_test)
#print(classification_report(y_test, y_pred))


# In[21]:

print("####################################################################################")

start = time.time()


clf=RandomForestClassifier(n_estimators=100)
#clf = clf.fit(X_train_smtom, y_train_smtom)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
#print(classification_report(y_test, y_pred))

end = time.time()

Ttime = end-start

print("time taken = ",Ttime)

if TtimeMPI != 0:
    print("MPI consumed ",Ttime-TtimeMPI," less")

    print("Time effeciency = ",int((TtimeMPI/Ttime)*100)," %")

# In[ ]:




