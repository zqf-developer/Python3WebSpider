import urllib.request
import urllib.parse
import urllib.error
import socket

'''
爬取网页内容
'''
# 模拟请求提交表单
data = bytes(urllib.parse.urlencode({'word': 'hi'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# timeout参数
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

