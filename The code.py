#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd # import pandas libary.
from sklearn.neighbors import KNeighborsRegressor # import K Neighbors Regressor.
import matplotlib.pyplot as plt
#plt.style.use('dark_background')


# In[2]:


df = pd.read_excel('Source_Data.xlsx', skiprows=5) # import the source data.
df = df[df['tij'] > 0]   # remove measurement errors (t=0).
x = df[["DayOrder","Season","DayOfWeek","Period"]] # put the features together in x.
t = df[["tij"]]          # put the time alone in t.
x20 = pd.read_csv('2020x.csv') # import csv file contain the features for 2020.

print("features for years 2017,2018,2019:\n",x)
print("time for years 2017,2018,2019:\n",t)
print("features for year 2020:\n",x20)


# # K Neighbors Regression (Forecast)

# In[3]:


knnreg = KNeighborsRegressor(n_neighbors = 2, p = 1,algorithm = 'brute',
                             weights = 'distance').fit(x, t) # build the model.

t20 = pd.DataFrame(knnreg.predict(x20),columns=["tij"])
# using the model to forecast the time based on 2020 features.
y2020 = pd.concat([x20, t20], axis=1) # merge the features with its forecast.
y2020.to_csv(r'year2020_Forecast.csv', index = False) # Export the Results.


# # Show the results

# In[7]:


# Comparison between some stats of measured time (2017,2018,2019) and forecasted time (2020)
# the Small differences indicate the forecast is good.
print("Mean difference:", pd.DataFrame.mean(t)-pd.DataFrame.mean(t20))
print("Max difference:", pd.DataFrame.max(t)-pd.DataFrame.max(t20))
print("Min difference:", pd.DataFrame.min(t)-pd.DataFrame.min(t20))
print("STD difference:", pd.DataFrame.std(t)-pd.DataFrame.std(t20))

t.boxplot(color='g') # box plot for measured time.
t20.boxplot(color='r') # box plot for forecasted time.
plt.legend(['t','t20']).legendHandles[1].set_color('r') # set legend.
plt.show() # box plot can visualize the differences.

print("time for year 2020:\n",y2020.head(15)) # year 2020 with the forecast.


# In[8]:


t.plot(kind='hist',color='g') # plot histogram
t20.plot(kind='hist',color='r') # The two histograms are similar.
pd.plotting.scatter_matrix(df, diagonal='kde', figsize=(12,12)) #last row show the relationship of time with the features.
pd.plotting.scatter_matrix(y2020, diagonal='kde', figsize=(12,12))
# the two scatter matric show how the data are similar but there are some differences.
plt.show()

