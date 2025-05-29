from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/hacim')
def hacim():
    symbol = request.args.get('symbol', 'BTCUSDT')
    interval = request.args.get('interval', '5m')
    limit = request.args.get('limit', '2')
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        res = requests.get(url)
        data = res.json()
        volumes = [float(row[5]) for row in data]
        return jsonify(volumes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
