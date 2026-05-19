#!/usr/bin/env python
# coding: utf-8

# # Pizza Sales Analysis 

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
import plotly.express as px


# ## Import Raw Data

# In[9]:


df = pd.read_excel("/Users/fatimajohranaikwadi/Downloads/pizza_sales_excel_file.xlsx")


# ## MetaData Raw Data

# In[11]:


df.head(10)


# In[12]:


df.tail()


# In[13]:


print(" The MetaData of the dataset: ",df.shape)


# In[14]:


print(" The Rows of the dataset: ",df.shape[0])


# In[15]:


print(" The Columns of the dataset: ",df.shape[1])


# In[16]:


df.columns


# In[17]:


df.info


# ### Data Types in Raw Data

# In[19]:


df.dtypes


# In[20]:


df.describe()


# ### KPI's

# In[28]:


total_revenue = df['total_price'].sum()
total_pizzas_sold = df ['quantity'].sum()
total_orders = df ['order_id'].nunique()
avg_order_value = total_revenue /total_orders
avg_pizzas_per_order = total_pizzas_sold /total_orders


print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Pizzas Sold: {total_pizzas_sold:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Avg Order Values: ${avg_order_value:,.2f}")
print(f"Avg Pizza Per Orders: {avg_pizzas_per_order:,.2f}")


# ### Charts

# #### Ingredient Analysis

# In[32]:


ingredient = (
    df['pizza_ingredients']
    .str.split(',')
    .explode()
    .value_counts()
    .reset_index()
    .rename(columns={'index': 'Count', 'pizza_ingredients': 'Ingredients'})
)

print(ingredient.head(15))


# ### Daily Trend - Total Orders

# In[40]:


df['order_date'] = pd.to_datetime(df['order_date'])

df['day_name'] = df['order_date'].dt.day_name()

weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

df['day_name'] = pd.Categorical(
    df['day_name'],
    categories=weekday_order,
    ordered=True
)

orders_by_day = df.groupby('day_name', observed=False)['order_id'].nunique()

ax = orders_by_day.plot(
    kind='bar',
    figsize=(8,5),
    color='Purple',
    edgecolor='black'
)

print(orders_by_day)


# ### Daily Trend - Total Revenue

# In[43]:


df['order_date'] = pd.to_datetime(df['order_date'])

df['day_name'] = df['order_date'].dt.day_name()

weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

df['day_name'] = pd.Categorical(
    df['day_name'],
    categories=weekday_order,
    ordered=True
)

orders_by_day = df.groupby('day_name', observed=False)['total_price'].sum()

ax = orders_by_day.plot(
    kind='bar',
    figsize=(8,5),
    color='Purple',
    edgecolor='black'
)

plt.title("Total Revenue by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)



for i,val in enumerate(orders_by_day):
    plt.text(i, val + 20, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')



plt.tight_layout()
plt.show()


# ### Hourly Trend - Total Orders

# In[44]:


df['order_time'] = pd.to_datetime(df['order_time'], format='%H:%M:%S')

df['order_hour'] = df['order_time'].dt.hour

orders_by_hour = df. groupby('order_hour', observed=False) ['order_id'].nunique ()

ax = orders_by_hour.plot(kind='bar', figsize=(10,5), color='maroon', edgecolor='black')    



plt.title("Total Orders by Hour of Day")
plt.xlabel("Hour of Day (24-Hour Format)")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)



for i,val in enumerate(orders_by_hour):
    plt.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')



plt.tight_layout()
plt.show()


# #### Monthly Trend - Total Orders

# In[51]:


df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

df ['month_name'] = df['order_date'].dt.month_name()

month_order = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]

df['month_name'] = pd.Categorical(df['month_name'], categories=month_order, ordered=True)

orders_by_month = df.groupby ('month_name', observed=False)['order_id'].nunique()

plt.figure(figsize=(10,5))
plt.fill_between(orders_by_month.index, orders_by_month.values, color="orange", alpha=0.6) 
plt.plot(orders_by_month.index, orders_by_month.values, color="black", linewidth=2, marker='o')

plt.title("Total Orders by Month") 
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
for i, val in enumerate(orders_by_month):
    plt.text(i, val + 20, str (val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### % of Sales by Category

# In[53]:


category_sales = df.groupby('pizza_category')['total_price'].sum()

category_pct = category_sales / category_sales.sum() * 100

plt.figure(figsize=(7,7))
colors = plt.get_cmap('tab20').colors  # nice color palatte

plt.pie(category_pct, labels=category_pct.index, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor':'black', 'width':0.4})
plt.title("Percentage of Sales by Pizza Category")
plt.show()


# #### % Sales b y Pizza Size & Category

# In[62]:


sales_pivot = df.pivot_table(
    index='pizza_category',
    columns='pizza_size',
    values='total_price',
    aggfunc='sum',
    fill_value=0
)


sales_pct = sales_pivot / sales_pivot.sum().sum() * 100

plt.figure(figsize=(10,6))
sns.heatmap(sales_pct, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
plt.title("% of Sales by Pizza Category and Size")
plt.xlabel("Pizza Category")
plt.ylabel("Pizza size")
plt.show()


# #### Total Pizzas Sold by Pizza Category

# In[67]:


pizzas_by_category = df.groupby('pizza_category')['quantity'].sum()

colors = list(plt.get_cmap('tab20').colors)

colors = colors[:len(pizzas_by_category)]

ax = pizzas_by_category.plot(kind='bar', figsize=(8,5), color=colors, edgecolor= 'black')

plt.title("Total Pizzas Sold by Pizza Category") 
plt.xlabel ("Pizza category") 
plt.ylabel("Total Pizzas Sold")
plt.xticks(rotation=45)

for i, val in enumerate(pizzas_by_category) :
    plt.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')


plt.tight_layout()
plt.show()


# #### Top 5 Best Selling Pizzas - Total Qty

# In[75]:


pizzas_by_name = df.groupby('pizza_name')['quantity'].sum()


top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='green', edgecolor='black')

plt.title("Top 5 Pizzas Sold")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold")
plt.xticks(rotation=45)


for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')


plt.tight_layout()
plt.show()


# #### Top 5 Best Selling Pizzas - Total Orders

# In[76]:


pizzas_by_name = df.groupby('pizza_name')['order_id'].nunique()


top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='purple', edgecolor='black')

plt.title("Top 5 Pizzas Ordered")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold")
plt.xticks(rotation=45)


for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')


plt.tight_layout()
plt.show()


# #### Top 5 Best Selling Pizzas - Total Sales

# In[78]:


pizzas_by_name = df.groupby('pizza_name')['total_price'].nunique()


top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='violet', edgecolor='black')

plt.title("Top 5 Pizzas by Revenue")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold")
plt.xticks(rotation=45)


for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')


plt.tight_layout()
plt.show()


# #### Bottom 5 Best Selling Pizzas - Total Sales

# In[82]:


pizzas_by_name = df.groupby('pizza_name')['total_price'].sum()
bottom5 = pizzas_by_name.sort_values(ascending=True).head(5)

ax = bottom5.plot(kind='bar', figsize=(8,5), color='brown', edgecolor='black')

plt.title("Bottom 5 Pizzas by Sold")
plt.xlabel("Pizza Name")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)


for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')


plt.tight_layout()
plt.show()


# In[ ]:




