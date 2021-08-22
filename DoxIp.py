import requests
import json
import pyfiglet
import os
os.system("clear")
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[39m'
p= pyfiglet.figlet_format("DoxIP")
print(RED+p)
print(GREEN+"===================================")
print(RED+"By L.C.A HACK\nYouTube: L.C.A HACK\nContactame: https://t.me/LCAHACK576")
print(GREEN+"===================================")
api_url = "http://ip-api.com/json/"
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
 res = requests.get(api_url+ip, data=data)
 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 ip = input(YELLOW+"Ingrese la dirección IP: "+RESET)

 par = parametros.split(",")
 for x in par:
  print(x.upper(), ":")
  print(ip_scraping(ip)[x])
  print("n")
