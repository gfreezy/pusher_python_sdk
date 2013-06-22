#!/usr/bin/python
# _*_ coding: UTF-8 _*_

###
# 百度云推送PUSH服务 Python SDK
#
# 本文件提供百度云推动PUSH的Python版本SDK
#
# @author 百度云平台部
# @copyright Copyright (c) 2012-2020 百度在线网络技术(北京)有限公司
# @version 1.0.0
### 
'''
 @author: blacklaw
 @version: 1.1.0
 @email:	blacklaw00@gmail.com
 @date:	2013-06-08
 @description: 由于百度把pycurl给限制掉了，老版的不能用，现在改为urllib2实现 
'''

import urlparse
import StringIO
import urllib, urllib2

class RequestCore(object):
	"""封装curl，提供网络交互功能,组网络请求包，并保存返回结果"""
	#类常量
	HTTP_GET = 'GET'
	
	HTTP_POST = 'POST'

	HTTP_PUT = 'PUT'

	HTTP_DELETE = 'DELETE'

	HTTP_HEAD = 'HEAD'


	def __init__(self, url = None, proxy = None, helpers = None):		
		self.request_url = url
		self.method = RequestCore.HTTP_POST
		self.request_headers = dict()
		self.request_body = None
		self.response = None
		self.response_headers = None
		self.response_body = None
		self.response_code = None
		self.response_info = None
		self.curl_handle = None
		self.proxy = None
		self.username = None
		self.password = None
		self.curlopts = None
		self.debug_mode = False
		self.request_class = 'RequestCore'
		self.response_class = 'ResponseCore'
		self.useragent = 'RequestCore/1.4.2'
		if(isinstance(helpers, dict)):
			if(helpers.has_key() and helpers['request'] is not None):
				self.request_class = helpers['request']
			if(helpers.has_key() and helpers['response'] is not None):
				self.response_class = helpers['response']
		if(proxy is not None):
			self.set_proxy(proxy)
		
	def set_credentials(self, username, password):
		self.username = username
		self.password = password

	def add_header(self, key, value):
		self.request_headers[key] = value

	def remove_header(self, key):
		if(self.request_headers.has_key(key)):
			del self.request_headers[key]

	def set_method(self, method):
		self.method = method.upper()

	def set_useragent(self, ua):
		self.useragent = ua

	def set_body(self, body):
		self.request_body = body

	def set_request_url(self, url):
		self.request_url = url
	
	def set_curlopts(self, curlopts):
		self.curlopts = curlopts

	def set_proxy(self, proxy):
		self.proxy = urlparse.urlparse(proxy)
        
	'''
	bae 把pycurl 给取消了，我现在改成了urllib实现
	'''
	def handle_request(self):
		url = self.request_url
		headers = dict()
		headers['HTTP_REFERER'] = self.request_url
		request = urllib2.Request(url, self.request_body, headers)
		f = urllib2.urlopen(request)
		self.response_code = f.getcode()
		self.response_headers = f.info()
		self.response_body = f.read()
		
	'''
		以前使用的是Curl方法，baidu把它禁用了
	def handle_request_curl(self):
		print '\n\n',dir(self),'\n\n'
		curl_handle = pycurl.Curl()
		# set default options.
		url = 'http://127.0.0.1/gethead.php'
		curl_handle.setopt(pycurl.URL, url)#self.request_url)
		curl_handle.setopt(pycurl.REFERER, self.request_url)
		curl_handle.setopt(pycurl.USERAGENT, self.useragent)
		curl_handle.setopt(pycurl.TIMEOUT, 5184000)
		curl_handle.setopt(pycurl.CONNECTTIMEOUT, 120)
		curl_handle.setopt(pycurl.HEADER, True)
	#	curl_handle.setopt(pycurl.VERBOSE, 1)
		curl_handle.setopt(pycurl.FOLLOWLOCATION, 1)
		curl_handle.setopt(pycurl.MAXREDIRS, 5)
		if(self.request_headers and len(self.request_headers) > 0):
			tmplist = list()
			for(key, value) in self.request_headers.items():
				tmplist.append(key + ':' + value)
			print 'request keylist',dir(tmplist)
			curl_handle.setopt(pycurl.HTTPHEADER, tmplist)
		#目前只需支持POST
		curl_handle.setopt(pycurl.HTTPPROXYTUNNEL, 1)
		print '\n\n*************************\nrequest.body',self.request_body,'\n******************************\n'
		curl_handle.setopt(pycurl.POSTFIELDS, self.request_body)

		response = StringIO.StringIO()
		curl_handle.setopt(pycurl.WRITEFUNCTION, response.write)
		curl_handle.perform()

		self.response_code = curl_handle.getinfo(curl_handle.HTTP_CODE)
		header_size = curl_handle.getinfo(curl_handle.HEADER_SIZE)
		resp_str = response.getvalue()
		self.response_headers = resp_str[0 : header_size]
		self.response_body = resp_str[header_size : ]
		print self.response_body
		response.close()
		curl_handle.close()
	'''
	def get_response_header(self, header = None):
		if(header is not None):
			return self.response_headers[header]
		return self.response_headers

	def get_response_body(self):
		return self.response_body

	def get_response_code(self):
		return self.response_code


#
#	Container for all response-related methods 
#

class ResponseCore(object):
	
	def __init__(self, header, body, status = None):
		self.header = header
		self.body = body
		self.status = status

	def isOK(self, codes = None):
		if(codes == None):
			codes = [200, 201, 204, 206]
			return self.status in codes
		else:
			return self == codes



		

