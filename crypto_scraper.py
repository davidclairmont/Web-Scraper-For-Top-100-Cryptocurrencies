from bs4 import BeautifulSoup
import requests
import csv

ranks = []
names = []
market_caps = []
prices = []
volumes = []
supplies = []
ticker_symbols = []
changes = []


## requests the page of coinmarketcap.com that contains the top 100 cryptos ranked by market cap
r = requests.get('https://coinmarketcap.com/')
## compresses all text from the page request
data = r.text
## creates a BeautifulSoup object called soup in order to parse website data
soup = BeautifulSoup(data, 'html.parser')
## the prettify method turns the parsed website data into a formatted string
soup.prettify()

## for loop to go through every tr tag within the tbody tag
## this is used to access the info for the top 100 cryptos
for tr_tags in soup.tbody:
    td_count = 0
    ## for loop to loop through the td tags for each crypto. each will only have 9 td tags
    ## only the first 7 td tags are used to extract information
    for td_tags in tr_tags:
        td_count+=1

        ## grabs the rank of the crypto from the 1st td tag
        if td_count == 1:
            rank = str(td_tags.find("div").text)
            ranks.append(rank)

        ## grabs the name of the crypto from the 2nd td tag
        elif td_count == 2:
            name = str(td_tags.find("a").text)
            names.append(name)

        ## grabs the market cap of the crypto from the 3rd td tag 
        elif td_count == 3:
            market_cap = str(td_tags.find("div").text)
            market_caps.append(market_cap)

        ## grabs the current price of the crypto from the 4th td tag
        elif td_count == 4:
            price = str(td_tags.find("a").text)
            prices.append(price)

        ## grabs the volume of the crypto over the last 24 hours from the 5th td tag
        elif td_count == 5:
            volume = str(td_tags.find("a").text)
            volumes.append(volume)

        ## grabs the current circulating supply and the ticker of the crypto from the 6th td tag
        elif td_count == 6:
            supply = str(td_tags.find("div").text)
            ticker_symbol = supply.split()[1]
            supply = supply.split()[0]
            supplies.append(supply)
            ticker_symbols.append(ticker_symbol)
            
        ## grabs the percent change of the price of the crypto over the last 24 hours from the 7th td tag
        elif td_count == 7:
            percent_change = str(td_tags.find("div").text)
            changes.append(percent_change)

        else:
            break

with open('top_100_cryptos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rank", "Ticker symbol", "Name", "Market Cap", "Price", "Volume(24h)", "Circulating Supply", "Change(24h)"])
    for i in range(0,100):
        row = [ranks[i], ticker_symbols[i], names[i], market_caps[i], prices[i], volumes[i], supplies[i], changes[i]]
        writer.writerow(row)
