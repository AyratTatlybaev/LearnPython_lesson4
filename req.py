import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print("Что-то пошло не так!")
#проверка что программа запущена в консоли, 
# а не импортирована в качестве модуля
if __name__ == "__main__":
	data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=479561&APPID=8ded20b5e0dc6be380bc14a80d526bb2&units=metric")
	#popular_names = get_weather("http://api.data.mos.ru/v1/datasets/2009/rows")
	#print(popular_names)