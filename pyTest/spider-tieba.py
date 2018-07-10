#!/usr/bin/python
#coding:utf-8
 

import re
import json
import urllib.error
import urllib.request
import time
import random
import os
import threading
import html.parser as HTMLParser
from bs4 import BeautifulSoup as BS
 
import sys
''' py2 写法
reload(sys)
sys.setdefaultencoding('utf-8')
'''
 
 
#处理页面标签类
class Tool:
	#去除img标签,7位长空格
	removeImg = re.compile(r'<img.*?>| {7}|')
	#删除超链接标签
	removeAddr = re.compile(r'<a.*?>|</a>')
	#把换行的标签换为\n
	replaceLine = re.compile(r'<tr>|<div>|</div>|</p>')
	#将表格制表<td>替换为\t
	replaceTD= re.compile(r'<td>')
	#把段落开头换为\n加空两格
	replacePara = re.compile(r'<p.*?>')
	#将换行符或双换行符替换为\n
	replaceBR = re.compile(r'<br><br>|<br>')
	#将其余标签剔除
	removeExtraTag = re.compile(r'<.*?>')
	#删除正斜线和反斜线
	removeLine1=re.compile(r'/')
	removeLine2=re.compile(r'\\')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n    ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		#strip()将前后多余内容删除
		return x.strip()
	def replaceSlash(self,x):
		x=re.sub(self.removeLine1,"",x)
		x=re.sub(self.removeLine2,"",x)
		return x.strip()
 
