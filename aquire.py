#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import env
import os


# In[18]:


def get_connection(schema, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{schema}'

def get_titanic_data():    
    if os.path.exists('titanic.csv'):
        df = pd.read_csv('titanic.csv', index_col = 0)
    else:
        query = 'SELECT * FROM passengers'
        connection = get_connection('titanic_db')
        df = pd.read_sql(query, connection)
        df.to_csv('titanic.csv')
    return df


def get_iris_data():
    if os.path.exists('iris_db.csv'):
        df = pd.read_csv('iris_db.csv', index_col = 0)
    else:
        query = '''
        SELECT measurement_id, 
        sepal_length, 
        sepal_width, 
        petal_length,
        petal_width,
        species_name, 
        species_id
        FROM measurements 
        LEFT JOIN species 
        USING (species_id);
        '''
        connection = get_connection('iris_db')
        df = pd.read_sql(query, connection)
        df.to_csv('iris_db.csv')
    return df


def get_telco_data():    
    if os.path.exists('telco_churn.csv'):
        df = pd.read_csv('telco_churn.csv', index_col = 0)
    else:
        query = '''
        SELECT * FROM customers 
        LEFT JOIN contract_types 
        USING (contract_type_id) 
        LEFT JOIN internet_service_types 
        USING (internet_service_type_id)
        LEFT JOIN payment_types
        USING (payment_type_id);
        '''
        connection = get_connection('telco_churn')
        df = pd.read_sql(query, connection)
        df.to_csv('telco_churn.csv')
    return df


# In[ ]:




