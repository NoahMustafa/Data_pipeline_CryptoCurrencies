CREATE SCHEMA IF NOT EXISTS currencies;

CREATE TABLE IF NOT EXISTS currencies.crypto_currencies (
    title TEXT,
    prefix TEXT,
    prices NUMERIC,
    change_24 NUMERIC,
    volume_24 NUMERIC,
    market_cap NUMERIC,
    time_scraped TIMESTAMP
);

CREATE TABLE IF NOT EXISTS currencies.crypto_currencies_old (
    title TEXT,
    prefix TEXT,
    prices NUMERIC,
    change_24 NUMERIC,
    volume_24 NUMERIC,
    market_cap NUMERIC,
    time_scraped TIMESTAMP
);
