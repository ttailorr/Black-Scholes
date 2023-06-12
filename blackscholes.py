#Black Scholes Model calculation
#Inputs:
# S0 - Initial Stock Price
# K - Strike Price
# r - Risk-free Rate
# T - Time to Maturity (in years)
# sigma - Volatility

#Output:
# C - Theoretical Call Option Price
# P - Theoretical Put Option Price

import math
from polygon import RESTClient


key = 'lBrnXp59pSkkXvyS8P3KwaM6OYTslr41'
client = RESTClient(key)


contractNames = []
for i in client.list_options_contracts(underlying_ticker = 'AAPL', limit = 1000):
    contractNames.append(i)
#print(contractNames)

contractData = contractNames[398]


optionsTicker = contractData.ticker
#initialPrice = client.get_previous_close_agg(optionsTicker, True, None, False)
initialPrice = 140.89
strikePrice = contractData.strike_price
risk = 4.15
time = 1
volatility = 33



def black_scholes (S0, K, r, T, sigma):
   # Calculate d1 and d2
   d1 = (math.log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
   d2 = (math.log(S0 / K) + (r - 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))

   # Calculate C and P
   C = S0 * math.erf(d1) - K * math.exp(-r * T) * math.erf(d2)
   P = K * math.exp(-r * T) * math.erf(-d2) - S0 * math.erf(-d1)

   print("Call option price: " + str(C))
   print("Put option price: " + str(P))




black_scholes(initialPrice, strikePrice, risk, time, volatility)