class GetBaiduTieba:
	def __init__(self,keyword):
		self.keyword=keyword
		self.tiebaUrl='http://tieba.baidu.com/f?kw=%s' % self.keyword
		self.tool=Tool()#初始化工具类
		
		self.info_list=[]#存贮帖子地址，标题，回复数，创建人，创建时间的全局变量
		self.tiezi_info_list=[]#存贮每一个帖子的回复情况，包括楼层，回复人，时间，内容，本楼层的评论数
		self.create_dir(self.keyword)
		self.tiezi_path=self.keyword+'/'+self.keyword+'.txt'
		self.tiezi_file=open(self.tiezi_path,'w')
	
	
	#创建文件夹
	def create_dir(self,path):
		if not os.path.exists(path):  
			os.makedirs(path) 
	
	#获取页面内容
	def get_html(self,url):
		self.my_log(1,u'start crawl %s ...' % url)
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}#设置header
		req = urllib.request.Request(url=url,headers=headers)
		try:
			html = urllib.request.urlopen(req).read().decode('utf-8')
			html=HTMLParser.HTMLParser().unescape(html)#处理网页内容， 可以将一些html类型的符号如" 转换回如" 转换回双引号
			#html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())#转码:避免输出出现乱码
		except urllib.error.HTTPError as e:
			self.my_log(2,u"连接百度贴吧失败，错误原因：%s " % e.code)
			return None
		except urllib.error.URLError as e:
			if hasattr(e,'reason'):
				self.my_log(2,u"连接百度贴吧失败，错误原因:%s " % e.reason)
				return None
		return html
	
	#自定义log 打印函数， 以数字定义log 级别
	def my_log(self,log_leavel,msg): 
		#0：不打印 		1：main		2：error		3：warning		
		log= {	0:lambda:no_log(msg),
				1:lambda:main_log(msg), 
				2:lambda:error_log(msg), 
				3:lambda:warning_log(msg)} 
		def no_log(msg):
			pass
		def main_log(msg):
			print(u'main: %s: %s' % (time.strftime('%Y-%m-%d_%H-%M-%S'), msg) )
		def error_log(msg):
			print(u'error: %s: %s' % (time.strftime('%Y-%m-%d_%H-%M-%S'), msg) )
		def warning_log(msg):	
			print(u'warning:  %s: %s' % (time.strftime('%Y-%m-%d_%H-%M-%S'), msg))
		return log[log_leavel]()
	
	#获取本贴吧总共有多少帖子
	def get_Total_Num(self,html):
		try:
			pattern=re.compile('<div id="frs_list_pager".*?class="next pagination-item ".*?href=(.*?)class=.*?</div>',re.S)#直接使用正则暴力匹配
			result=re.search(pattern,html)#使用search方法找到内容， 因为只有一个，不需要使用find_all的方法
			patternNum=re.compile('pn=(\d+)')#对于获取到的数据进行重新查找，找到我们要的数字
			Num=re.search(patternNum,result.group(1))#只寻找一个元素，因此这里参数为1
			PageNum=int(Num.group(1))
			#self.my_log(1,TotalNum)
		except Exception as e:
			self.my_log(3,u'贴吧的帖子数量没有找到， 错误原因：%s' % e)
			return None
		finally:
			self.my_log(1,u'本贴吧总共有%s个帖子' % int(PageNum))
			return int(PageNum)
		
	#获取本贴吧总共有多少帖子，详细的
	def get_page_content(self,html):
		try:
			tiebaNumContent=[]
			#定义匹配规则，总共匹配三个元素
			pattern=re.compile('<div class="th_footer_l".*?<span.*?>(\d+)</span>.*?<span.*?>(\d+)</span>.*?class="red_text">(\d+).*?</div>',re.S)
			results=re.search(pattern,html)
			
			#参数为0的元素是正则匹配到的所有内容，1是第一个括号里面的内容，2是第二个括号里面的内容，3是第三个括号里面的内容
			#使用search方法，就用group的方式获取找到的元素
			tiebaTheme=results.group(1)
			tiebaNum=results.group(2)
			tiebaPeople=results.group(3)
			tiebaNumContent.append(tiebaTheme)
			tiebaNumContent.append(tiebaNum)
			tiebaNumContent.append(tiebaNumContent)
		except Exception as e:
			self.my_log(3,u'贴吧的帖子数量没有找到， 错误原因：%s' % e)
			return None
		finally:
			self.my_log(1,u'本贴吧共有主题数:%s, 帖子数:%s, %s 人在本贴吧发布内容' % (tiebaTheme,tiebaNum,tiebaPeople) )
			self.tiezi_file.write(u'本贴吧共有主题数:%s, 帖子数:%s, %s 人在本贴吧发布内容\n' % (tiebaTheme,tiebaNum,tiebaPeople))
			return tiebaNumContent
 
	#根据页面num依次获取每一个页面的帖子内容
	def getAll_tiezi_list(self,PageNum):
		if PageNum < 51:
			self.my_log(1,u'当前贴吧帖子数量不足一页内容')
			return None
		#for num in range(50,PageNum+1,50):
		#for num in range(50,500,50):
		for num in range(50,50,50):
			current_url=self.tiebaUrl+"&ie=utf-8&pn="+str(num)
			target_Content=self.get_Single_Title_And_Url(current_url)
			
		
	#获取单页内容
	def get_Single_Title_And_Url(self,url):
		#定义存贮变量
		info=[]
		html=self.get_html(url)
		if not html:
			self.log(3,u'页面%s内容获取失败，跳过' % url)
			return None
		try:
			#创建正则匹配模板 #pattern=re.compile('<li class=" j_thread_list clearfix".*?<span class="threadlist_rep_num center_text".*?>(.*?)</span>.*?<a href=(.*?)title=(.*?)target=.*?class="frs-author-name j_user_card".*?>(.*?)</a>.*?class="pull-right is_show_create_time".*?>(.*?)</span>.*?</li>',re.S)
			#匹配整个页面的列表内容
			pattern=re.compile('<li class=" j_thread_list clearfix".*?</li>',re.S)
			tiezi_Contents=re.findall(pattern,html)
			#调试log
			self.my_log(1,'当前页面%s 找到了%d 个帖子' % (url,len(tiezi_Contents)))
				
			#匹配回帖人数，帖子标题，帖子地址
			replyNum_tirle_url_pattern=re.compile('<span class="threadlist_rep_num center_text".*?>(.*?)</span>.*?<a href="(.*?)" title="(.*?)" target=',re.S)
			#匹配创建人，创建时间
			author_creattime_Pattern=re.compile('<span class="frs-author-name-wrap".*?target="_blank">(.*?)</a>.*?class="pull-right is_show_create_time".*?>(.*?)</span>',re.S)
			
			for item in tiezi_Contents:
				tmp={}#临时变量
				replyNum_tirle_url=re.search(replyNum_tirle_url_pattern,item)
				author_creattime=re.search(author_creattime_Pattern,item)
				
				replyNum_Tmp=replyNum_tirle_url.group(1)#回复人数
				tieziNum=str(replyNum_tirle_url.group(2))[-10:]#截取帖子编号
				ttieziUrl_Tmp='http://tieba.baidu.com'+replyNum_tirle_url.group(2)#帖子地址
				tieziTitle_Tmp=replyNum_tirle_url.group(3)#帖子标题
				
				author_Tmp=author_creattime.group(1)#创贴人
				creat_time_Tmp=author_creattime.group(2)#建贴时间
						
				self.my_log(1,u"发帖人:%s|发帖时间:%s|帖子题目%s|帖子地址%s|跟帖人数%s|帖子编号:%s" % (author_Tmp,creat_time_Tmp,tieziTitle_Tmp,ttieziUrl_Tmp,replyNum_Tmp,tieziNum))
				#将获取到的数据写入文件中
				self.tiezi_file.write(u"发帖人:%s|发帖时间:%s|帖子题目%s|帖子地址%s|跟帖人数%s|帖子编号:%s\n" % (author_Tmp,creat_time_Tmp,tieziTitle_Tmp,ttieziUrl_Tmp,replyNum_Tmp,tieziNum))
				tmp['replyNum']=replyNum_Tmp
				tmp['tieziNum']=tieziNum
				tmp['tieziUrl']=ttieziUrl_Tmp
				tmp['tieziTitle']=tieziTitle_Tmp.strip()
				tmp['author']=author_Tmp.encode('utf-8')
				tmp['creat_time']=creat_time_Tmp
				info.append(tmp)
				#回帖数小于10的数据，暂时抛弃
				if int(replyNum_Tmp) > 10:
					self.info_list.append(tmp)
				
			self.my_log( 1,"数据匹配之后还有%d个帖子" % len(info))
		except Exception as e:
			self.my_log(2,u'匹配数据异常,跳过,错误原因：%s' % e)
			return None
		finally:
			self.my_log(1,u'当前页面 %s 数据查找完毕' % url )
			return info
		
	#获取每一个帖子的页码数目，因为	之前已经过滤过一次了，因此这里不需要重新过滤那些回帖数很少的情况
	def get_each_tiezi_content(self):
		tmp_test_url=[]#中间变量
		tiezi_count=len(self.info_list)#遍历次数
		for i in range(tiezi_count):
			#tmp_single_info_list=random.choice(self.info_list)#随机选择一个url
			tmp_single_info_list=self.info_list[i]
			#?see_lz=  它后面的值决定了是否只看楼主信息
			tiezi_url= tmp_single_info_list['tieziUrl']+'?see_lz=0&pn=1'#重新组合要访问的帖子的地址
			tiezi_num=1
			try:
				html=self.get_html(tiezi_url)
				tiezi_num=self.get_tiezi_Page_Num(html)#获取帖子的页码数目
			except Exception as e:
				self.my_log(2,u'get_each_tiezi_content() 匹配数据异常,跳过,错误原因：%s' % e)
				tmp_single_info_list['tiezi_page_num']=tiezi_num#将得到的帖子页数重新加到数据中去
				tmp_test_url.append(tiezi_url)#收集异常地址
			finally:
				tmp_single_info_list['tiezi_page_num']=tiezi_num#将得到的帖子页数重新加到数据中去
				tmp_single_info_list['tieziUrl']=tiezi_url#将得到的帖子页数重新加到数据中去
				
				self.info_list[i]=tmp_single_info_list
				#for a,b in self.info_list[i].items():#一种遍历字典的方法，这里是测试是否将数据添加成功
				#	print a,b						  #
				self.my_log( 1,u'%s|%s|当前帖子的页数：%s' % (sys._getframe().f_lineno,sys._getframe().f_code.co_name,str(tiezi_num)))
				#del self.info_list[0]
				
		self.my_log(1,'异常的url 有：%d' % len(tmp_test_url))
 
		
	#获取一个帖子总共有多少页
	def get_tiezi_Page_Num(self,page):
		if not page:
			self.my_log(3,u'页面%s内容获取失败，跳过')
			return None
		try:
			pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)#匹配页码规则
			result=re.search(pattern,page)
		except Exception as e:
			self.my_log(2,u'查找帖子页面数目异常,跳过,错误原因：%s' % e)
		finally:
			if result:
				return result.group(1).strip()
			else:
				return None
			
			
	def mutil_thread(self):	
		#帖子的内容过多，这里仅仅开启三个线程，来爬取三个帖子的内容
		for i in range(3):
			tmp_single_info_list=random.choice(self.info_list)#随机选择一个地址
			p=threading.Thread(target=self.loop_for_every_tiezi, args=(tmp_single_info_list,))
			p.start()
			time.sleep(3)
			p.join()
		
		#tmp_single_info_list=random.choice(self.info_list)#随机选择一个地址
		#self.loop_for_every_tiezi(tmp_single_info_list)
		
		
	def loop_for_every_tiezi(self,tmp_single_info_list):
		#self.my_log(1,u'thread %s is running...' % threading.current_thread().name)
		
		#tmp_single_info_list=random.choice(self.info_list)#随机选择一个地址
		page_num=tmp_single_info_list['tiezi_page_num']
		page_url_base=tmp_single_info_list['tieziUrl'][:-1]#对地址做一个处理
		tiezi_num=tmp_single_info_list['tieziNum']
		
		path=self.keyword+'/'+tiezi_num
		self.create_dir(path)#使用帖子的地址创建文件夹
		
		tiezi_file_path=path+'/'+tiezi_num+'.txt'#创建文件，记录本贴子所有回复内容
		tiezi_file_symbol=open(tiezi_file_path,'w')
		
		for num in range(1,int(page_num)+1):
			current_url=page_url_base+str(num)#重新组装地址
			current_tiezi_html=self.get_html(current_url)#获取当前帖子页面内容
			self.get_every_tiezi_content(current_tiezi_html,num,tiezi_file_symbol)
		tiezi_file_symbol.close()
		
	#根据每一页帖子的内容，匹配每一个楼层的内容	
	def get_every_tiezi_content(self,html,num,tiezi_file_symbol):
	#采用函数嵌套，先定义两个内部函数，然后再做处理
		#只获取首楼信息		
		def get_every_tiezi_first_floor_content(html):
			try:
				#首楼匹配规则
				first_floor_pattern = re.compile(r'<div class="l_post j_l_post l_post_bright noborder ".*?<div class="clear"></div>.*?</div>',re.S)
				item=re.search(first_floor_pattern,html)
				tmp_content=item.group(0)
				#获取回贴人的楼层，回复时间，回复人，内容
				author_content_floor_time_pattern=re.compile(r'data-field=.*?"date":"(.*?)".*?post_no":(\d+),.*?comment_num":(\d+),.*?>.*?<li class="d_name".*?target="_blank">(.*?)</a>.*?<div id="post_content_.*?>(.*?)</div>',re.S)
				
				items=re.search(author_content_floor_time_pattern,tmp_content)
				tmp={}
				floor_reply_time = items.group(1).strip()
				floor_post_num= items.group(2)
				floor_comment_num = items.group(3)
				floor_author = items.group(4)
				floor_reply_content =items.group(5)
				
				tmp['floor_reply_time']=floor_reply_time
				tmp['floor_post_num']=floor_post_num
				tmp['floor_comment_num']=floor_comment_num
				tmp['floor_author']=floor_author
				tmp['floor_reply_content']=floor_reply_content#回复内容还需要重新做处理，因此暂时没有记录到文件中去
				
				self.tiezi_info_list.append(tmp)
								
				self.my_log(1, u'%s楼| 回复人：%s|回复时间：%s|本楼层回复数：%s ' % (floor_post_num,floor_author,floor_reply_time,floor_comment_num))
				tiezi_file_symbol.write(u'%s楼|回复人：%s|回复时间：%s|本楼层回复数：%s\n' % (floor_post_num,floor_author,floor_reply_time,floor_comment_num))
				
				save_tiezi_content(floor_reply_content,tiezi_file_symbol)
				
			except Exception as e:
				self.my_log(2,u'匹配首楼内容失败,跳过,错误原因：%s' % e)
							
		
		#获取不包含首楼的其他楼层内容		
		def get_every_tiezi_not_first_floor_content(html):
			try:
				other_floor_pattern=re.compile('<div class="l_post j_l_post l_post_bright  ".*?<div class="clear"></div>.*?</div>',re.S)
				items=re.findall(other_floor_pattern,html)
			except Exception as e:
				self.my_log(2,u'匹配其他楼层内容失败,跳过,错误原因：%s' % e)
			finally:
				self.my_log(0,u'不在首页，找到%s 个回帖' % len(items) )
				reply_num= len(items)
				try:
					author_content_floor_time_pattern=re.compile(r'data-field=.*?"date":"(.*?)".*?post_no":(\d+),.*?comment_num":(\d+),.*?>.*?<li class="d_name".*?target="_blank">(.*?)</a>.*?<div id="post_content_.*?>(.*?)</div>',re.S)
					for floor_content in items:
						item=re.search(author_content_floor_time_pattern,floor_content)
						tmp={}
						floor_reply_time = item.group(1).strip()
						floor_post_num= item.group(2)
						floor_comment_num = item.group(3)
						floor_author = item.group(4)
						floor_reply_content =item.group(5)
												
						tmp['floor_reply_time']=floor_reply_time
						tmp['floor_post_num']=floor_post_num
						tmp['floor_comment_num']=floor_comment_num
						tmp['floor_author']=floor_author
						tmp['floor_reply_content']=floor_reply_content#回复内容还需要重新做处理，因此暂时没有记录到文件中去
						self.tiezi_info_list.append(tmp)
						
						self.my_log(1, u'%s楼| 回复人：%s|回复时间：%s|本楼层回复数：%s ' % (floor_post_num,floor_author,floor_reply_time,floor_comment_num))
						tiezi_file_symbol.write(u'%s楼|回复人：%s|回复时间：%s|本楼层回复数：%s\n' % (floor_post_num,floor_author,floor_reply_time,floor_comment_num))
						save_tiezi_content(floor_reply_content,tiezi_file_symbol)
				except Exception as e:
					self.my_log(2,u'匹配其他楼层，查找回复内容时失败,跳过,错误原因：%s' % e)
					
		def save_tiezi_content(floor_reply_content,tiezi_file_symbol):
			floor_reply_content=self.tool.replace(floor_reply_content)
			floor_reply_content=self.tool.replaceSlash(floor_reply_content)
			tiezi_file_symbol.write(floor_reply_content)
			temp_data=u'\n**********************分割符*************************\n'
			tiezi_file_symbol.write(temp_data)
			
		if not html:
			self.my_log(3,u'页面%s内容获取失败，跳过')
			return None
 
		#首楼层和其他楼层内容不同， 而首楼层只在帖子的第一页出现
		if num == 1:
			get_every_tiezi_first_floor_content(html)
			get_every_tiezi_not_first_floor_content(html)
		else:
			get_every_tiezi_not_first_floor_content(html)
 
	def run(self):
		
		self.my_log(1,u'start crawl...')
		
		#step1  获取贴吧入口网页内容
		tieba_html = self.get_html(self.tiebaUrl)
 
		#step2  查询本贴吧总共多少页内容
		Page_Num=self.get_Total_Num(tieba_html)
		tieba_Num_Content=self.get_page_content(tieba_html)
		
		#setp3 获取单页内容
		self.get_Single_Title_And_Url(self.tiebaUrl)
		
		#step4 根据PageNum 获取所有帖子的内容
		self.getAll_tiezi_list(Page_Num)
		self.my_log(1,u'total length is %d' % len(self.info_list))
		
		#step 5  遍历每一个帖子， 获取其页码数
		self.get_each_tiezi_content()
		self.my_log(1,u'Start mutil thread to crawl...' )
		time.sleep(3)
		self.mutil_thread()
		#step 6 获取每一个帖子所有的内容
		#self.loop_for_every_tiezi()
		
		
		
		self.my_log(1,u'total length is %d' % len(self.info_list))
		self.my_log(1,u'End crawl')
		#关闭文件描述符
		self.tiezi_file.close()
		
		#测试函数
	def test(self):
		url='http://tieba.baidu.com/p/5062576866?see_lz=0&pn=1'
		html=self.get_html(url)
		self.get_every_tiezi_content(html,1,'5062576866')	
if __name__ == '__main__':
	print( '''
			***************************************** 
			**    Welcome to Spider of baidutieba  ** 
			**      Created on 2017-04-25          ** 
			**      @author: Jimy _Fengqi          ** 
			*****************************************
	''')
	keyword=input(u'请输入要获取的贴吧名字：')
	if not keyword:
		keyword='python'
    
	print('将要获取%s 贴吧的内容' % keyword)
	#GetBaiduTieba(keyword).test()
	GetBaiduTieba(keyword).run()
	#mytieba=GetBaiduTieba(keyword)
