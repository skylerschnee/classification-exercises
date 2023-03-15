#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[5]:


def prep_iris(df):
    '''
    prep_iris will take in a single pandas dataframe and will
    proceed to drop redundant columns and non-usefull info in 
    addition to encoding categorical variables for iris_data specifically
    '''
    df = df.drop(columns = ['measurement_id', 'species_id'])
    df = df.rename(columns= {'species_name':'species'})
    df = pd.concat([df,pd.get_dummies(df['species'], drop_first = True)], axis = 1)
    return df

def prep_titanic(df):
    '''
    prep titanic will take in a single pandas dataframe and will
    proceed to drop redundant columns and non-usefull info in 
    addition to addressing null values and encoding categorical variables
    for titanic_data specifically
    '''
    #drop redundancies
    df = df.drop(columns=['class', 'deck', 'passenger_id'])
    
    #impute avg age and most common embark_town:
    df['age'] = df['age'].fillna(df.age.mean())
    df['embark_town'] = df['embark_town'].fillna('Southampton')
    
    # encode categorical values
    df = pd.concat([df, pd.get_dummies(df[['sex', 'embark_town']], drop_first = True)], axis = 1)
    
    return df

def prep_telco(df):
    '''
    prep_telco will take in a single pandas dataframe and will
    proceed to drop redundant columns and non-usefull info in 
    addition to encoding categorical variables for telco_data specifically
    '''
    #drop redundancies
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
    
    # encode categorical values
    df = pd.concat([df, pd.get_dummies(df[['payment_type', 'internet_service_type', 'contract_type']], drop_first = True)], axis = 1)
    
    return df



# In[ ]:




