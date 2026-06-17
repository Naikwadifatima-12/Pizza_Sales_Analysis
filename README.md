# Pizza-Sales-Analysis (Data Analysis using Python)

## Project Objective
To analyze pizza sales data to uncover revenue trends, best and worst performing products, customer ordering patterns by time, and sales distribution across categories and sizes. So that, the business owner can make data-driven decisions to maximize revenue and optimize the menu.

## Dataset used
- <a href="#">Dataset</a>

## Libraries Used
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
```

## Questions (KPIs)
- What is the Total Revenue?
- What is the Total Number of Pizzas Sold?
- What is the Total Number of Orders?
- What is the Average Order Value?
- What is the Average Number of Pizzas Per Order?
- Which day of the week has the highest number of orders? (Daily Trend - Orders)
- Which day of the week generates the most revenue? (Daily Trend - Revenue)
- Which hour of the day sees peak orders? (Hourly Trend - Orders)
- Which month has the highest number of orders? (Monthly Trend - Orders)
- What is the percentage of sales by pizza category?
- What is the percentage of sales by pizza size and category?
- Which pizza category has the most pizzas sold?
- Which are the Top 5 best-selling pizzas by quantity, orders, and revenue?
- Which are the Bottom 5 worst-selling pizzas by revenue?
- Which ingredients are used the most across all pizzas?
- Dashboard Interaction <a href="#">View Notebook</a>

## Process
- Loaded the dataset from Excel and explored its shape, data types, and statistical summary using `df.info()`, `df.dtypes`, and `df.describe()`.
- Verified data for any missing values and anomalies, and sorted out the same.
- Made sure data is consistent and clean with respect to data type, data format and values used.
- Engineered new features: `day_name`, `order_hour`, and `month_name` for time-based analysis.
- Computed 5 KPIs: Total Revenue, Total Pizzas Sold, Total Orders, Average Order Value, and Average Pizzas Per Order.
- Created 12+ charts using Matplotlib, Seaborn, and Plotly to answer each business question.

## Dashboard
![Pizza Sales Analysis Dashboard](#)

## Project Insight
- **Friday and Saturday** are the busiest days, generating the highest number of orders and revenue across the week.
- **Lunch (12 PM – 1 PM) and Dinner (5 PM – 8 PM)** hours are peak ordering times, showing clear meal-time demand spikes.
- **July and May** record the highest monthly order volumes, suggesting seasonal demand peaks.
- **Classic and Supreme** pizza categories contribute the most to total sales revenue.
- **Large-size** pizzas dominate sales across most categories, indicating customer preference for bigger portions.
- The **Top 5 best-selling pizzas** by quantity consistently align with top performers by total orders and revenue.
- The **Bottom 5 pizzas** by revenue represent underperforming menu items that may need repricing or removal.
- **Ingredient analysis** reveals the most frequently used toppings, which can guide bulk purchasing decisions.

## Final Conclusion
To improve pizza sales, a strategic plan should focus on **promoting best-selling pizzas** and **running targeted offers on Fridays and Saturdays** during peak lunch and dinner hours. Since **Large-size Classic and Supreme pizzas** drive the most revenue, upsell campaigns around these categories can significantly boost average order value. The **bottom 5 underperforming pizzas** should be reviewed for menu optimization — either through repricing, bundling, or replacement with new variants. **Ingredient-level analysis** can further support cost control and supply chain efficiency.

## Tools Used
- **Python** — NumPy, Pandas, Matplotlib, Seaborn, Plotly Express
- **Jupyter Notebook**

## 👩‍💻 Author
**Fatimajohra Naikwadi**  
Data Analyst | Excel · SQL · Power BI · Tableau · Python  
[LinkedIn](#) · [GitHub](#)
