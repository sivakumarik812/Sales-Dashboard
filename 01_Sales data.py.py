import pandas as pd
import numpy as np

# Seed for reproducible results
np.random.seed(101)

n_rows = 1000

categories = {
    'Electronics': [('Laptop', 55000), ('Smartphone', 25000), ('Headphones', 3000)],
    'Furniture': [('Office Chair', 7500), ('Study Table', 12000), ('Bookshelf', 5000)],
    'Clothing': [('Jacket', 3500), ('Jeans', 2000), ('T-Shirt', 800)]
}

regions = ['South', 'North', 'East', 'West']
payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Net Banking']

data = []
for i in range(1, n_rows + 1):
    cat = np.random.choice(list(categories.keys()))
    prod, price = categories[cat][np.random.randint(0, len(categories[cat]))]
    qty = np.random.randint(1, 5)
    region = np.random.choice(regions)
    pay = np.random.choice(payment_methods)
    
    data.append({
        'OrderID': 2000 + i,
        'OrderDate': pd.date_range('2025-01-01', '2025-12-31', periods=n_rows)[i-1].strftime('%Y-%m-%d'),
        'Category': cat,
        'Product': prod,
        'UnitPrice': price,
        'Quantity': qty,
        'TotalSales': price * qty,
        'Region': region,
        'PaymentMethod': pay
    })

df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("Sales dataset generated successfully!")
