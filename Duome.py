import requests as r
import re, os, datetime

class Duolingo_User():
	def __init__(self, username):
		self.username = username
		self.RAW_HTML = self.Get_Data(username)
		self.STR_DATE_COMPLETION = re.search('b>\d\d\d?\d?-\d\d\d?\d?-\d\d\d?\d?', self.RAW_HTML).group(0).replace("b>", "")
		self.Date_completion = datetime.datetime(int(self.STR_DATE_COMPLETION[:4]), int(self.STR_DATE_COMPLETION[5:][:2]), int(self.STR_DATE_COMPLETION[:2]))# Year, Month, Day
		self.Days_left = re.sub("[^0-9]", "", re.search('<h2>(.*)!</h2>', self.RAW_HTML ).group(1) )
		self.Persentage_Completed = re.search('<b>(.*)complete</b>', self.RAW_HTML ).group(1)
		self.Strength = re.search('\d\d\d?\d?', re.search('<b>Strength:</b> \d\d?\d?%', self.RAW_HTML).group(0)).group(0)
		self.ETA_RAW =  self.Date_completion - datetime.datetime.now() # item.ETA.days
		self.ETA =  (self.Date_completion - datetime.datetime.now()).days # item.ETA.days
	def Get_Data(self, username):
		url = f"https://duome.eu/{username}"
		headers = {
		'authority': 'duome.eu',
		'method': 'GET',
		'path': f'/{username}',
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
		'cache-control': 'no-cache',
		'cookie': 'PHPSESSID=708cb873e303cb1007b19735f87e8b5d',
		'pragma': 'no-cache',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
		}
		return r.get(url=url, headers=headers).text

if __name__ == '__main__':
	item = Duolingo_User(os.environ['DuolingoUsername'])
	print(item.Days_left)
	print(item.Persentage_Completed)
	print(item.Strength)
	print(item.Date_completion)
	print(item.ETA)