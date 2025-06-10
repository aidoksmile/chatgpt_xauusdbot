import yfinance as yf

def fetch_data(ticker, interval='1d', period='1y'):
    try:
        data = yf.download('GC=F', interval='1d', period='1y')
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
