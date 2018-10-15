L=[]
for i in range(1000):
	if i%3==0 or i%5==0:#如果i為3或5的倍數
		L.append(i)#將i放入列表L中
print("3或5倍數的和(1000以內的數):",sum(L))



