import pandas as pd 

df=pd.read_excel("online+retail/online retail.xlsx")

print(df.head())
print("dataset shape:",df.shape)
print(df.columns)
print(df.isnull().sum())
print("duplicate rows:",df.duplicated().sum())
df=df.drop_duplicates()
print("New dataset shape:",df.shape)
df = df.dropna(subset=['CustomerID'])
print("After removing missing CustomerID:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("New dataset shape:", df.shape)
df = df.dropna(subset=['CustomerID'])
print("After removing missing CustomerID:", df.shape)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("\nInvoiceDate datatype:")
print(df['InvoiceDate'].dtype)
print("\nDate range:")
print(df['InvoiceDate'].min())
print(df['InvoiceDate'].max())
print("Negative Quantity:", (df["Quantity"] < 0).sum())
print("Zero Quantity:", (df["Quantity"] == 0).sum())
print("Negative UnitPrice:", (df["UnitPrice"] < 0).sum())
print("Zero UnitPrice:", (df["UnitPrice"] == 0).sum())
print("Negative Quantity:", (df["Quantity"] < 0).sum())
print("Zero Quantity:", (df["Quantity"] == 0).sum())
print("Negative UnitPrice:", (df["UnitPrice"] < 0).sum())
print("Zero UnitPrice:", (df["UnitPrice"] == 0).sum())
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
print("After removing invalid transactions:", df.shape)
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
print("\nTotalAmount:")
print(df[['Quantity', 'UnitPrice', 'TotalAmount']].head())
print("\nTotalAmount statistics:")
print(df['TotalAmount'].describe())
cancelled = df['InvoiceNo'].astype(str).str.startswith('C')
print("\nCancelled transactions:", cancelled.sum())
print("Normal transactions:", (~cancelled).sum())
print("\nFinal dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nTotal Revenue:", df['TotalAmount'].sum())
print("Total Quantity Sold:", df['Quantity'].sum())
print("Number of Transactions:", df['InvoiceNo'].nunique())
print("Number of Customers:", df['CustomerID'].nunique())
print("Number of Products:", df['StockCode'].nunique())
top_products = (
    df.groupby('Description')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)
country_revenue = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False)
print("\nTop 10 Countries by Revenue:")
print(country_revenue.head(10))
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['TotalAmount'].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)
total_revenue = df['TotalAmount'].sum()
total_transactions = df['InvoiceNo'].nunique()
aov = total_revenue / total_transactions
print("\nAverage Order Value (AOV):", aov)
top_customers = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue:")
print(top_customers)
top_products = (
    df.groupby('Description')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)
