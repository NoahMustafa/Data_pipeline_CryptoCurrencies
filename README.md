# 📊 Real-Time Cryptocurrency Data Pipeline

<div align="center">

![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![DBT](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge&logo=python&logoColor=white)

*End-to-end data pipeline for real-time cryptocurrency market intelligence*

</div>

---

## 📌 Project Overview

This project implements an **end-to-end data pipeline** for **real-time cryptocurrency data**. It scrapes cryptocurrency market data every **15 minutes**, processes and loads it into **PostgreSQL**, transforms it with **DBT**, and visualizes trends in **Power BI** dashboards.

---

## 🏗️ Architecture

<div align="center">

![Architecture Workflow](https://github.com/user-attachments/assets/5c3637a7-fcb4-4603-b47a-acee966e6451)

</div>

---

## ⚡ Pipeline Flow

### 1. **Web Scraping** (Python + BeautifulSoup)
- Scrapes `title`, `prefix`, `price`, `24h change`, `volume`, `market cap`
- Runs every **15 minutes**
- Cleans values (`$`, `%`, `M`, `B`) → numeric format

### 2. **Data Storage** (PostgreSQL)
- `crypto_currencies` → latest snapshot
- `crypto_currencies_old` → previous snapshot  
- Ensures **historical tracking** of prices

### 3. **Transformations** (DBT)
- Combines `crypto_currencies` + `crypto_currencies_old`
- Produces a **view** with:
  - Current Price
  - Maximum Price
  - Minimum Price
  - Market Cap, Volume, 24h Change

### 4. **Visualization** (Power BI)
- Connects to DBT view
- Dashboards include:
  - Current market snapshot
  - Historical price highs/lows
  - Trends over time

---

## 🚀 How to Run on Local Machine

### Prerequisites
- Docker installed with proper configurations
- PostgreSQL database setup

### Setup Instructions
1. **Database Setup**: Create PostgreSQL database using `create_schema.sql` file
2. **Docker Configuration**: Ensure all files and folders are mounted in Docker with correct configs
3. **AI Assistant**: Share the `DAG.py` file with any AI for detailed instructions
4. **Testing Only**: To test scraping mechanism only, run the `Scrape.py` script

---

## 📊 Power BI Dashboard

<div align="center">

### Dashboard Features
- **Snapshot View** → Current market prices, volumes, caps
- **Trend Analysis** → Min/max price tracking across time

<img width="1278" height="719" alt="Cryptocurrency Dashboard" src="https://github.com/user-attachments/assets/36467a2a-52d0-481a-b12f-f1742c802680" />

</div>

---

## 🎥 Project Demo

<div align="center">

[![Watch the Demo Video](https://img.youtube.com/vi/sbFoUVz6ZZ8/0.jpg)](https://youtu.be/sbFoUVz6ZZ8)

*Click to watch the complete project walkthrough*

</div>

---

## 📈 Project Outcomes

<div align="center">

| Achievement | Description |
|-------------|-------------|
| **🔄 Automated Pipeline** | Built end-to-end automated data processing system |
| **⏰ Real-time Monitoring** | Enables continuous cryptocurrency market tracking |
| **📚 Historical Data** | Preserves complete price history for trend analysis |
| **📊 Business Intelligence** | Provides insightful dashboards for decision-making |

</div>

---

<div align="center">

**Built with modern data engineering practices for cryptocurrency market intelligence**

</div>
