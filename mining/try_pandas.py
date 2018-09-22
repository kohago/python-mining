'''
Created on 2018/04/30

@author: syuu
'''
import pandas as pd
from matplotlib import pyplot

indata = [('Toms', 174, 75), ('Jam', 144, 45), ('Lily', 114, 25)]
df = pd.DataFrame(data = indata, columns= ['name','weight','length'], index = ['one','two','threes'])

print(df)
print("====================")
print(df['name'])
print("====================")
print(df[['name','length']])
print("====================")
print(df['weight'].sum())

df['length'].plot.bar()
pyplot.show()