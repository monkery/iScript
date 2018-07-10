from city import city
import urllib.request

def getCityWeather():
    cityname = input('你想查哪个城市的天气？\n')
    citycode = city.get(cityname)
    if citycode:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib.request.urlopen(url).read()
        print('%s的天气是：%s'%[cityname, content])
    else:
        print('未找到')
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % '101010100')
        content = urllib.request.urlopen(url).read()
        print(content)


#getCityWeather()

url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
send_headers={  
                  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
                  'Connection':'keep-alive',  
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'  
                  }
req = urllib.request.Request(url,headers=send_headers)
content = urllib.request.urlopen(req).read()
print(type(content))
print(content)

import json
data = json.loads(content)
print(type(data))
print(data)

result = data['weatherinfo']
str_temp = ('%s:%s，%s ~ %s') % (
   result['city'],
   result['weather'],
   result['temp1'],
   result['temp2']
)

print(str_temp)

print('try to get city info')
cityurl = 'http://m.weather.com.cn/data3/city%s.xml'
result = 'city = {\n'
content1 = urllib.request.urlopen(cityurl%'').read()
provinces = content1.decode('utf-8').split(',')
print(provinces)
for province in provinces:
    arr = province.split('|')
    p_code = arr[0]
    content2 = urllib.request.urlopen(cityurl%p_code).read()
    citys = content2.decode('utf-8').split(',')
    print('citys in %s :'% arr[1])
    print(citys)
    for c in citys:
        c_code = c.split('|')[0]
        content3 = urllib.request.urlopen(cityurl%c_code).read()
        districts = content3.decode('utf-8').split(',')
        print('districts in %s :'% c.split('|')[1])
        print(districts)
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            content4 = urllib.request.urlopen( cityurl % d_code).read().decode('utf-8')
            print("Data:%s"%content4)
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print('%s : %s'%(name,code))
result += '}'
f = open('city.py', 'w')
f.write(result)
f.close()

