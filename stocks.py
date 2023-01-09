import requests
import pandas as pd
import matplotlib.pyplot as plt

#play with these stock symbols for more comparisons -> https://finance.yahoo.com/lookup/index/
companies = ['NVDA','F', 'MSFT','GOOG','TSLA']
listofdf = []
yourAPIKEY = ""

for item in companies:
    histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line&from=2020-03-12&to=2021-03-12&apikey={yourAPIKEY}")
    histprices = histprices.json()
    print(histprices) 

#get subset of prices
    histprices = histprices['historical'][-200:]

#Merge prices and Convert to dataframe
    histpricesdf = pd.DataFrame.from_dict(histprices)

    histpricesdf = histpricesdf.rename({'close': item}, axis=1)

    listofdf.append(histpricesdf)

#set date as index
dfs = [df.set_index('date') for df in listofdf]

histpriceconcat = pd.concat(dfs,axis=1)

#calculate results as a percentage of the base date
histpriceconcat = histpriceconcat/histpriceconcat.iloc[0]

for i, col in enumerate(histpriceconcat.columns):
    histpriceconcat[col].plot()

plt.title('Trend Analysis')
plt.xticks(rotation=70)
plt.legend(histpriceconcat.columns)
plt.savefig('trendy.png', bbox_inches='tight')