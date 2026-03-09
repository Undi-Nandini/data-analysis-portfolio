#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def load_dataset(path):
    """
    Load dataset and display basic information
    """
    df = pd.read_csv(path)
    print("Dataset Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Missing Values:\n", df.isnull().sum())
    return df


def basic_statistics(df):
    """
    Return basic statistical summary
    """
    return df.describe()


def correlation_matrix(df):
    """
    Generate correlation matrix
    """
    return df.corr()


# In[ ]:




