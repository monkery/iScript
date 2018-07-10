# coding=utf-8
import os
import re
import ssl
import urllib.request
from bs4 import BeautifulSoup


class htmlReader:
    def getHtml(self, url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        req = urllib.request.Request(url, headers=header)
        page = urllib.request.urlopen(req)
        html = page.read()
        html = html.decode('utf-8')
        return html


class articleReader(htmlReader):
    #暂时没用到
    def saveImgByUrlList(self,urlList):
        if len(urlList) == 0:
            return
        else:
            for url in urlList:
                self.saveImgByUrl(self, url)

    def saveImgByUrl(self, url, base_dir='d:/spider/Maldives'):
        filename = ''
        imgfilenames = re.findall('/([0-9A-Za-z]*\\.jpg)$', url)
        if len(imgfilenames) != 1:
            #print('没有在%s中匹配到符合要求的照片名称'%url)
            return 0
        else:
            filename = imgfilenames[0]
        urllib.request.urlretrieve(url,'%s/%s'%(base_dir, filename))
        return 1
    
    def downloadImg(self, url, page=1):
        sum = 0
        if url == None or url == '':
            print('没有设置检索的url')
            return sum
        print('============当前为帖子的第%d页============='%page)
        only_cur_page_flag = False
        if '?' in url:
            only_cur_page_flag = True

        if page > 1:
            cur_page_url = url + '?pn='+str(page)
        else:
            cur_page_url = url
        print('url is : %s'%cur_page_url)
        content = self.getHtml(cur_page_url)
        soup = BeautifulSoup(content, 'lxml')
        list = soup.select(self.config.get('img_selector'))#使用选择器， 因为不太会用 find 和find_all
        
        for img in list:
            img_url = img['src']
            sum +=self.saveImgByUrl(img_url, self.config.get('base_dir'))
        
        print('============帖子的第%d页结束============='%page)
        if only_cur_page_flag:
            return sum

        #获取页码信息
        page_info = soup.select("div.l_thread_info li:nth-of-type(2) span:nth-of-type(2)")[0]
        page_max = int(page_info.get_text())
        if page_max > page:
            sum += self.downloadImg(url, page+1)
        else:
            print('============帖子结束=============')
        return sum

    def __init__(self, **config):
        #self.url = url
        if config != None:
            for key in config:
                self.config[key] = config[key]
    
    #url = 'http://tieba.baidu.com/p/3509553327'
    config = {
        'base_dir' : 'd:/spider/Maldives',
        'img_selector' : 'div.j_d_post_content img'
    }

    #ssl._create_default_https_context = ssl._create_unverified_context


class tiebaReader(htmlReader):
    def downloadImg(self, url, page=1):
        sum = 0
        if url == None or url == '':
            print('没有设置检索的url')
            return sum
        print('============当前为贴吧的第%d页============='%page)
        
        #&pn=50
        cur_page_url = url
        if page > 1:
            offset = 50*(page-1)
            if '?' in url:
                cur_page_url = url + '&pn='+str(offset)
            else:
                cur_page_url = url + '?pn='+str(offset)
        
        print('teiba_url is : %s'%cur_page_url)
        content = self.getHtml(cur_page_url)
        soup = BeautifulSoup(content, 'lxml')
        list = soup.select('#thread_list li a.j_th_tit')#使用选择器， 因为不太会用 find 和find_all
        
        reader= articleReader()
        for article in list:
            temp_url = article['href']
            reader.downloadImg(self.base_url + temp_url)

            
        
        print('============贴吧的第%d页结束============='%page)
        
        #获取页码信息
        page_info_list = soup.select("div.th_footer_l span")
        print(len(page_info_list)
        
        # page_info = page_info_list[index]
        # article_max = int(page_info.get_text())
        # if article_max > page*50:
        #     sum += self.downloadImg(url, page+1)
        # else:
        #     print('============结束=============')
        return sum

    base_url = 'http://tieba.baidu.com'



'''
r = Reader()
content = r.getHtml('http://tieba.baidu.com/p/3442336728?pn=2')
soup = BeautifulSoup(content, 'lxml')
list = soup.select('div.j_d_post_content img ')#使用选择器， 因为不太会用 find 和find_all
print('have %d pics'%len(list))
for img in list:
    url = img['src']
    print(url)
    r.saveImgByUrl(url)
'''
# r = articleReader()
# count = r.downloadImg('http://tieba.baidu.com/p/3442336728')
# print('共下载%d张图片'%count)
r = tiebaReader()
r.downloadImg('http://tieba.baidu.com/f?kw=%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB&ie=utf-8&tab=good&pn=150')




