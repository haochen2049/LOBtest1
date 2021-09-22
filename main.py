
import time, cbpro

# Simple WebSocket
wsc = cbpro.WebsocketClient(url="wss://ws-feed.pro.coinbase.com",
                                products="BTC-USD",
                                channels=["full"])


# WebSocket Class Example!!

class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USDT"]
        self.channels=["full"]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if (msg["type"] =="received"):
            print ("Message type:",msg["type"],"\ttime:",msg["time"],
                   "\tproduct_id:",msg["product_id"],"\tsequence:{:.0f}".format(float(msg["sequence"])),
                   "\torder_id:",msg["order_id"],"\tsize:{:.8f}".format(float(msg["size"])),
                   "\tprice:{:.3f}".format(float(msg["price"])),"\tside:",msg["side"],
                   "\torder_type:",msg["order_type"]
                   )
        elif (msg["type"] =="open"):
            print("Message type:", msg["type"]
                  )
        elif (msg["type"] =="done"):
            print("Message type:", msg["type"]
                  )
        elif (msg["type"] =="match"):
            print("Message type:", msg["type"]
                  )
        elif (msg["type"] =="change"):
            print("Message type:", msg["type"]
                  )
        elif (msg["type"] =="activate"):
            print("Message type:", msg["type"]
                  )
        elif 'taker_user_id' in msg:
            print("Message type:", msg["type"]
                  )
        else:
            print(400000004)

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



