SELECT * FROM gold.categories;

SELECT * FROM gold.extsales;

SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://`your-storage-account`.dfs.core.windows.net/silver/adventure_works_calendar/',
        FORMAT = 'PARQUET'
    ) AS query1