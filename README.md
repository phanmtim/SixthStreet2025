# SixthStreet2025

A Python library for fetching and processing stock quotes from the Alpha Vantage API using the TIME_SERIES_DAILY endpoint.

## Overview

SixthStreet2025 provides simple functionality for:
- **lookup(symbol, date):** Retrieve the open, high, low, close, and volume for a given stock symbol on a specific date.
- **min(symbol, n):** Determine the lowest price (low) over the last `n` trading days for a given stock symbol.
- **max(symbol, n):** Determine the highest price (high) over the last `n` trading days for a given stock symbol.

This library leverages the [Alpha Vantage API](https://www.alphavantage.co/documentation/#daily) to fetch historical daily stock data. A free API key is required to use the API.

## Project Structure

```
SixthStreet2025/ 
├── alphavantage_client.py # Main library module with API interaction and utility functions 
├── example.py # Example usage of the library 
├── README.md # Project documentation (this file) 
├── setup.py # Setup script for installation 
└── DISCUSSION.md # Detailed discussion of design decisions and implementation notes
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/SixthStreet2025.git
   cd SixthStreet2025

2. **Install Packages**
   ```bash
   pip install .