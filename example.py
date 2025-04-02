from alphavantage_client import AlphaVantageClient

def main():
    api_key = "93ZUW8JTV8Z6Q9VW"
    client = AlphaVantageClient(api_key)
    
    symbol = "IBM"
    date = "2024-11-06"  

    try:
        quote = client.lookup(symbol, date)
        print(f"Quote for {symbol} on {date}:")
        print(f"  Open:   {quote['open']}")
        print(f"  High:   {quote['high']}")
        print(f"  Low:    {quote['low']}")
        print(f"  Close:  {quote['close']}")
        print(f"  Volume: {quote['volume']}")
    except Exception as e:
        print("Error during lookup:", e)

    try:
        n = 5
        lowest = client.min(symbol, n)
        highest = client.max(symbol, n)
        print(f"\nOver the last {n} trading days for {symbol}:")
        print(f"  Lowest Low: {lowest}")
        print(f"  Highest High: {highest}")
    except Exception as e:
        print("Error during min/max computation:", e)

if __name__ == "__main__":
    main()
