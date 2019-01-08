# PyCandleData
This is script scrapes candle data for FX pairs from Oanda servers.

# Getting started
<b>DISCLAIMER! Forex trading carries a heavy amount of risk. Any and everything outlined in this code is for educational purposes only. I am not responsible for any of your losses or any hardships you may face as a result of using this code. Again, this is meant to be used ONLY for educational purposes.</b>

You will need to install <a href="https://github.com/hootnot/oanda-api-v20">oandapyV20</a>.
If you do not know how to setup a python environment, I reccomend using Anaconda or learning how to use virtualenv. There are numerous tutorials online for this.


1. Create a demo account with <a href="https://oanda.com">Oanda</a> and obtain an api key.
2. Place your api key in the script under "access_token".
3. Adjust the script best on the type of data you would like. Ex.(Granularity, pair, timezone). Checkout Oanda's API endpoints for the type of data you want to grab. This should be pretty self-explanatory from the script. http://developer.oanda.com/rest-live-v20/introduction/
3. Point your terminal to the project directory and run getCandleData.py in terminal with:

> user$: python getCandleData.py

Data will be stored in a folder titled "dataStore" in whatever directory you placed the script.
