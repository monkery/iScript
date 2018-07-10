#!/usr/bin/python
#coding:utf-8
#作者：Byron
#博客：http://jiabin.tk
import urllib.request
import re
import ssl
#定义程序主函数
def qiubai(page):
    url = "https://www.qiushibaike.com/week/page/%d" % page
    re_qb = re.compile(r'detail.*?<a.*?>(.*?)<.*?title="(.*?)">\s*(.*?)\s*?<',re.DOTALL)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0' }
    req = urllib.request.Request(url, headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    html = html.decode('utf-8')
    my_qiubai = re_qb.findall(html)
    n = len(my_qiubai)
    for i in range(n):
        for k in range(3):
            print(my_qiubai[i][k])
        s = input("回车继续")
        if s == "q":
            exit()
        print("-"*40)
#定义程序循环体
def for_qb():
    for page in range(int(p),280):
        print("-"*18 + "第" + str(page) + "页" + "-"*18)
        qiubai(page)
#该部分代码的目是为了设计的严谨，尽可能的使程序不发生崩溃
def if_qb():
    global p
    p = input("输入要看的页数1~280:")
    if p == "q":
        exit()
    elif not p.isdigit() or p =="0" or int(p) > 280:
        if_qb()
    else:
        for_qb()
ssl._create_default_https_context = ssl._create_unverified_context

print("-"*40)
print("糗百命令行版——Byron")
print("一入糗百深似海，从此节操是路人")
print('输入"q"退出程序')
print("-"*40)
if_qb()