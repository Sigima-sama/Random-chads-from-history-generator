import random, urllib.request
lines = open('Chads.txt').read().splitlines()
myline =random.choice(lines)
print(myline)


# Fetch wikipedia page
try:
  link = "https://en.wikipedia.org/wiki/"+myline.replace(" ","_")
  page = urllib.request.urlopen(link)
  if(page.getcode() == 200):
    print("Read more about "+myline+" at Wikipedia on: "+link)
except:
    print("No Wikipedia page found.")
