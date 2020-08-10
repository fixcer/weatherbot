import json
from unidecode import unidecode
import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

with open("city.json", "r") as read_file:
	data = json.load(read_file)

dicter = {}

for i in range(len(data)):
	dicter[unidecode(data[i]['name']).lower()] = data[i]['id']


def getWeather(city_id):
	try:
		city_id = dicter[unidecode(city_id.lower().strip())]
		URL = "https://weather.com/vi-VN/weather/tenday/l/" + city_id
		res = requests.get(URL)
		
		if res.status_code != 200:
			return "Có lỗi xảy ra, chúng tôi không lấy được dữ liệu"
		else:
			soup_data = BeautifulSoup(res.text, 'html.parser')
			temperature = soup_data.find("span", attrs={"data-testid": "TemperatureValue"})
			a = temperature.text
			b = temperature.find_next("span", attrs={"data-testid": "TemperatureValue"}).text

			temperature = soup_data.find_all("div", attrs={"data-testid": "detailsTemperature"})

			for i in range(len(temperature)):
				temperature[i] = temperature[i].text.split('/')

			temperature[:0] = [[a, b]]

			description = soup_data.find_all("p", attrs={"data-testid": "wxPhrase"})
			UV = soup_data.find_all("span", attrs={"data-testid": "UVIndexValue"})
			humidity = soup_data.find_all("li", attrs={"data-testid": "HumiditySection"})

			details = []
			for i in range(len(UV)):
				if not i & 1:
					tmp = description[i].text.split('.')
					res = tmp[0] + tmp[2] + ".\n" + tmp[3] + ", nhiệt độ " + temperature[i//2][1] + "C - " + \
                            		temperature[i//2][0] + "C.\n" + "Chỉ số UV " + \
                    		        UV[i].text + ", độ ẩm " + humidity[i].text[5:] + "\n"
					details.append(res)

			return details
	except:
		return "Vị trí này ngoài phạm vi của tôi rồi"
