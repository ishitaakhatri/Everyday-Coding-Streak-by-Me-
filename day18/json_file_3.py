import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/news/joe-biden-ends-campaign-endorses-vp-harris-throwing-election-into-unprecedented-chaos-180606770.html") as response:
    source = response.read() 

data = json.loads(source)
print(json.dump(data,indent=2))
