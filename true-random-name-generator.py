# Using Random.org and https://www.mit.edu/~ecprice/wordlist.10000

import requests
import re

data = []
with open("wordlist_10000.txt","r") as f:
    data = f.readlines()

response = requests.get("https://www.random.org/integers/?num=2&min=1&max=5000&col=1&base=10&format=plain&rnd=new")
response_array = re.split("\n", response.text)

del response_array[-1]

respone_unfiltered = data[int(response_array[0])] + "-" + data[int(response_array[1])]

respone_cleaned = re.sub("\n", "", respone_unfiltered)

print(respone_cleaned)
