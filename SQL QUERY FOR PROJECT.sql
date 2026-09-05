create database ECommerceAnalytics
use ECommerceAnalytics

SELECT COUNT(*) AS TotalRows
FROM online_retail;

SELECT
    COUNT(*) AS TotalRows,
    COUNT(TotalAmount) AS TotalAmountRows
FROM online_retail;

SELECT 
    SUM(TotalAmount) AS TotalRevenue
FROM online_retail;

SELECT 
    SUM(Quantity) AS TotalQuantitySold
FROM online_retail;

SELECT 
    COUNT(DISTINCT CustomerID) AS NumberOfCustomers
FROM online_retail;

SELECT 
    COUNT(DISTINCT StockCode) AS NumberOfProducts
FROM online_retail;

SELECT TOP 10
    StockCode,
    Description,
    SUM(TotalAmount) AS Revenue
FROM online_retail
GROUP BY StockCode, Description
ORDER BY Revenue DESC;

SELECT TOP 10
    Country,
    SUM(TotalAmount) AS Revenue
FROM online_retail
GROUP BY Country
ORDER BY Revenue DESC;

SELECT 
    YEAR(InvoiceDate) AS Year,
    MONTH(InvoiceDate) AS Month,
    SUM(TotalAmount) AS Revenue
FROM online_retail
GROUP BY 
    YEAR(InvoiceDate),
    MONTH(InvoiceDate)
ORDER BY 
    Year,
    Month;

SELECT 
    SUM(TotalAmount) / COUNT(DISTINCT InvoiceNo) AS AverageOrderValue
FROM online_retail;

SELECT TOP 10
    CustomerID,
    SUM(TotalAmount) AS TotalRevenue
FROM online_retail
GROUP BY CustomerID
ORDER BY TotalRevenue DESC;

SELECT TOP 10
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS NumberOfOrders
FROM online_retail
GROUP BY CustomerID
ORDER BY NumberOfOrders DESC

SELECT
    CASE
        WHEN COUNT(DISTINCT InvoiceNo) = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END AS CustomerType,
    COUNT(*) AS NumberOfCustomers
FROM online_retail
GROUP BY CustomerID

WITH CustomerOrders AS (
    SELECT
        CustomerID,
        COUNT(DISTINCT InvoiceNo) AS OrderCount
    FROM online_retail
    GROUP BY CustomerID
)
SELECT
    CASE
        WHEN OrderCount = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END AS CustomerType,
    COUNT(*) AS NumberOfCustomers

SELECT TOP 10
    StockCode,
    Description,
    SUM(Quantity) AS TotalQuantitySold
FROM online_retail
GROUP BY StockCode, Description
ORDER BY TotalQuantitySold DESC;

SELECT TOP 10
    Country,
    COUNT(DISTINCT InvoiceNo) AS NumberOfOrders,
    SUM(TotalAmount) AS Revenue,
    AVG(TotalAmount) AS AverageOrderValue
FROM online_retail
GROUP BY Country
ORDER BY Revenue DESC;
FROM CustomerOrders
GROUP BY
    CASE
        WHEN OrderCount = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END;