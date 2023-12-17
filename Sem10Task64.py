import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# print(pd.get_dummies(data['whoAmI']))

heads=data.whoAmI.unique()
row=data['whoAmI'].tolist()
one_hot=pd.DataFrame()
for head in heads:
    list_of_res=list()
    for item in row:
        list_of_res.append(1) if item==head else list_of_res.append(0)            
    one_hot[head]=list_of_res
print(one_hot)