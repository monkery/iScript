
import re
import ssl
import urllib.request
import threading


urlList = [
'http://bit.ly/Celsius-SR3-stream-applications-rabbit-maven',
'http://bit.ly/Celsius-SR3-stream-applications-rabbit-docker',
'http://bit.ly/Celsius-SR3-stream-applications-kafka-10-maven',
'http://bit.ly/Celsius-SR3-stream-applications-kafka-10-docker',
'http://bit.ly/Celsius-BUILD-SNAPSHOT-stream-applications-rabbit-maven',
'http://bit.ly/Celsius-BUILD-SNAPSHOT-stream-applications-rabbit-docker',
'http://bit.ly/Celsius-BUILD-SNAPSHOT-stream-applications-kafka-10-maven',
'http://bit.ly/Celsius-BUILD-SNAPSHOT-stream-applications-kafka-10-docker',
'http://bit.ly/Darwin-GA-stream-applications-rabbit-maven',
'http://bit.ly/Darwin-GA-stream-applications-rabbit-docker',
'http://bit.ly/Darwin-GA-stream-applications-kafka-10-maven',
'http://bit.ly/Darwin-GA-stream-applications-kafka-10-docker',
'http://bit.ly/Darwin-BUILD-SNAPSHOT-stream-applications-rabbit-maven',
'http://bit.ly/Darwin-BUILD-SNAPSHOT-stream-applications-rabbit-docker',
'http://bit.ly/Darwin-BUILD-SNAPSHOT-stream-applications-kafka-10-maven',
'http://bit.ly/Darwin-BUILD-SNAPSHOT-stream-applications-kafka-10-docker'
]

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

base_dir='d:/spider/gy'

def saveByUrl(url, base_dir='d:/spider/gy'):
        print('开始下载路径：%s'%url)
        filename = ''
        filenames = getFileName(url)
        if len(filenames) != 1:
            #print('没有在%s中匹配到符合要求的文件'%url)
            return 0
        else:
            filename = filenames[0]
        print('开始下载路径%s对应的%s'%(url,filename))
        urllib.request.urlretrieve(url,'%s/%s'%(base_dir, filename))
        print('%s下载完成'%filename)
        return 1


def getFileName(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url, headers=header)
    response=urllib.request.urlopen(req)
    print(response.geturl())
    filename = re.findall('/([0-9A-Za-z\\-\\.]*)$', response.geturl())
    return filename

for url in urlList:
    # saveByUrl(url, base_dir)
    # getFileName(url)
    t =threading.Thread(target=saveByUrl,args=(url, base_dir))
    t.start()
