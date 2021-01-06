# Using Random.org and https://www.mit.edu/~ecprice/wordlist.10000

import requests
import re

data = []
with open("wordlist_10000.txt","r") as f:
    data = f.readlines()

response = requests.get("https://www.random.org/integers/?num=1&min=1&max=5000&col=1&base=10&format=plain&rnd=new")
word_a = data[int(response.text)]

response = requests.get("https://www.random.org/integers/?num=1&min=5000&max=10000&col=1&base=10&format=plain&rnd=new")
word_b = data[int(response.text)]

result = str(word_a) + "-" + str(word_b)

replaced = re.sub('\n', '', result)
print(replaced)
