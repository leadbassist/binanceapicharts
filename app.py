from flask import Flask, render_template, request, flash, redirect
import config, csv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *

app = Flask(__name__)
app.secret_key = b'kjhdsafhdfihiadhcj'

client = Client(config.API_KEY, config.API_SECRET)


@app.route("/")
def index():
    title = "CoinView"

    account = client.get_account()

    balances = account["balances"]

    exchange_info = client.get_exchange_info()
    symbols = exchange_info["symbols"]

    return render_template("index.html", title=title, my_balances=balances, symbols=symbols)

@app.route("/buy", methods=["POST"])
def buy():
    print(request.form)
    try:
        order = client.create_order(
            symbol=request.form["symbol"],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,

            quantity=request.form["quantity"],)
    except Exception as e:
        flash(e.message, "error")



    return redirect("/")

@app.route("/sell")
def sell():
    return "sell"

@app.route("/settings")
def settings():
    return "settings"