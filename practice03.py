name='赛文'
name='艾斯'
print(name)
#整数类型
x1=114
x2=514
x3=250.0
print(x1,type(x1))
print(x2,type(x2))
print(x3,type(x3))
#整数可调整十进制，二进制
print('十进制',114)
print('二进制',0b1101001)#0b开头
print('八进制',0o242)#0o开头
print('十六进制',0x1F1)#0x开头





#浮点类型(float)
a=1.14
print(a,type(a))
x1=1.1
x2=2.2
x3=3.3
print(x1+x2)
print(x1+x3)#出现误差为正常现象
print(x1+x2+x3)
print(x3-x1)
      #消除误差
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))





#布尔类型(bool)
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))

#布尔值可以转换成整数计算
print(f1+1)# 1+1=2   Ture表示1
print(f2+1)# 0+1=1   False表示0




#字符串类型
str1='是谁在绳索上滑行,me!'
str2="rabbit，tank！变身！"
str3='''一旦认清了自己的软弱
那我就是无敌da'''
str4="""假面骑士
zedddddd"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))




#类型转换-str()函数与int（）函数
str10='路人甲'
str20='jian'
a=True
b=11.4
print(int(a),int(b))
print(type(a),type(int(a)))
print(type(b),type(int(b)))




