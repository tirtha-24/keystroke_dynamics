# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:09:25 2019

@author: SUTIRTHA PAL
"""

import pandas as pd
df=pd.read_csv('data.csv')

df0=df[df.y==0]
train=df0.sample(frac=0.7,random_state=99)
test=df0.loc[~df0.index.isin(train.index),:]
train.to_csv('user0.csv',index=False)
test.to_csv('testuser0.csv',index=False)

df1=df[df.y==1]
train=df1.sample(frac=0.7,random_state=99)
test=df1.loc[~df1.index.isin(train.index),:]
train.to_csv('user1.csv',index=False)
test.to_csv('testuser1.csv',index=False)

df2=df[df.y==2]
train=df2.sample(frac=0.7,random_state=99)
test=df2.loc[~df2.index.isin(train.index),:]
train.to_csv('user2.csv',index=False)
test.to_csv('testuser2.csv',index=False)

df3=df[df.y==3]
train=df3.sample(frac=0.7,random_state=99)
test=df3.loc[~df3.index.isin(train.index),:]
train.to_csv('user3.csv',index=False)
test.to_csv('testuser3.csv',index=False)


df4=df[df.y==4]
train=df4.sample(frac=0.7,random_state=99)
test=df4.loc[~df4.index.isin(train.index),:]
train.to_csv('user4.csv',index=False)
test.to_csv('testuser4.csv',index=False)


df=pd.read_csv('final_mean.csv')
df=df.drop('index',axis=1)
df.to_csv('user5.csv',index=False)
df=pd.read_csv('final_mean1.csv')
df=df.drop('index',axis=1)
df.to_csv('testuser5.csv',index=False)