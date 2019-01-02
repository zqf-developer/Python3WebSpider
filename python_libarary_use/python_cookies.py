import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# 以上注释的代码是获取cookie值

# 下面两段代码保存为TXT文件
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
# 下面是通用的代码块
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# 需要懂点网站开发才可以知道取哪里的数据，否则很难弄懂 这里的bing的网站并不是www.bing.com,
# 而是https://cn.bing.com
response = opener.open('https://cn.bing.com')

# 显示cookie的所有内容
# for item in cookie:
#     print(item.name+"="+item.value)

# 保存cookie内容
cookie.save(ignore_discard=True, ignore_expires=True)
