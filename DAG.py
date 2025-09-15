import re
from sched import scheduler
from datetime import datetime, timedelta
from requests.models import default_hooks
from sqlalchemy import create_engine, engine, false, schema, text
import psycopg2 as sy
from airflow import DAG
from psycopg2.extras import execute_values
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago
from numpy import append
import requests as rs
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.sql import elements
import pandas as pd
import os


def ingest_and_load(**kwarg):
    engine = create_engine(
        "your_database_connection"
    )
    page = 1
    prices = []
    title = []
    prefix = []
    change_24 = []
    volume_24 = []
    market_cap = []
    output_dir = "/opt/airflow/output"
    os.makedirs(output_dir, exist_ok=True)
    path = "D:\data_eng\Data_Pipelines\V1\data.csv"
    for page in range(1, 5):

        url = f"https://crypto.com/price?page={page}"
        print(f"scraping page {page}")

        response = rs.get(url)

        if response.status_code == 200:
            rows = BeautifulSoup(response.text, "html.parser").find_all(
                "tr", class_="css-1cxc880"
            )
            for r in rows:
                title.append(r.find(class_="chakra-text css-rkws3").text)
                prices.append(r.find(class_="css-b1ilzc").text)
                change_24.append(r.find(class_="css-vtw5vj").text)
                prefix.append(r.find(class_="chakra-text css-1jj7b1a").text)

                tds = r.find_all(class_="css-15lyn3l")
                cap = tds[1].text
                vol = tds[0].text
                volume_24.append(vol)
                market_cap.append(cap)

        else:
            print("error")
    print(volume_24)

    data = pd.DataFrame(
        {
            "title": title,
            "prefix": prefix,
            "prices": prices,
            "change_24": change_24,
            "volume_24": volume_24,
            "market_cap": market_cap,
            "time_scraped": datetime.now(),
        }
    )

    print(data.head(10))

    def parse_money(s):
        try:
            if not s or s == "N/A":
                return None

            s = s.replace("$", "").replace(",", "").replace("%", "").strip()

            if "M" in s:
                return pd.to_numeric(s.replace("M", "").strip()) * 10**6
            elif "B" in s:
                return pd.to_numeric(s.replace("B", "").strip()) * 10**9
            else:
                return pd.to_numeric(s)
        except Exception as e:
            print(f"Error parsing {s}: {e}")
            return None

    data["prices"] = data["prices"].apply(parse_money)
    data["change_24"] = data["change_24"].apply(parse_money)
    data["volume_24"] = data["volume_24"].apply(parse_money)
    data["market_cap"] = data["market_cap"].apply(parse_money)
    data.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    with engine.begin() as conn:
        conn.execute(
            text(
                """
            DROP VIEW IF EXISTS currencies.newview;
            INSERT INTO currencies.crypto_currencies_old (
            title, prefix, prices, change_24, volume_24, market_cap, time_scraped
        )
        SELECT 
            title, prefix, prices, change_24, volume_24, market_cap, time_scraped
        FROM currencies.crypto_currencies;

        """
            )
        )
        conn.execute(
            text(
                """
        truncate table currencies.crypto_currencies
        
        """
            )
        )
        for col in ["prices", "change_24", "volume_24", "market_cap"]:
            data[col] = pd.to_numeric(data[col], errors="coerce")

        data.to_sql(
            "crypto_currencies",
            conn,
            schema="currencies",
            if_exists="append",
            index=False,
        )
    return path


with DAG(
    dag_id="noah_ver_pipeline",
    default_args={"owner": "noah", "retries": 1},
    start_date=days_ago(1),
    catchup=False,
    schedule_interval=timedelta(minutes=15),
) as dag:
    ingesting = PythonOperator(
        task_id="ingesting",
        python_callable=ingest_and_load,
    )

    transform = BashOperator(
        task_id="transform_in_dbt",
        bash_command=r"""
        cd /opt/dbt_projects/noah
        dbt run --profiles-dir /opt/airflow/.dbt -s version1
        """
    )

    ingesting >> transform
