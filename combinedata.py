# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:19:33 2019

@author: SUTIRTHA PAL
"""

import pandas as pd

df0=pd.read_csv('user0.csv')
df1=pd.read_csv('user1.csv')
df2=pd.read_csv('user2.csv')
df3=pd.read_csv('user3.csv')
df4=pd.read_csv('user4.csv')
df5=pd.read_csv('user5.csv')

df=df0.append(df1,ignore_index=True)
df=df.append(df2,ignore_index=True)
df=df.append(df3,ignore_index=True)
df=df.append(df4,ignore_index=True)
df=df.append(df5,ignore_index=True)

#df1=df[['lr','rl','Lr','Rl','ll','rr','l','r','L','R','Space','Enter','cpm','y']]

df.to_csv('data_final.csv',index=False)