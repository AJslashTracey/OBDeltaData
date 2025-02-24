def api_call_OB():
    conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'  # Example User-Agent
    }

    product_id = "BTC-USD"
    endpoint = f"/products/{product_id}/book?level=2"  # Adjust the level if needed

    conn.request("GET", endpoint, payload, headers)
    res = conn.getresponse()
    data = res.read()

    # Check for errors
    if res.status != 200:
        raise Exception(f"API call failed with status {res.status}: {data}")

    return data
def get_orderbook_delta():
    order_book_data = api_call_OB()
    order_book = json.loads(order_book_data.decode("utf-8"))

    bids = order_book["bids"]
    asks = order_book["asks"]

    highest_bid = float(bids[0][0])
    lowest_ask = float(asks[0][0])

    bid_threshold = highest_bid * 0.95
    ask_threshold = lowest_ask * 1.05

    topBids = [bid for bid in bids if float(bid[0]) >= bid_threshold]
    topAsks = [ask for ask in asks if float(ask[0]) <= ask_threshold]

    bidSum = sum(float(bid[1]) for bid in topBids)
    askSum = sum(float(ask[1]) for ask in topAsks)

    delta = bidSum - askSum
    return delta
