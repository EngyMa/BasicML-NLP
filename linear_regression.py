#import libraries
from datetime import datetime
import pandas as p 
from sklearn.linear_model import LinearRegression

#time
start = datetime.now()

x = p.read_csv("default of credit card clients.csv", usecols=[0], skiprows=2)
y = p.read_csv("default of credit card clients.csv", usecols=[1], skiprows=2)
model = LinearRegression()
model.fit(x, y)

#predict
x_p = [62541]
y_p = model.predict(x_p)

print(y_p)

#time
end = datetime.now()
print("Duration: {}".format(end - start)) #running time