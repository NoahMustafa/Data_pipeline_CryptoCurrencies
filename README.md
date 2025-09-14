Real-Time Cryptocurrency Data Pipeline
![Airflow](https://img.shields.io/badge/Airflow-DAG-blue?logo=apache-airflow)  
![DBT](https://img.shields.io/badge/DBT-Data%20Modeling-orange?logo=dbt)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)  
![Python](https://img.shields.io/badge/Python-Scraping-green?logo=python)  
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=powerbi)  

---

## 📌 Overview
This project implements an **end-to-end data pipeline** for **real-time cryptocurrency data**.  
It scrapes cryptocurrency market data every **15 minutes**, processes and loads it into **PostgreSQL**, transforms it with **DBT**, and visualizes trends in **Power BI** dashboards.  


⚙️ Architecture

![workflow](https://github.com/user-attachments/assets/5c3637a7-fcb4-4603-b47a-acee966e6451)



## ⚡ Pipeline Flow

1. **Web Scraping (Python + BeautifulSoup)**
   - Scrapes `title`, `prefix`, `price`, `24h change`, `volume`, `market cap`.
   - Runs every **15 minutes**.
   - Cleans values (`$`, `%`, `M`, `B`) → numeric format.

2. **Data Storage (PostgreSQL)**
   - `crypto_currencies` → latest snapshot.
   - `crypto_currencies_old` → previous snapshot.
   - Ensures **historical tracking** of prices.

3. **Transformations (DBT)**
   - Combines `crypto_currencies` + `crypto_currencies_old`.
   - Produces a **view** with:
     - Current Price
     - Maximum Price
     - Minimum Price
     - Market Cap, Volume, 24h Change

4. **Visualization (Power BI)**
   - Connects to DBT view.
   - Dashboards include:
     - Current market snapshot
     - Historical price highs/lows
     - Trends over time



##   Power BI Dashboard

Snapshot View → current market prices, volumes, caps.

Trend Analysis → min/max price tracking across time.

Performance Comparison → currency-by-currency historical shifts.

<img width="1278" height="719" alt="first project dashboard" src="https://github.com/user-attachments/assets/36467a2a-52d0-481a-b12f-f1742c802680" />


📈 Outcome

Built an end-to-end automated pipeline.

Enables real-time crypto monitoring.

Preserves historical data for trend analysis.

Provides insightful dashboards for decision-making.
