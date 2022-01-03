# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.preprocessing import MinMaxScaler

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 


dataset = pd.read_csv("c:/Darknet_all.csv" , low_memory=False) 
df = pd.DataFrame(dataset)
df = df.replace([np.inf, -np.inf], 0).fillna(0)
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


x = df.iloc[:,:-1].values
y = df.iloc[:, 81].values


scaler = StandardScaler().fit(x)
x = scaler.transform(x)






