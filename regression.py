import pandas as pd
import numpy as np
from sklearn.linear_model import *
from sklearn.svm import *

train_data_df = pd.read_csv('train.csv',delimiter=',',header = None)
test_data_df = pd.read_csv('test.csv',header = None ,delimiter=",")

train_data_df.columns = ['Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales']
test_data_df.columns = ['Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type']

labels_numeric = pd.Series(train_data_df['Item_Outlet_Sales'],dtype = "float")
labels_numeric = labels_numeric.astype(np.float)
train_data_df = train_data_df.drop('Item_Outlet_Sales',1)

train_data_df = np.array(train_data_df)
test_data_df = np.array(test_data_df)

my_model = LinearRegression()
my_model = my_model.fit(X=train_data_df, y=labels_numeric)
test_pred = my_model.predict(test_data_df)

f1 = open('id.csv')
id_list = []
for i in f1 :
	j = i.strip()
	id_list.append(j)

f = open('test_results.csv','w')
f.write("Item_Identifier,Outlet_Identifier,Item_Outlet_Sales\n")

for i in range(len(test_pred)) :
	j = str(test_pred[i])
	f.write(str(id_list[i])+","+str(j)+"\n")
