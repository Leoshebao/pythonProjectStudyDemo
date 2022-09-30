b = int(input("请输入本金："))
r = float(input("请输入年利率："))
n = int(input("请输入年份："))
print("你的本金为","年利率为",r,",年份为",n,",你的收益为",round(b*(pow(1+r,n)),2))