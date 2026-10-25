import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def sigmoid(x): #the sigmmoid func
 return 1/(1+math.exp(-x))
def prediction(age,model): #### setting z to y=mx+c, 0 indexing is bcz they are arrays
  z= model.intercept_[0] + model.coef_[0][0] *age
  return sigmoid(z)
data=pd.read_csv("insurance_data.csv")
plt.scatter(data.age,data.bought_insurance,marker='+',color='red')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(data[['age']], data.bought_insurance, train_size=0.9)
print(X_test)
model=LogisticRegression()
model.fit(X_train,Y_train)
print(model.predict(X_test))
print(model.score(X_test,Y_test))
y_predicted=model.predict(X_test)
print(model.predict_proba(X_test))#returns probability of each answer, 1 or 0. 
#predict chooses the bigger probability one 
print("coeff")
print(model.coef_)
print("interrceppts")
print(model.intercept_)
ans=prediction(60,model)
print(ans)