import yfinance as yf

#inputing stock symbol
name = input(" ENTER STOCK SYMBOL")

#storing the values in a variable x
Stock = yf.Ticker(name)
x=Stock.info

#extracting r
r = x['pegRatio']

#extracting PE ratio
PE = x['trailingPE']

#extracting EPS
EPS = x['trailingEps']

#extracting previous day close
previous_close = x['previousClose']

#formula for calculating the intrinsic value of the stock
intrinsic_value = EPS * (1+(r/100)) * PE

previous_close = x['previousClose']

#printing all the statements 
print(f"r               : {r}")
print(f"PE              : {PE}")
print(f"EPS             : {EPS}")

print(" ")

print(f"intrinsic value : {intrinsic_value}")
print(f"Previous Close  : {previous_close}")

print(" ")

if previous_close<intrinsic_value:
  print("It is a good trade, since the current price is less than intrinsic price")
else:
  print("This parameter cannot be accurately used for investing.")
