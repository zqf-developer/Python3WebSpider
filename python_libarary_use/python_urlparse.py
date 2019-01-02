from urllib.parse import urlparse, urlunparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(type(result), result)
# print(result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
print(result.path, result[2], result.params, result[3], sep='\n')
print(result.query, result[4], sep='\n')

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

