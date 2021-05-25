import requests as r
import re

def Get_Data(username):
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
	import os; output = Get_Data(os.environ["Duolingo_Username"])
	Days_left = re.sub("[^0-9]", "", re.search('<h2>(.*)!</h2>',output ).group(1) )
	Persentage_Completed = re.search('<b>(.*)complete</b>',output ).group(1)
	print(f"{Persentage_Completed}complete.")
	print(f"{Days_left} days left.")