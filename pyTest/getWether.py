import urllib.request as urlRequest
import ssl
import json

_url_template = 'https://www.sojson.com/open/api/weather/json.shtml?city=%s'
city = '北京'   
url = _url_template%(urlRequest.quote(city))

ssl._create_default_https_context = ssl._create_unverified_context
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0' }

req = urlRequest.Request(url, headers=header)
result = urlRequest.urlopen(req).read().decode('utf-8')
data = json.loads(result)

date = data.get('date')
times = data.get('count')
city2 = data.get('city')
info = data.get('data')
humidity = info.get('shidu')
temperature = info.get('wendu')
pm25 = info.get('pm25')
pm10 = info.get('pm10')
quality = info.get('quality')

print('日期：%s, 第%s次查询\n城市：%s\n气温:%s\n湿度:%s\npm2.5:%s\npm10:%s\n空气质量:%s\n'%(date, times, city2, temperature, humidity, pm25, pm10, quality))



