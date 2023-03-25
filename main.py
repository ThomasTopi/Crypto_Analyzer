from tradingview_ta import TA_Handler, Interval, Exchange


SYMBOLS = ["BTCUSDT31H2023", "TRUUSDT", "LINKUSDT", "BANDUSDT", "UNIUSD", "ENJUSDT", "SOLUSDT", "RENUSDT",
          "LTCUSDT", "ETHUSDT"]

SCREENER = "crypto"
EXCHANGE = "BINANCE"
inter = [Interval.INTERVAL_4_HOURS, Interval.INTERVAL_1_DAY, Interval.INTERVAL_1_WEEK]

for i in SYMBOLS:
    print("----------------------------------------------------", i, '\n')
    for j in inter:
        BTC = TA_Handler(
            symbol = i,
            screener = SCREENER,
            exchange = EXCHANGE,
            interval = j
            )

        print("--------- Interval: ", j+": -------------", '\n')
        print(i+":", BTC.get_analysis().summary['RECOMMENDATION'])
        print("Close price is: ", BTC.get_analysis().indicators["close"], '\n')
   
    



