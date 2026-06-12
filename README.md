Gun Violence Data Warehouse & OLAP Analysis (US 2013–2018)

📌 Project Overview

This project builds a full data warehouse system and OLAP solution using a multi-format dataset (CSV, XML, JSON) of US gun violence incidents (2013–2018). The goal is to design an analytical system for exploring crime patterns across geography, time, and participant attributes.

🏗️ Data Engineering & ETL
Integrated multiple data formats (CSV, XML, JSON)
Cleaned and transformed raw datasets using ETL pipelines (SSIS)
Engineered new features such as:
Quarter (Q1–Q4)
Crime Gravity (severity metric combining incident factors)
Enriched geographic data using city/state coordinates
Generated surrogate keys for dimensional modeling

🗄️ Data Warehouse Design

Built a Star Schema architecture:

Fact Table: Custody
Dimension Tables: Participant, Gun, Geography, Date, Incident

📊 OLAP & Analytical Modeling
Created OLAP cube with Time and Geography hierarchies
Developed MDX queries to answer:
- High-risk cities per state
- Incident severity vs state average
- Quarterly crime gravity trends

📈 Dashboards (Power BI)
- Geographic heatmaps of crime severity
- Age group distribution of participants
- Time-based trend analysis (year, month, quarter)
- KPI tracking for custody counts and crime gravity

🎯 Key Insights
Handguns were the most dominant weapon type across states
Certain cities showed significantly higher crime gravity than state averages
Crime patterns varied strongly by geography and time

🛠️ Tools & Technologies
* SSIS (ETL pipelines)
* SQL Server (Data Warehouse)
* MDX (OLAP analysis)
* Power BI (Dashboarding)
* Python / Data preprocessing
