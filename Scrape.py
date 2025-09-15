import requests as rs
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_crypto_pages(pages=2):
    prices, title, prefix, change_24, volume_24, market_cap = [], [], [], [], [], []

    for page in range(1, 3):
        url = f"https://crypto.com/price?page={page}"
        print(f"Scraping {url}")
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
                cap, vol = tds[1].text, tds[0].text
                volume_24.append(vol)
                market_cap.append(cap)
        else:
            print(f"Error fetching {url}")

    df = pd.DataFrame({
        "title": title,
        "prefix": prefix,
        "prices": prices,
        "change_24": change_24,
        "volume_24": volume_24,
        "market_cap": market_cap,
        "time_scraped": datetime.now()
    })

    return df

if __name__ == "__main__":
    data = scrape_crypto_pages(2)
    print(data.head())
    data.to_csv("crypto_data_sample.csv", index=False)
    print("Data saved to crypto_data_sample.csv")
