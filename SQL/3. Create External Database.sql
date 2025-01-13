CREATE DATABASE SCOPED CREDENTIAL cred_tahir
WITH
    IDENTITY = 'Managed Identity'

CREATE EXTERNAL DATA SOURCE source_silver
WITH
(
    LOCATION = 'https://`your-storage-account`.dfs.core.windows.net/silver',
    CREDENTIAL = cred_tahir
)

CREATE EXTERNAL DATA SOURCE source_gold
WITH
(
    LOCATION = 'https://`your-storage-account`.dfs.core.windows.net/gold',
    CREDENTIAL = cred_tahir
)

CREATE EXTERNAL FILE FORMAT format_parquet
WITH
(
    FORMAT_TYPE = PARQUET
)

-- CREATE EXTERNAL TABLE EXTSALES --
CREATE EXTERNAL TABLE gold.extsales
WITH
(
    LOCATION = 'extsales',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = format_parquet
)
AS
SELECT * FROM gold.sales






























