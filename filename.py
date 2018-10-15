urls=["http://www.google.com/a.txt",
"http://www.google.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"http://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png"]

L=[]
for i in urls:
	a=i.split('/')[-1]#以/將網址分割，並取出最後的檔名
	L.append(a)#將每次取出的檔名放入列表中
#print(L)
a=0#a.txt的次數
b=0#b.txt的次數
c=0#c.jpg的次數
for i in L:
	if i=='a.txt':
		a+=1
	elif i =='b.txt':
		b+=1
	elif i =='c.jpg':
		c+=1
print("a.txt:",a)
print("b.txt:",b)
print("c.txt:",c)


