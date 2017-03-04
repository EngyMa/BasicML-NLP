#import all required libraries
import csv
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt 
#from sklearn import datasets
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#load iris dataset for trial; dataset obtained from UCI archive
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
url = "iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#dimensions of dataset as (no. of instances, no. of attributes)
print(dataset.shape)

'''
#display some instances of dataset; head or tail
print(dataset.tail(40))
'''

#statistical summary of each attribute
print(dataset.describe())

'''
#univariate plot to understand each attribute
#histograms
dataset.hist()
plt.show()
'''


#multivariate plot to understand relationship between attributes
scatter_matrix(dataset)
plt.show()
