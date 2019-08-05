# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:08:33 2019

@author: SUTIRTHA PAL
"""

import pandas as pd
from sklearn.externals import joblib

#Feature Extraction part
#Output - array of input (n,N_features)
def func(p):
  X_test=pd.read_csv('testnew.csv',header=0)  #test file


  X_test=X_test[['lr','rl','lR','Lr','rL','Rl','lL','rR','ll','rr','l','r','L','R','Space','Enter',
                                     'Backspace','cpm']]
  X_test=X_test.values
  GMM_classifier=joblib.load('GMMclassifier.pkl')
  y_test=GMM_classifier.predict(X_test)

  Person={0:'Astha',1:'Arti',2:'Shreya',3:'Deeksha',4:'Abhilasha',5:'Sutirtha'}

  y_test_length=len(y_test)
  y_=y_test.tolist()
  k=0;
  for i in range(len(y_)):
    if(y_[i]==p):
      k=k+1;
#print(k)
  acc=k/len(y_)*100
  print(acc)
  if acc>60:
      return True
  else:
      return False
  mode=max(set(y_), key=y_.count)
  frequency=y_.count(mode)
#print(mode)
#print(frequency)
  accuracy=float(frequency)/len(y_)*100

  if  accuracy > 50:
      print ("The Person identified typing is ", Person[mode],"with",round(accuracy,2),'% accuracy')
  else:
      print ("Impostor!")
