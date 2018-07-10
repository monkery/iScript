# coding=utf-8
import re
import urllib.request
import ssl

class QiuReader:
    def getHtml(self, url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0' }
        req = urllib.request.Request(url, headers=header)
        page = urllib.request.urlopen(req)
        html = page.read()
        html = html.decode('utf-8')
        return html

    def getImg(self, html):
        reg = r'<p class="img_title">(.*)</p>'
        img_title = re.compile(reg)
        imglist = re.findall(img_title, html)
        return imglist
    
    def getImgUri(self, html):
        #引入bs4,解析html页
        reg = r'<p class="img_title">(.*)</p>'
        img_title = re.compile(reg)
        imglist = re.findall(img_title, html)
        return imglist

    def saveImgByUriList(self, urlList)：
        if len(urlList) == 0:
            return
        else:
            for uri in urlList:
                filename = ''
                imgfilenames = re.findall('/^[/\\]*$', uri)
                if len(imgfilenames) != 1:
                    print('没有在%s中匹配到照片名称'%uri)
                    continue
                else:
                    filename = imgfilenames[0]
                urllib.request.urlretrieve(imgurl,'d:\\%s'% filename)


    # id="qiushi_tag_***"
    # 正文：<div class="content"><span></span></div>
    # 图片：<div class="thumb"></div>
    def getContent(self, html):
        reg = r'<div class="content">\s*<span>\s*(.*)\s*</span>\s*</div>'
        contentReg = re.compile(reg)
        list = re.findall(contentReg, html)
        return list


    def printContent(self, list):
        index = 1
        for str in list:
            print('-'*20, index, '-'*20, sep='' )
            print(str)
            print()
            index += 1

    url_temp = 'https://www.qiushibaike.com/8hr/page/%d/'
    ssl._create_default_https_context = ssl._create_unverified_context
    # url = "https://tieba.baidu.com"
    def read(self):
        page = input('请问要看哪页？')
        try:
            url = self.url_temp%int(page)
            #print('url is %s'%url )
            html = self.getHtml(url)
            # imglist = getImg(html)
            content=self.getContent(html)
            self.printContent(content)
        except:
            print("出错啦！")

reader = QiuReader()
flag = True
while flag:
    reader.read()
    flag = ('y' == input('是否继续？ y继续，其他键结束'))

print('byebye')
