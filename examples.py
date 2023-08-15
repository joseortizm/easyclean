from easyclean import clean
#import numpy as np 
import pandas as pd
import random as rd

#m = clean.test('jose')
#print(m)

#dataframe for testing
path = 'test.csv'
df = pd.read_csv(path, encoding = 'unicode_escape')
#print(df.head())
#print(df.isnull().sum())
newDf = df.dropna()
#print(newDf.isnull().sum())
comments = newDf['text']
#print(comments.head())
comments_list = list(comments)
#print(len(comments_list))
#print(comments_list)

#5 comments 
randomComments = rd.sample(comments_list, 5)
#print(randomComments)

#examples
#one comment
print(randomComments[0])
posRegular = clean.rex(randomComments[0]) #check space when start
print(posRegular)
#manual comment
comentario = '   @handz  a z y Z ~it: ^ } :-* was_] HOLA  ` A B :D :=D :) :() @{ quiet [.... <> % unfortunatly!!!!! http://www.google.com' # pend with: _ 
print(comentario) 
posRegularText = clean.rex(comentario)
print(posRegularText)







