-- CREATING VIEW CALENDER --
CREATE VIEW gold.calender
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_calendar/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW CATEGORIES --
CREATE VIEW gold.categories
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_categories/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW CUSTOMERS --
CREATE VIEW gold.customers
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_customers/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW PRODUCTS --
CREATE VIEW gold.products
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_products/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW RETURNS --
CREATE VIEW gold.returns
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_returns/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW SALES --
CREATE VIEW gold.sales
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_sales/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW SUBCATEGORIES --
CREATE VIEW gold.subcategories
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_subcategories/',
        FORMAT = 'PARQUET'
    ) AS query1

-- CREATING VIEW TERRITORIES --
CREATE VIEW gold.territories
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_territories/',
        FORMAT = 'PARQUET'
    ) AS query1
