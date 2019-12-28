
from datetime import datetime
import twitter
from twitter import OAuth
date = datetime.today().strftime('%Y-%m-%d')
day = int(date[-2:])
day =-7
sevendays = (date[:7] + str(day))

api = twitter.Twitter(auth=OAuth("2964621776-PLGxDSbvWvt6bLRXEYdTERnIZeQndYiUv5hqOWO",
                  "VX1meeC1rHbywAvPp4jcOiwJV1i2cM4IGodupdcP4I8Gq",
                  "aufAcUAjSUsRHkA1eiZDMc4Ew",
                  "hcuEfRlDgZJ4FzRFHLdRZaWFWLMkHlW7Xbh7nL0HeQbfjQaaLR"))
squirtle = len(api.search.tweets(q="squirtle", since = sevendays)["statuses"])
charmander = len(api.search.tweets(q="charmander", since = sevendays)["statuses"])
bulbasaur = len(api.search.tweets(q="bulbasaur", since = sevendays)["statuses"])

total= squirtle+charmander+bulbasaur
print("""From the the past 7 days the popularity(tweets) of 1st gen starters was: 
Bulbasaur: {}%, Charmander: {}%, and Squirtle: {}%""".format(bulbasaur/total*100,charmander/total*100,squirtle/total*100))