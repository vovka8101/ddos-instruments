import requests
import sys

alive = []
amount, success, tout = 0, 0, 10.0

i = 1
for arg in sys.argv[1:]:
	if arg == "-t":
		tout = float(sys.argv[i + 1])
	i += 1


with open("sites.txt", encoding="utf-8") as f:
	for site in f:
		site = site.rstrip()
		amount += 1
		try:
			response = requests.get(site, timeout=tout)
			print(f"{amount}. {site} : OK | Kode: {response.status_code}")
			alive.append(site)
			success += 1
		except requests.exceptions.RequestException:
			print(f"{amount}. {site} : ERROR")


print(f"{success}/{amount}\n")
if len(alive) > 0:
	for link in alive:
		print(link)
