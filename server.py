from flask import Flask, abort, request 
from req import get_weather
from datetime import datetime
from news_list import all_news
import requests

city_id = 479561
apikey = '8ded20b5e0dc6be380bc14a80d526bb2'
#переменная кот. содержит каркас приложения
app = Flask(__name__)

#создаем страницу test
@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime('%d.%m.%Y')
	#print(cur_date)

	result = "<p><b>Температура:</b> %s</p>" % weather['main']['temp']
	result += "<p><b>Город:</b> %s</p>" % weather['name']
	result += "<p><b>Дата:</b> %s</p>" % cur_date
	return result

@app.route("/news")
def all_the_news():
	#for item in request.args:
	#	print(item)
	#	print(request.args.get(item))
	#нельзя передовать перменные без обработки в БД и т.д.
	#limit = request.args.get('limit', 'all')
	colors = ['green', 'red', 'blue', 'magenta']
	#
	try:
		limit = int(request.args.get('limit'))
	except:
		limit = 10
	#
	color = request.args.get('color', 'black') if request.args.get('color', 'black') in colors else 'black'
	return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)


@app.route("/news/<int:news_id>")
def news_by_id(news_id):
	news_to_show = [news for news in all_news if news['id'] == news_id]
	#print(news_to_show)
	if len(news_to_show) == 1:
		result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
		result = result % news_to_show[0]
		return result
	else:
		abort(404)

#имена 
@app.route("/names")
def all_names():
	url = "http://api.data.mos.ru/v1/datasets/2009/rows"
	popular_names = requests.get(url).json()

	try:
		year = int(request.args.get('year'))
	except:
		year = 2015

	data_newborn = [i for i in popular_names]
	
	result = "<table><tr><th>%s</th><th>%s</th><th>%s</th></tr>" % ('Имя','Год','Число родившихся')
	
	for i in data_newborn:
		if i['Cells']['Year'] == year:
			result += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (i['Cells']['Name'],i['Cells']['Year'],i['Cells']['NumberOfPersons'])
	result += "</table>"
	
	#for data in data_newborn:
	#	print(data) # + ' ' + data_newborn['Cells']['Year']  + ' ' + data_newborn['Number'])
	
	return result
			
#проверка что программа запущена в консоли, 
# а не импортирована в качестве модуля
if __name__ == '__main__':
	app.run(port=5010,debug=True)
