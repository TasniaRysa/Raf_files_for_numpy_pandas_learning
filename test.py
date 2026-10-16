import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data=pd.read_csv("student_scores.csv")
#data.plot()
#plt.show()
x=data.iloc[:,:-1].values #x carries from 0 to last column exxcept last column. since it has only 2 columns, it will carry only first column
y=data.iloc[:,1].values #y carries only last column
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2, random_state=0) #0.2 percent of data will be used for testing and 80 percent for training.
#random_state=0 is used to get same result every time we run the code
lmodel=LinearRegression()
#instance of linear regression model created

print(lmodel.fit(X_train, Y_train))
print(X_train)
print(lmodel.intercept_) #intercept is the value of y when x=0
print(lmodel.coef_) #coefficient is the slope of the line

Y_pred=lmodel.predict(X_test) #predicts the values of y for the given x values in X_test
print(Y_pred)