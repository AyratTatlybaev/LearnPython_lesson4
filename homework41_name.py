import requests

def get_name(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print("Что-то пошло не так!")
#проверка что программа запущена в консоли, 
# а не импортирована в http://api.data.mos.ru/v1/datasets/2009/rowsкачестве модуля
if __name__ == "__main__":
	data = get_name("http://api.data.mos.ru/v1/datasets/2009/rows")
	print(data)