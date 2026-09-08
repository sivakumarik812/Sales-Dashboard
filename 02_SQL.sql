-- 1. Overall Sales Performance Summary
SELECT 
    COUNT(DISTINCT OrderID) AS Total_Orders,
    SUM(Quantity) AS Total_Units_Sold,
    SUM(TotalSales) AS Total_Revenue,
    ROUND(AVG(TotalSales), 2) AS Average_Order_Value
FROM sales_data;

-- 2. Category-wise Sales Breakdown
SELECT 
    Category,
    SUM(Quantity) AS Total_Quantity,
    SUM(TotalSales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 3. Region-wise Revenue Analysis
SELECT 
    Region,
    COUNT(OrderID) AS Order_Count,
    SUM(TotalSales) AS Regional_Revenue
FROM sales_data
GROUP BY Region
ORDER BY Regional_Revenue DESC;

-- 4. Payment Method Distribution
SELECT 
    PaymentMethod,
    COUNT(OrderID) AS Transactions,
    SUM(TotalSales) AS Amount_Processed
FROM sales_data
GROUP BY PaymentMethod
ORDER BY Amount_Processed DESC;
