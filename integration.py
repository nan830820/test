def anonymous(x):
	return x**2+1
def integrate(fun,start,end):
	step=0.1#每一塊矩形的寬度設為0.1
	intercept=start#將intercept設定為定積分的上界值
	area=0
	while intercept<end:
		intercept+=step
		#fun(intercept)*step為計算每一塊的面積，並累加到area中
		area=area+fun(intercept)*step
	return area

print(integrate(anonymous,0,10))