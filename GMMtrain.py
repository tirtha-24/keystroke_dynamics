# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:34:01 2019

@author: SUTIRTHA PAL
"""

import numpy as np
import pandas as pd
from sklearn.externals.six.moves import xrange
from sklearn.mixture import GaussianMixture as GMM
from sklearn.externals import joblib

#from sklearn.decomposition import PCA
#import matplotlib.pyplot as plt

train=pd.read_csv('data_final.csv',header=0)

#Separate out X_train and y_train

X=train
y=train

X=X.drop(['y'],axis=1) #remove the output label column

y=y.drop(['lr','rl','lR','Lr','rL','Rl','lL','rR','ll','rr','l','r','L','R','Space','Enter',
                                     'Backspace','cpm'],axis=1) #remove all the columns except the output label

X=X.values
y=y.values

X_train=X
y_train=y

#GMM
n_classes=len(np.unique(y_train)) # should be 6 
print(n_classes)

classifiers = dict((covar_type, GMM(n_components=n_classes,
                    covariance_type=covar_type,max_iter=60))
                   for covar_type in ['tied'])
                       
n_classifiers = len(classifiers)

#print X_train.shape
#print X_train[0]


for index, (name, classifier) in enumerate(classifiers.items()):
    
    #Initializing the Means of the GMM manually
#    print("X_train.shape:", X_train.shape)
#    print("y_train.shape:", y_train.shape)
    
    y_train = y_train.flatten()

#    z = y_train == (0+1)
#    print("z.shape", z.shape)
#    print("X_train[y_train == (0+1)].shape:", X_train[y_train == (0+1)].shape)
    classifier.means_init = np.array([X_train[y_train == (i)].mean(axis=0)
                                  for i in xrange(n_classes)])
#    print("classifier.means_:", classifier.means_)                                  
    #Fitting the training data
    classifier.fit(X_train)
#    #Predictions
    y_train_pred = classifier.predict(X_train)   
    train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    print ("The accuracy in training is ",train_accuracy,"\n") 
    joblib.dump(classifier,'GMMclassifier.pkl')