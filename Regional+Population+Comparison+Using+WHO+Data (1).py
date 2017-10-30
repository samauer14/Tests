
# coding: utf-8

# In[18]:

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib

import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

import numpy as np

import pandas as pd


# In[27]:

def generate_graph_with_region(region):
    return generate_graph_with_region.plot.bar(x='Country',y='Population',title='Region Population Comparison',legend=False)


# In[19]:

#reading the WHO data used previously in this course
#regions are Africa, Europe, Americas, Eastern Mediterranean, South-East Asia, Western Pacific
who_df = pd.read_csv('../data/WHO.csv')


# In[20]:

assert isinstance(who_df, pd.DataFrame)
assert who_df.shape == (194, 13)
assert list(who_df.columns.values) == ['Country', 'Region', 'Population', 'Under15', 'Over60',
       'FertilityRate', 'LifeExpectancy', 'ChildMortality',
       'CellularSubscribers', 'LiteracyRate', 'GNI',
       'PrimarySchoolEnrollmentMale', 'PrimarySchoolEnrollmentFemale']


# In[21]:

#Parsing the dataset down into the relevant columns 
who_df= who_df[['Region','Country','Population']]


# In[22]:

assert list(who_df.columns.values) == ['Region','Country','Population']


# In[23]:

#Setting Region as the index as that is how I am sorting them
who_df=who_df.set_index('Region')


# In[24]:

print ("Please enter a region.")
print ("Africa, Europe, Americas, Eastern Mediterranean, South-East Asia, or Western Pacific are your choices.")


# In[25]:

#returning the data for the entered region

generate_graph_with_region=who_df.loc[input(), : ]


# In[ ]:

#print bar graph using data for the inputed region
generate_graph_with_region.plot.bar(x='Country',y='Population',title='Region Population Comparison',legend=False)

