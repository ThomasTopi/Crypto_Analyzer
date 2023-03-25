from tradingview_ta import TA_Handler, Interval, Exchange


SYMBOLS = ["BTCUSDT31H2023", "TRUUSDT", "LINKUSDT", "BANDUSDT" ]
SCREENER = "crypto"
EXCHANGE = "BINANCE"

for i in SYMBOLS:
    BTC = TA_Handler(
        symbol = i,
        screener = SCREENER,
        exchange = EXCHANGE,
        interval = Interval.INTERVAL_1_DAY
        )

    print(i+":", BTC.get_analysis().summary)



