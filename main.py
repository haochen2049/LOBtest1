
# import cryptofeed
# from cryptofeed import FeedHandler
#
#
# fh = FeedHandler()
#
# # ticker, trade, and book are user defined functions that
# # will be called when ticker, trade and book updates are received
# from cryptofeed import FeedHandler
# from cryptofeed.backends.arctic import FundingArctic, TickerArctic, TradeArctic
# from cryptofeed.defines import FUNDING, TICKER, TRADES
# from cryptofeed.exchanges import Bitfinex, Bitmex, Coinbase
#
#
# def main():
#     f = FeedHandler()
#     f.add_feed(Coinbase(channels=[TICKER], symbols=['BTC-USD'], callbacks={TICKER: TickerArctic('cryptofeed-test')}))
#     f.run()



# const websocket = new CoinbasePro.WebsocketClient(
#   ["BTC-EUR"],
#   "wss://ws-feed.pro.coinbase.com",
#   null, // <-- you need to put your API key in
#   {
#     channels: ['ticker']
#   }
# );
# websocket.on('message',data=>data.type==='ticker'&&xPrice=data.price&&console.log(data.price, data))
#                              // (only want to see ticker messages)
#                              // you will receive heartbeat (keep-alive) and ticker messages
#                              // asynchronous callback will send data when it is available
#                              // you must wait for data to be available and act on it

import time, cbpro

# Simple WebSocket
wsc = cbpro.WebsocketClient(url="wss://ws-feed.pro.coinbase.com",
                                products="BTC-USD",
                                channels=["ticker"])


# WebSocket Class Example
class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USDT"]
        self.channels=["ticker"]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if (msg["type"] =="received"):
            print ("Message type:", msg["type"], "\ttrade_id:{:.0f}".format(float(msg["trade_id"]))
                   , "\tsequence:{:.0f}".format(float(msg["sequence"])), "\ttime:", msg["time"]
                   , "\tproduct_id:", msg["product_id"], "\tprice:{:.3f}".format(float(msg["price"]))
                   , "\tside:", msg["side"], "\tlast_size:{:.8f}".format(float(msg["last_size"]))
                   , "\tbest_bid:{:.0f}".format(float(msg["best_bid"])), "\tbest_ask:{:.0f}".format(float(msg["best_ask"]))
                   )
    def on_close(self):
        print("Closing")

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products, wsClient.channels)
while (wsClient.message_count < 50):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(1)
wsClient.close()



# if __name__ == '__main__':
#     main()
