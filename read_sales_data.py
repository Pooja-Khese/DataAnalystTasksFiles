# import pandas as pd

# # Step 1: Read Data
# data = pd.read_csv('sales_data.csv')

# # Step 2: Handle Missing Values (if any)
# # Example: Filling missing values in 'Quantity' column with the mean
# data['Quantity'].fillna(data['Quantity'].mean(), inplace=True)
# data['Date'].fillna('2024-01-01', inplace=True)

# # Step 3: Calculate Total Revenue (Quantity * Price)
# data['Revenue'] = data['Quantity'] * data['Price']  # This is where you calculate the revenue

# # Calculate total revenue for all sales
# total_revenue = data['Revenue'].sum()

# # Step 4: Identify Top 3 Products by Revenue
# top_products = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(3)

# # Step 5: Show Monthly Sales Trends
# data['Date'] = pd.to_datetime(data['Date'])  # Ensure Date is in datetime format
# data['Month'] = data['Date'].dt.to_period('M')  # Extract Month
# monthly_sales = data.groupby('Month')['Revenue'].sum()

# # Output the results
# print(f"Total Revenue: ${total_revenue:.2f}")
# print("\nTop 3 Products by Revenue:")
# print(top_products)
# print("\nMonthly Sales Trends:")
# print(monthly_sales)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read cleaned data (assuming you've already cleaned and analyzed the data)
data = pd.read_csv('sales_data.csv')
data['Revenue'] = data['Quantity'] * data['Price']
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')

# Analysis (just as an example, assuming you've already done it)
monthly_sales = data.groupby('Month')['Revenue'].sum()
top_products = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(3)

# 1. Revenue Trend Over Months (Line Plot)
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='blue')  # Line plot with markers
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()

# 2. Bar Chart of Revenue by Product
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.index, y=top_products.values, palette='viridis')  # Bar plot
plt.title('Top 3 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.xticks(rotation=45)  # Rotate product names for better readability
plt.tight_layout()  # Adjust layout
plt.show()
