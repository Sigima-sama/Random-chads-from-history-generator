import random, urllib.request, os, requests

if os.path.isfile('Chads.txt') == False:
  ask = input("Chads.txt File is Missing, Download Standard List (y/n)?").lower()
  if "y" in ask:
    content = requests.get("https://raw.githubusercontent.com/Sigima-sama/Random-chads-from-history-generator/main/Chads.txt")
    if content.status_code != 200:
      print("Failed to Download")
      exit()
    try:
        make_file = open('Chads.txt', "w")
        make_file.write(content._content.decode("UTF-8"))
        make_file.close()
    except PermissionError:
        print("Permission Error!")
        exit()
    print("Complete")
    os.system('cls' if os.name=='nt' else 'clear')
  else:
    exit()
    
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
