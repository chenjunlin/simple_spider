if __name__ == '__main__':
	response = request.urlopen("http://www.cnblogs.com/peida/archive/2012/10/30/2745714.html")
#输入url

	html = response.read()
#必须要有read（）

	charset = chardet.detect(html)


#侦测网页编码
	print(charset)
#打印   
	html = html.decode(charset['encoding'])

	print(html)
