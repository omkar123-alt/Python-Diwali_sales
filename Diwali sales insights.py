#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# !pip install numpy


# In[3]:


df = pd.read_csv(r"C:\Users\OMKAR\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv",encoding = 'unicode_escape')


# In[4]:


df


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.info()


# In[9]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'], axis = 1, inplace = True)


# In[10]:


pd.isnull(df).sum()


# In[11]:


df.shape


# In[12]:


# drop null values
df.dropna(inplace = True)


# In[13]:


df.shape


# In[14]:


df['Amount'] = df['Amount'].astype('int')


# In[15]:


df['Amount'].dtypes


# In[16]:


df.columns


# In[40]:


# rename columns
df.rename(columns = {'Marital_Status': 'Shaadi'},inplace = True)


# In[41]:


df


# In[42]:


df.describe()


# In[43]:


# use describe() for specific columns


# In[44]:


df[['Age','Orders','Amount']].describe()


# In[45]:


# Exploratory Data Analysis

# Gender


# In[46]:


ax = sns.countplot(x = 'Gender', data = df)
for bar in ax.containers:
    ax.bar_label(bars)


# In[26]:


df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[27]:


sales_gen = df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# In[28]:


# Age


# In[29]:


ax = sns.countplot(x = 'Age Group', data = df , hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_age = df.groupby(['Age Group'], as_index = False )['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# In[31]:


sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.set(rc={'figure.figsize':(15,5)})

sns.barplot(x = 'State', y = 'Orders' , data = sales_state)


# In[32]:


sales_state = df.groupby(['State'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.set(rc={'figure.figsize':(15,5)})

sns.barplot(x = 'State', y = 'Amount', data = sales_state)


# In[49]:


df.columns


# In[50]:


ax = sns.countplot(x = 'Shaadi', data = df)

sns.set(rc={'figure.figsize':(6,3)})

for bars in ax.containers:
    ax.bar_label(bars)
    


# In[54]:


sales_state = df.groupby(['Shaadi', 'Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.barplot(x = 'Shaadi', y = 'Amount', hue = 'Gender', data = sales_state)
                          


# In[76]:


ax = sns.countplot(x = 'Occupation', data = df)

sns.set(rc={'figure.figsize':(23,7)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


sales_state = df.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.barplot(x = 'Occupation', y = 'Amount', data = sales_state)


# In[75]:


ax = sns.countplot(x = 'Product_Category', data = df)

sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[78]:


sales_state = df.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.barplot(x = 'Product_Category', y = 'Amount', data = sales_state)


# In[82]:


sales_state = df.groupby(['Product_ID'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.barplot(x = 'Product_ID', y = 'Orders', data = sales_state)


# In[ ]:




