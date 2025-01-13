# adventureWorksDataAnalytics

## Overview

This project demonstrates data engineering concepts using the AdventureWorks dataset. It involves data ingestion, transformation, and storage using modern data engineering tools and workflows. The project is designed to showcase efficient data pipelines and best practices for handling large-scale datasets.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
- [Data Pipeline Workflow](#data-pipeline-workflow)
- [Technologies Used](#technologies-used)

## Project Structure

### Explanation of the Structure:
- **Data/**: 
  - contains original, unprocessed datasets.
- **SQL/**:
  - Holds SQL scripts for setting up the database schema, views and running queries.
- **Docs/**:
  - Includes architecture diagrams and additional project-related documentation.
- **Notebooks/**:
  - Interactive Jupyter notebooks for exploration and demonstration purposes.
- **README.md**:
  - Your project’s main documentation file.

## Features

- **Automated ETL Pipeline**:
  - End-to-end ETL pipeline for ingesting, transforming, and storing AdventureWorks data.

- **Relational Database Integration**:
  - Includes SQL scripts for creating tables, views, and running analytical queries.

- **Interactive Notebooks**:
  - Jupyter notebooks for data exploration, transformation, and pipeline visualization.

- **Best Practices**:
  - Demonstrates industry-standard workflows and tools for data engineering.

- **Architecture Documentation**:
  - Detailed documentation and diagrams illustrating pipeline workflows and architecture.

## Getting Started

### Prerequisites

Before you can run the project, make sure you have the following:

- **Azure Subscription**:
  - You need access to an Azure account with permissions to use **Azure Data Factory**, **Azure Databricks**, **Azure Synapse Analytics**, and **ADLS Gen 2**.
  
- **GitHub Account**:
  - A GitHub account to access the repository for data ingestion.

- **Power BI Account**:
  - A Power BI account for connecting to the serverless database endpoint and visualizing the data.

- **Tools**:
  - **Azure Data Factory**: To create and manage pipelines.
  - **Azure Databricks**: For data transformation using Spark.
  - **Azure Synapse Analytics**: To create a serverless database and data warehouse.
  - **Power BI Desktop**: For building reports and dashboards.

- **Original Dataset**:
    - Link: [Dataset](https://www.kaggle.com/datasets/ukveteran/adventure-works/data)

## Data Pipeline Workflow

This project follows a streamlined data pipeline workflow to ingest, transform, and store the AdventureWorks dataset, using Azure services to ensure scalability and automation.

![Data Pipeline Workflow](https://github.com/tahir007malik/adventureWorksDataAnalytics/blob/main/Docs/adventureWorksArchitecture.png)

### 1. **Data Ingestion (Bronze Directory)**
   - Data is ingested from a GitHub repository using **Azure Data Factory**.
   - A linked service is created in Data Factory to pull the data from the GitHub repository and store it in **ADLS Gen 2** in the **Bronze** directory as raw files (e.g., CSV, JSON).
   - Data Factory pipelines are responsible for orchestrating this process.

### 2. **Data Transformation (Silver Directory)**
   - The raw data stored in the **Bronze** directory is then processed using **Azure Databricks**.
   - Spark-based notebooks are used to clean, transform, and prepare the data for analysis.
   - The transformed data is stored in the **Silver** directory of **ADLS Gen 2**, which holds the more structured version of the dataset.

### 3. **Data Storage & Structuring (Gold Schema)**
   - The processed and transformed data is then loaded into **Azure Synapse Analytics** to create a **serverless database**.
   - A **Gold schema** is created within Synapse, consisting of tables like `gold.calendar`, `gold.categories`, `gold.customers`, and `gold.sales` etc.
   - These tables are organized for easy access by data analysts, optimized for querying.

### 4. **External Data Sources & Tables**
   - **External data sources** are configured in Azure Synapse for both the **Silver** and **Gold** datasets.
   - External tables like `gold.extsales` are created to allow analysts to query the transformed and structured data efficiently.

### 5. **Power BI Integration**
   - The **Gold schema** in the Synapse database is then connected to **Power BI**.
   - Power BI visualizations and dashboards are created using the Gold schema for reporting and data analysis, enabling analysts to work with ready-to-use, clean data.

### 6. **Automated Data Flow**
   - The workflow is partially automated through Azure services. 
   - **Azure Data Factory** pipelines are set to run at regular intervals using **Scheduled Triggers**, ensuring that the data pipeline is automatically triggered without manual intervention.
   - Additionally, **event-based triggers** can be configured to automatically start the pipeline when new data is available or other conditions are met.
   - For maximum automation, services like **Azure Logic Apps** or **GitHub Actions** can be integrated to initiate the pipeline in response to specific events.

## Technologies Used

This project leverages a variety of Azure services and tools to automate and manage the data pipeline, along with other technologies to ensure smooth data transformation, storage, and reporting.

- **Azure Data Factory**:
  - Used for orchestrating data movement and managing the ETL pipeline. Data is ingested from the GitHub repository and stored in ADLS Gen 2.
  
- **Azure Databricks**:
  - Provides an environment for data transformation and processing using Apache Spark. The data is cleaned and structured in Databricks before being stored in ADLS Gen 2.

- **Azure Synapse Analytics**:
  - Used for creating a **serverless database** and implementing the **Gold schema**. Synapse enables querying of transformed data using external tables and provides a scalable solution for large datasets.

- **ADLS Gen 2 (Azure Data Lake Storage)**:
  - A highly scalable storage solution for raw (Bronze) and processed (Silver) data. ADLS Gen 2 is used to store the raw and transformed datasets before and after processing.

- **Power BI**:
  - Used for connecting to the **Gold schema** in Azure Synapse Analytics to create data visualizations, reports, and dashboards. Analysts use these reports for data insights.

- **GitHub**:
  - Serves as the source for the dataset, which is pulled into the Azure Data Factory pipeline. It also acts as the version control system for project code.

- **Python & Jupyter Notebooks**:
  - Python is used in **Azure Databricks** notebooks for data transformation and processing. Jupyter notebooks are also used for data exploration and interactive analysis.

- **SQL**:
  - SQL scripts are used in **Azure Synapse Analytics** to create tables, views, and queries for managing the transformed data and creating insights for analysts.

- **Azure Logic Apps** (Optional):
  - Can be integrated for event-based triggers to automate the data pipeline based on external changes, such as new data being pushed to GitHub.

These technologies come together to form a robust, scalable, and automated data pipeline, enabling efficient data engineering workflows.