/*
E-Commerce Sales Analysis
Author: Sinem Azaklý

This file contains the core SQL queries
used for analysis and Power BI dashboard.
*/
--Toplam Ciro – Toplam Satýþ Adedi
SELECT
    SUM(Quantity) AS Total_Quantity,
    SUM([Total Price]) AS Total_Revenue
FROM orders;
--Ülkeye Göre Toplam Satýþ (Quantity)
SELECT
    Country,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Country
ORDER BY Total_Quantity DESC;

--Ülkeye Göre Toplam Ciro
SELECT
    Country,
    SUM([Total Price]) AS Total_Revenue
FROM orders
GROUP BY Country
ORDER BY Total_Revenue DESC;

--Customer Type (Guest / Registered)
SELECT
    CASE
        WHEN CustomerID IS NULL THEN 'Guest'
        ELSE 'Registered'
    END AS CustomerType,
    SUM([Total Price]) AS Total_Revenue,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY
    CASE
        WHEN CustomerID IS NULL THEN 'Guest'
        ELSE 'Registered'
    END;

--Yýla Göre Toplam Satýþ
SELECT
    Year,
    SUM([Total Price]) AS Total_Revenue,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Year
ORDER BY Year;

--Top 10 Ürün – Ciroya Göre
SELECT TOP 10
    Description,
    SUM([Total Price]) AS Total_Revenue
FROM orders
GROUP BY Description
ORDER BY Total_Revenue DESC;



