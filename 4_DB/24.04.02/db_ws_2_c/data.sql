

-- 1.
SELECT BillingCountry, SUM(Total) FROM invoices GROUP BY BillingCountry;

-- 2.
-- strftime funciton (format, datetime column)
SELECT strftime('%Y', InvoiceDate) AS YEAR, SUM(Total) AS TotalSales FROM invoices GROUP BY YEAR;

-- 3.
SELECT BillingState, SUM(Total) AS TotalSales
FROM (SELECT * FROM invoices
WHERE BillingCountry == 'USA' AND InvoiceDate > '2010-01-01')
GROUP BY BillingState;

-- 4.
SELECT BillingCountry, MAX(Total) AS MaxOrderAmount
FROM (SELECT * FROM invoices
WHERE BillingCountry == 'Germany' OR BillingCountry == 'France')
GROUP BY BillingCountry;
