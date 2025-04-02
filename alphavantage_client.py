import requests

class AlphaVantageClient:
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key):
        """
        Initializes the client with an API key.
        A simple cache is used to reduce duplicate network calls.
        """
        self.api_key = api_key
        self.cache = {}

    def fetch_daily_series(self, symbol):
        """
        Fetches daily time series data for the given symbol.
        Caches the result to avoid multiple API calls.
        """
        if symbol in self.cache:
            return self.cache[symbol]

        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        if "Time Series (Daily)" not in data:
            raise Exception(f"Error fetching data for symbol {symbol}: {data}")
        timeseries = data["Time Series (Daily)"]
        self.cache[symbol] = timeseries
        return timeseries

    def lookup(self, symbol, date):
        """
        Returns the open, high, low, close, and volume for the given symbol on a specified date.
        Date should be in 'YYYY-MM-DD' format.
        """
        timeseries = self.fetch_daily_series(symbol)
        if date not in timeseries:
            raise Exception(f"Date {date} not found for symbol {symbol}")
        record = timeseries[date]
        return {
            "open": float(record["1. open"]),
            "high": float(record["2. high"]),
            "low": float(record["3. low"]),
            "close": float(record["4. close"]),
            "volume": int(record["5. volume"])
        }

    def min(self, symbol, n):
        """
        Returns the lowest low in the last 'n' data points for the given symbol.
        """
        timeseries = self.fetch_daily_series(symbol)
        sorted_dates = sorted(timeseries.keys(), reverse=True)
        if len(sorted_dates) < n:
            raise Exception(f"Not enough data points for symbol {symbol}. Requested {n}, available {len(sorted_dates)}.")
        recent_dates = sorted_dates[:n]
        lows = [float(timeseries[date]["3. low"]) for date in recent_dates]
        return min(lows)

    def max(self, symbol, n):
        """
        Returns the highest high in the last 'n' data points for the given symbol.
        """
        timeseries = self.fetch_daily_series(symbol)
        sorted_dates = sorted(timeseries.keys(), reverse=True)
        if len(sorted_dates) < n:
            raise Exception(f"Not enough data points for symbol {symbol}. Requested {n}, available {len(sorted_dates)}.")
        recent_dates = sorted_dates[:n]
        highs = [float(timeseries[date]["2. high"]) for date in recent_dates]
        return max(highs)