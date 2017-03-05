#import libraries
import pandas
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import model_selection
#libraries for algorithms to cross-validate
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.svm import SVC #SVM
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis #Linear Discriminant Analysis
from sklearn.naive_bayes import GaussianNB #Naive Bayes
from sklearn.neighbors import KNeighborsClassifier #K-Nearest Neighbours

'''
#read the data
train = np.loadtxt(open("maintenance_train.csv", "rb"), delimiter=",", skiprows=1) #training data
test = np.loadtxt(open("maintenance_test.csv", "rb"), delimiter=",", skiprows=0) #test data
'''

#load dataset
names = ['Lifetime', 'Broken', 'Pressure Index', 'Moisture Index', 'Temperature Index', 'Team', 'Provider']
dataset = pandas.read_csv("maintenance_data.csv", names=names)
array = dataset.values
X = array[:,0:7]
Y = array[:,6]
seed = 6 #no. of seeds

#prepare models
models = []
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

#evaluate models
results = []
names = []
scoring = 'accuracy' #scores maintained on basis of accuracy of prediction
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed) #divide data 10-fold for cross-validation
	cvresults = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	results.append(cvresults)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cvresults.mean(), cvresults.std()) #mean accuracy and standard deviation of accuracy
	print(msg)

#boxplot of algorithm comparison
figure = plt.figure()
figure.suptitle('Algorithm Comparison') #title of plot
a = figure.add_subplot(111)
plt.boxplot(results) #data to plot
a.set_xticklabels(names) #labels of x-axis
plt.show() #display plot