customer_orders = (
    df.groupby('CustomerID')['InvoiceNo']
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Number of Orders:")
print(customer_orders)
customer_avg_spending = (
    df.groupby('CustomerID')['TotalAmount']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Average Spending:")
print(customer_avg_spending)
orders_per_customer = df.groupby('CustomerID')['InvoiceNo'].nunique()

one_time_customers = (orders_per_customer == 1).sum()
repeat_customers = (orders_per_customer > 1).sum()

print("\nCustomer Purchase Behavior:")
print("One-time customers:", one_time_customers)
print("Repeat customers:", repeat_customers)

import matplotlib.pyplot as plt

monthly_revenue = df.groupby(
    df['InvoiceDate'].dt.to_period('M')
)['TotalAmount'].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)


plt.figure(figsize=(12, 6))
monthly_revenue.plot(kind='line', marker='o')

plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

top_products = df.groupby('Description')['TotalAmount'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Revenue:")
print(top_products)


plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind='barh')

plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Product')

plt.tight_layout()
plt.show()
print("\nNegative/Zero Quantity:")
print(df[df["Quantity"] <= 0][["Quantity", "UnitPrice"]].head())
print("Count:", (df["Quantity"] <= 0).sum())

print("\nNegative/Zero UnitPrice:")
print(df[df["UnitPrice"] <= 0][["Quantity", "UnitPrice"]].head())
print("Count:", (df["UnitPrice"] <= 0).sum())
print("Negative/Zero UnitPrice Count:", (df["UnitPrice"] <= 0).sum())
top_products_quantity = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Quantity Sold:")
print(top_products_quantity)
country_revenue = (
    df.groupby('Country')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
country_revenue.head(10).sort_values().plot(kind='barh')

plt.title('Top 10 Countries by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
customer_revenue = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
customer_revenue.sort_values().plot(kind='barh')

plt.title('Top 10 Customers by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Customer ID')
plt.tight_layout()
plt.show()
customer_type = {
    'One-time Customers': one_time_customers,
    'Repeat Customers': repeat_customers
}

plt.figure(figsize=(8, 6))
plt.bar(customer_type.keys(), customer_type.values())

plt.title('One-time vs Repeat Customers')
plt.xlabel('Customer Type')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()
top_products_quantity = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products_quantity.sort_values().plot(kind='barh')

plt.title('Top 10 Products by Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.tight_layout()
plt.show()
monthly_aov = (
    df.groupby(df['InvoiceDate'].dt.to_period('M'))
      .apply(lambda x: x['TotalAmount'].sum() / x['InvoiceNo'].nunique())
)

plt.figure(figsize=(12, 6))
monthly_aov.plot(kind='line', marker='o')

plt.title('Monthly Average Order Value')
plt.xlabel('Month')
plt.ylabel('Average Order Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

recency = (
    df.groupby('CustomerID')['InvoiceDate']
    .max()
    .apply(lambda x: (reference_date - x).days)
)

print("\nCustomer Recency:")
print(recency.head(10))
frequency = (
    df.groupby('CustomerID')['InvoiceNo']
    .nunique()
)

print("\nCustomer Frequency:")
print(frequency.head(10))
monetary = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
)

print("\nCustomer Monetary Value:")
print(monetary.head(10))
rfm = pd.concat(
    [recency, frequency, monetary],
    axis=1
)

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM Customer Table:")
print(rfm.head(10))
rfm['R_Score'] = pd.qcut(
    rfm['Recency'],
    5,
    labels=[5, 4, 3, 2, 1]
)

rfm['F_Score'] = pd.qcut(
    rfm['Frequency'].rank(method='first'),
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm['M_Score'] = pd.qcut(
    rfm['Monetary'].rank(method='first'),
    5,
    labels=[1, 2, 3, 4, 5]
)

print("\nRFM Scores:")
print(rfm.head(10))
rfm['RFM_Score'] = (
    rfm['R_Score'].astype(int) +
    rfm['F_Score'].astype(int) +
    rfm['M_Score'].astype(int)
)

print("\nFinal RFM Scores:")
print(rfm.head(10))
def customer_segment(score):
    if score >= 13:
        return 'Champions'
    elif score >= 10:
        return 'Loyal Customers'
    elif score >= 7:
        return 'Potential Customers'
    elif score >= 5:
        return 'At Risk'
    else:
        return 'Lost Customers'

rfm['Segment'] = rfm['RFM_Score'].apply(customer_segment)

print("\nCustomer Segments:")
print(rfm[['R_Score', 'F_Score', 'M_Score', 'RFM_Score', 'Segment']].head(10))

segment_counts = rfm['Segment'].value_counts()

print("\nCustomer Segment Counts:")
print(segment_counts)
plt.figure(figsize=(10, 6))

segment_counts.plot(kind='bar')

plt.title('Customer Segments')
plt.xlabel('Customer Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
segment_revenue = (
    rfm.groupby('Segment')['Monetary']
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Customer Segment:")
print(segment_revenue)

segment_customer_count = (
    rfm.groupby('Segment')['RFM_Score']
    .count()
    .sort_values(ascending=False)
)

print("\nNumber of Customers by Segment:")
print(segment_customer_count)
segment_analysis = (
    rfm.groupby('Segment')[['Recency', 'Frequency', 'Monetary']]
    .mean()
    .round(2)
)

print("\nAverage RFM Metrics by Customer Segment:")
print(segment_analysis)
highest_value_segment = (
    segment_analysis['Monetary']
    .sort_values(ascending=False)
)

print("\nCustomer Segments by Average Spending:")
print(highest_value_segment)
plt.figure(figsize=(10, 6))

segment_revenue.sort_values().plot(kind='barh')

plt.title('Revenue by Customer Segment')
plt.xlabel('Revenue')
plt.ylabel('Customer Segment')
plt.tight_layout()
plt.show()

high_value_customers = (
    rfm[['Monetary', 'Segment']]
    .sort_values('Monetary', ascending=False)
    .head(10)
)

print("\nTop 10 High-Value Customers:")
print(high_value_customers)

at_risk_customers = (
    rfm[rfm['Segment'] == 'At Risk']
    .sort_values('Monetary', ascending=False)
)

print("\nTop At-Risk Customers:")
print(at_risk_customers.head(10))
top_10_revenue = high_value_customers['Monetary'].sum()
total_customer_revenue = rfm['Monetary'].sum()

revenue_contribution = (
    top_10_revenue / total_customer_revenue
) * 100

print("\nTop 10 Customers Revenue Contribution:")
print(f"Revenue: {top_10_revenue:.2f}")
print(f"Percentage of Total Revenue: {revenue_contribution:.2f}%")
segment_revenue_percentage = (
    segment_revenue / segment_revenue.sum() * 100
)

print("\nRevenue Contribution by Customer Segment:")
print(segment_revenue_percentage.round(2))

plt.figure(figsize=(10, 6))

segment_revenue_percentage.sort_values().plot(kind='barh')

plt.title('Revenue Contribution by Customer Segment')
plt.xlabel('Revenue Contribution (%)')
plt.ylabel('Customer Segment')
plt.tight_layout()
plt.show()
best_segment = segment_revenue.idxmax()
best_segment_revenue = segment_revenue.max()

print("\nBest Customer Segment by Revenue:")
print(f"Segment: {best_segment}")
print(f"Revenue: {best_segment_revenue:.2f}")
best_products = (
    df.groupby('Description')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Best-Performing Products:")
print(best_products)
worst_products = (
    df.groupby('Description')['TotalAmount']
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print("\nBottom 10 Products by Revenue:")
print(worst_products)
best_countries = (
    df.groupby('Country')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries by Revenue:")
print(best_countries)
monthly_sales = (
    df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalAmount']
    .sum()
    .sort_values(ascending=False)
)

best_month = monthly_sales.idxmax()
best_month_revenue = monthly_sales.max()

worst_month = monthly_sales.idxmin()
worst_month_revenue = monthly_sales.min()

print("\nBest Sales Month:")
print(f"Month: {best_month}")
print(f"Revenue: {best_month_revenue:.2f}")

print("\nLowest Sales Month:")
print(f"Month: {worst_month}")
print(f"Revenue: {worst_month_revenue:.2f}")
total_customers = one_time_customers + repeat_customers

repeat_customer_percentage = (
    repeat_customers / total_customers
) * 100

print("\nRepeat Customer Analysis:")
print(f"Total Customers: {total_customers}")
print(f"Repeat Customers: {repeat_customers}")
print(f"One-time Customers: {one_time_customers}")
print(f"Repeat Customer Percentage: {repeat_customer_percentage:.2f}%")
df.to_csv('cleaned_online_retail.csv', index=False)

print("\nCleaned dataset exported successfully!")