Baidu Push 服务器端SDK Python版
==============
吃水不忘挖井人，该sdk是在@luvchh基础上修改核心http请求方式来的，98%的代码是@luvchh完成的
**第一版：**
由[@luvchh](http://weibo.com/luvchh) 提供，并开放在github上：
github地址：<https://github.com/Argger/pusher_python_sdk>
**第二版：**
由[@搞基宫陈尸](http://www.weibo.com/u/2255232584) 修改，
github地址:<https://github.com/blacklaw0/pusher_python_sdk>
**第三版：**
由 @gfreezy 修改，
github地址:<https://github.com/gfreezy/pusher_python_sdk>
- - -
Python SDK总体介绍：
将百度Push服务端的所有操作封装成一个类Channel，通过对该类的简单初始化，即可调用其内部的各种方法，使用百度Push服务。
Channel提供的方法和服务端API对应，是对服务端REST API的封装，REST API请参考:http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/api/list
使用前提:
支持pycurl的python版本

工具组成：
Python SDK工具包主要由以下部分组成：
*	channel.py -- Python_SDK 脚本，包含对外提供的所有接口
*	sample/sample.python -- 展示如何使用 Python_SDK 的 demo 文件

SDK 依赖于以下组件：
*	requests
*	python


一般规则
*	所有函数的参数和返回值中如果有中文，必须是UTF-8编码；
*	不需要对函数参数进行urlencode。
* 错误信息见 http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/api#JSON.E5.93.8D.E5.BA.94.E7.BC.96.E7.A0.81

---------------
HTTP状态错误
错误码	错误信息
>30600	Internal Server Error
>30601	Method Not Allowed
>30602	Request Params Not Valid
>30603	Authentication Failed
>30604	Quota Use Up Payment Required
>30605	Data Required Not Found
>30606	Request Time Expires Timeout
>30607	Channel Token Timeout
>30608	Bind Relation Not Found
>30609	Bind Number Too Many
>30610	Duplicate Operation
