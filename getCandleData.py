# Oanda Packages
from oandapyV20 import API
import csv

access_token = "######"
params = {
  "count": 4000,
  "granularity": "H1",
  "alignmentTimezone": "America/Los_Angeles"
}

client = API(access_token=access_token, environment="practice")

pairs = ["EUR_USD", "EUR_GBP", "EUR_AUD", "EUR_JPY", "USD_JPY", "GBP_USD", "AUD_USD"]

class main():

	def __init__(self):
		return

	def feedData(self):
		for pair in pairs:
		    # Call imported user1 class
		    o = instruments.InstrumentsCandles(instrument=pair, params=params)
		    client.request(o)
		    candles = o.response.get("candles")

		    # OHLC variables to return in array
		    self.wO = []
		    self.wH = []
		    self.wL = []
		    self.wC = []
		    self.wV = []
		    self.wD = []
		    for x in range(0, params["count"]):
		        candleData = candles[x].get("mid")
		        candleDate = candles[x].get("time")
		        v = candles[x].get("volume")
		        o = candleData.get("o")
		        h = candleData.get("h")
		        l = candleData.get("l")
		        c = candleData.get("c")
		        self.wO.append(float(o))
		        self.wH.append(float(h))
		        self.wL.append(float(l))
		        self.wC.append(float(c))
		        self.wV.append(float(v))
		        self.wD.append(candleDate)
            # Write to CSV
		    with open("./dataStore/" + pair + "1H.csv", "w") as csvfile:
		    	wr = csv.writer(csvfile, delimiter=',')
		    	for i in range(0, len(self.wO)):
		    		wr.writerow([self.wD[i], self.wO[i],self.wH[i],self.wL[i],self.wC[i]])


if __name__ == "__main__":
	m = main()
	print m.feedData()
