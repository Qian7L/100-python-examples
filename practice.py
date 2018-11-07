# -*- coding: utf-8 -*-
#案例实战
#1.有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
for i in range(1,5):
    for k in range(1,5):
        for j in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(i,k,j)

#2.企业发放的奖金根据利润提成
i=int(input("输入利润"))
if i <= 10:
    m=0.1*i
elif i <= 20:
    m=10*0.1+(i-10)*0.075
elif i <= 40:
    m=10*0.1+10*0.075*(i-20)*0.05
elif i <= 60:
    m=10*0.1+10*0.075+20*0.05+(i-40)*0.03
elif i <= 100:
    m=10*0.1+10*0.075+20*0.05+20*0.03+(i-60)*0.015
else:
    m=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(i-100)*0.01
print(m)

#3.输入某年某月某日，判断这一天是这一年的第几天？
i=input('请输入日期，例如20181029')
month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
year=int(i[:4])
month=int(i[4:6])
day=int(i[6:8])
#d=sum(month_day[:month-1],day)
d=0
for i in range(month-1):
    d=d+int(month_day[i])
if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
    if month>2:
        d=d+1
print('是第{0}天'.format(d+day))

#4.输入三个整数x,y,z，请把这三个数由小到大输出
x=int(input('输入x'))
y=int(input('输入y'))
z=int(input('输入z'))
d=sort(x,y,z)
print(d[0],d[1],d[2])

#5.将一个列表的数据复制到另一个列表中
a1=[1,2,3]
a2=[4,5,6]
print(a1+a2)

#6.输出9*9乘法口诀表
for i in range(1,10):
    for j in range(1,10):
        print('{0}*{1}={2}'.format(i,j,i*j),end=' ')
    print('\n')

#7.暂停一秒输出
import time
d = {"a":1,"b":2}
for i in d:
 print i
 time.sleep(1) #暂停一秒输出

#8.暂停一秒输出，并格式化当前时间
import time
print（time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))）
time.sleep(1)
print（time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))）

#9.斐波那契数列
def fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    fibs=[0,1]
    for i in range(2,n):
        fibs.append(fibs[i-2]+fibs[i-1])
    return fibs
print(fib(10))

#10.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#f(n)=f(n-1)+f(n-2),恰好为斐波那契数列
f1=1
f2=1
for i in range(1,21):
    print(f1,f2,end=' ')
    if (i % 3) == 0:
        print ('')
    f1 = f1 + f2
    f2 = f1 + f2

#11.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def equ(n):
    import math
    a = math.sqrt(n)
    if int(a) == a:
        return 1


for i in range(-100,10000):
    if equ(i + 100) == 1 and equ(i + 268) == 1:
        print(i)

#12.判断101-200之间有多少个素数，并输出所有素数
import math
k=0
m=[]
for i in range(101,201):
    n=0
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            break
        n=n+1
    if n == int(math.sqrt(i))-1:
        k=k+1
        m.append(i)
print(m)
print(k)

#13.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
for i in range(100,1000):
    a=i // 100
    b=(i // 10) % 10
    c=i % 10
    if (a ** 3 + b ** 3 + c ** 3) == i:
        print(i)

#14.将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def su(n):
    import math
    b=0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            b=b+1
            break
    if b == 0:
        return 1

t=1
q=0
i=int(input("输入一个数"))
print('{}='.format(i),end='')
for h in range(1,10):
    for j in range(2,int(i/t)):
        if i % j == 0:
            print('{}*'.format(j),end='')
            t=j
            i=i/t
            break
    if su(i) == 1:
        print(int(i))
        break

#15.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
a=int(input('请输入成绩'))
if a >= 90:
    grade='A'
elif (a > 60) and (a < 90):
    grade='B'
else:
    grade='C'
print('{}分为{}'.format(a,grade))

#16.输出指定格式的日期
import datetime
if __name__ == '__main__':
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))
 # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
# 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
# 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))

#17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
import string
alpha=0
digit=0
space=0
others=0
a=input('请输入字符')
for i in range(0,len(a)):
    m=a[i]
    if m.isalpha():
        alpha += 1
    elif m.isdigit():
        digit += 1
    elif m.isspace():
        space += 1
    else:
        others += 1
print(alpha,digit,space,others)

#18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
a=int(input('请输入a'))
n=int(input('请输入n'))
m=[a]
b=a
for i in range(1,n):
    b=10*b+a
    m.append(b)
print(sum(m))
print(m)

#19.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
for i in range(2,1001):
    m=0
    for j in range(1,i):
        if i % j == 0:
            m = m+j
    if m == i:
        print(i)

#20.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
h=100
l=0
for i in range(1,11):
    l=l+h+h/2
    h=h/2
l=l-h
print(h,l)

#21.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
x1=1
for i in range(9):
    x1=(x1+1)*2
print(x1)

#22.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
for a in ['x','y','z']:
    for b in ['x','y','z']:
        for c in ['x','y','z']:
            if (a != b) and (a != c) and (b != c) and (a != 'x') and (c != 'x') and (c != 'z'):
                print(a,b,c)

#23.打印出如下图案（菱形）
for i in range(1,5):
    print(' ' * (4-i),'*' * (2*i-1),' ' * (4-i))
for i in range(3,0,-1):
    print(' ' * (4-i),'*' * (2*i-1),' ' * (4-i))

#24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
def qiuhe(n):
    a=1
    b=2
    s=0
    for i in range(n):
        s=s+b/a
        a,b=b,a+b
    print(s)

qiuhe(20)

#25.求1+2!+3!+...+20!的和
def qiuhe(n):
    h=0
    for i in range(1,n+1):
        k=1
        for j in range(1,i+1):
            k=k*j
        h=h+k
    print(h)

qiuhe(20)

#26.利用递归方法求5!
def jiecheng(n):
    s=0
    if n == 1:
        s = 1
    else:
        s = n * jiecheng(n-1)
    return s                    #这里要用return，因为递归要用到这里的数值，用return返回int，而print不会，会报错
print(jiecheng(5))

#27.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
def digui(s,l):
    if l==0:
        return
    print(s[l-1])
    digui(s,l-1)

a=input('请输入字符')
l=len(a)
digui(a,l)

#28.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
def age(n):
    if n==1:
        a=10
    else:
        a=age(n-1)+2
    return a
print(age(5))

#29.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
s=int(input('输入数字'))
a=s//10000
b=s%10000//1000
c=s%1000//100
d=s%100//10
e=s%10
if a!=0:
    print('5位数',e,d,c,b,a)
elif b!=0:
    print('4位数',e,d,c,b)
elif c!=0:
    print('3位数',e,d,c)
elif d!=0:
    print('2位数',e,d)
else:
    print('1位数',e)

#30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
s=input('输入数字')
flag=1
for i in range(int(len(s)/2)):
    if s[i]!=s[len(s)-i-1]:
        flag=0
if flag==1:
    print('是回文数')
else:
    print('不是回文数')

#31.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
letter = input("please input:")
# while letter  != 'Y':
if letter == 'S':
    print('please input second letter:')
    letter = input("please input:")
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data error')

elif letter == 'F':
    print('Friday')

elif letter == 'M':
    print('Monday')

elif letter == 'T':
    print('please input second letter')
    letter = input("please input:")

    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')

elif letter == 'W':
    print('Wednesday')
else:
    print('data error')

#32.按相反的顺序输出列表的值
a=['apple','banana','orange']
for i in a[::-1]:
    print(i)

#33.按逗号分隔列表
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1

#34.练习函数调用
def use():
    print('so is life')

def using():
    for i in range(3):
        use()

if __name__=='__main__':
    using()

#35.文本颜色设置
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

#36.求100之内的素数
def sushu(n):
    k=0
    for i in range(2,n):
        if n % i==0:
            k=k+1
    if k==0:
        print(n)

for i in range(2,101):
    sushu(i)

#37.对10个数进行排序
import random
m=[]
for i in range(10):
    m.append(random.randint(0,99))
for i in range(len(m)-1,0,-1):
    for j in range(i):
        if m[j]>m[j+1]:
            m[j],m[j+1]=m[j+1],m[j]
print(m)

#38.求一个3*3矩阵主对角线元素之和
import numpy as np
a=np.random.randint(1,100,size=(3,3))
print(a)
b=0
for i in range(3):
    b=b+a[i][i]
print(b)

#39.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
import numpy as np
c=np.random.randint(1,100,size=10)
a=list(c)
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

b=int(input('请输入一个数'))
m=0
for i in range(len(a)-1):
    if a[i]>b:
        a.append(0)
        m=i
        break
for j in range(len(a)-2,m-1,-1):
    a[j+1]=a[j]
    a[m]=b
print(a)

#40.将一个数组逆序输出
import numpy as np
c=np.random.randint(1,100,size=10)
print(c)
#a=list(c)
for i in range(int(len(c)/2)):
    c[i],c[len(c)-i-1]=c[len(c)-i-1],c[i]
print(c)

#41.模仿静态变量的用法
def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()
        # 类的属性
        # 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

print (Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()

#42.学习使用auto定义变量的用法
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()

#43.模仿静态变量(static)另一案例
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print ('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print ('The num = %d' % nNum)
        inst.inc()

#44.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
import numpy as np
a=np.random.randint(1,100,size=(3,3))
b=np.random.randint(1,100,size=(3,3))
c=np.random.randint(1,100,size=(3,3))
print(a,b)
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]+b[i][j]
print(c)

#45.统计 1 到 100 之和
print(sum(range(1,101)))

#46.求输入数字的平方，如果平方运算后小于 50 则退出
q=1
while q==1:
    a = int(input('请输入数字'))
    print('输入数字的平方为{}'.format(a * a))
    if a*a<50:
        q=0

#47.两个变量值互换
def exchange(a, b):
    print('第一个变量 = {}, 第二个变量 = {}'.format(a, b))
    a, b = b, a
    print('第一个变量 = {}, 第二个变量 = {}'.format(a, b))
if __name__ == '__main__':
    x = 1
    y = 8
    exchange(x, y)

#48.数字比较
def compare(a,b):
    if a>b:
        print('{}>{}'.format(a,b))
    elif a<b:
        print('{}<{}'.format(a,b))
    else:
        print('{}={}'.format(a,b))

a=int(input('请输入a'))
b=int(input('请输入b'))
compare(a,b)

#49.使用lambda来创建匿名函数
maxin=lambda x,y:(x>y)*x+(x<=y)*y
minin=lambda x,y:(x>y)*y+(x<=y)*x
if __name__ =='__main__':
    x=20
    y=30
    print(maxin(x,y))
    print(minin(x,y))

#50.输出一个随机数
import random
print(random.random())
#random.uniform
#random.randint

#51.学习使用按位与 &
if __name__ == '__main__':
    a = 7
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)   #换算为二进制，同一位上都是1运算结果才为1

#52.学习使用按位或 |
if __name__ == '__main__':
    a = 7
    b = a | 3
    print('a | b is %d' % b)
    b |= 15
    print ('a | b is %d' % b)   #同一位上只要有一个为1结果就为1

#53.学习使用按位异或 ^
if __name__ == '__main__':
    a = 7
    b = a ^ 3
    print('The a ^ 3 = %d' % b)
    b ^= 7
    print('The a ^ b = %d' % b)   #同一位上两者结果不同则为1

#54.取一个整数a从右端开始的4〜7位   #二进制的
if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print ('%o\t%o' %(a,d))

#55.学习使用按位取反~
a=147
b=~a
print(b)

#56.画图，学用circle画圆形
#用tkinter画
if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 5
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3
    mainloop()
#用turtle画
if __name__ == '__main__':
    import turtle
    turtle.title("画圆")
    turtle.setup(800,600,0,0)
    pen=turtle.Turtle()
    pen.color("yellow")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(1)
    pen.circle(100)
#用matplotlib画
import numpy as np
import matplotlib.pyplot as plt

x = y = np.arange(-11, 11, 0.1)
x, y = np.meshgrid(x,y)
#圆心为（0，0），半径为1-10
for i in range(1,11):
   plt.contour(x, y, x**2 + y**2, [i**2])
   #如果删除下句，得出的图形为椭圆
   plt.axis('scaled')
plt.show()

#57.画图，学用line画直线。
if __name__ =='__main__':
    from tkinter import *
    canvas=Canvas(width=500,height=500,bg='yellow')
    canvas.pack(expand=YES,fill=BOTH)
    x0=250
    x1=260
    y0=300
    y1=180
    for i in range(20):
        canvas.create_line(x0,y0,x1,y1)
        x0-=5
        x1+=5
        y0-=5
        y1+=5
    mainloop()
#用turtle
import turtle
def drawline(n):
    t=turtle.Pen()
    t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
    t.begin_fill()   #开始填充颜色
    for i in range(n): #任意边形
        t.forward(50)
        t.left(360/n)
    t.end_fill()    #结束填充颜色
drawline(4)

#58.画图，学用rectangle画方形
if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas( width=400, height=400, bg='yellow')
    canvas.pack()
    x0 = 100
    y0 = 100
    y1 = 300
    x1 = 300
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    mainloop()

#59.画图，综合例子
if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()

#60.计算字符串长度
a=input('请输入字符串')
print(len(a))

#61.打印出杨辉三角形（要求打印出10行如下图）
a=[]
for i in range(10):
    a.append([])
    for j in range(i+1):
        if j==0:
            a[i].append(1)
        elif j==i:
            a[i].append(1)
        else:
            a[i].append(a[i-1][j-1]+a[i-1][j])
for i in range(10):
    for j in range(i):
        print(a[i][j],end=' ')
    print('\n')

#62.查找字符串
a='sdgga0'
b='0'
print(a.find(b))

#63.画椭圆
if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(380, 250 , 310 , 220 , width=1)
    mainloop()

#64.利用ellipse 和 rectangle 画图
if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()

from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
ax.add_patch(ell1)

x, y = 0, 0
ax.plot(x, y, 'ro')

plt.axis('scaled')
# ax.set_xlim(-4, 4)
# ax.set_ylim(-4, 4)
plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

plt.show()

#65.一个最优美的图案
import math
from tkinter import *
class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []

def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter + int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()
if __name__ == '__main__':
    LineToDemo()

#66.输入3个数a,b,c，按大小顺序输出
import random
a=[]
for i in range(3):
    a.append(random.randint(10,50))
print(sorted(a))

#67.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
import numpy as np
c=np.random.randint(1,100,size=10)
print(c)
#a=list(c)
minin=c[0]
maxin=c[0]
max=0
min=0
for i in range(len(c)):
    if c[i]<minin:
        minin=c[i]
        min=i
    if c[i]>maxin:
        maxin=c[i]
        max=i
c[max],c[0]=c[0],c[max]
c[min],c[len(c)-1]=c[len(c)-1],c[min]
print(c)

#68.有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
def sort_(n,m):
    import numpy as np
    c=np.random.randint(1,100,size=n)
    d=np.random.randint(1,100,size=n)
    print(c)
    for i in range(m):
        d[i]=c[n-m+i]
    for i in range(n-m):
        d[m+i]=c[i]
    print(d)

sort_(15,5)

#69.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
def findit(n):
    m=[]
    for i in range(n):
        m.append(i+1)
    l=len(m)
    q=0
    while l>1:
        w=l % 3
        for i in range(len(m),0,-1):
            if (i+q) % 3==0:
                m.remove(m[i-1])
        l=len(m)
        q=q+w
    print(m)

findit(34)

#70.写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
if __name__=='__main__':
    a=input('输入字符串')
    print('{}的长度为{}'.format(a,len(a)))

#71.编写input()和output()函数输入，输出5个学生的数据记录
N = 3
student = []
for i in range(5):
    student.append(['', '', []])
print(student)

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))


def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0], stu[i][1]))
        for j in range(3):
            print('%-8d' % stu[i][2][j])


if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)

#72.创建一个链表
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)

#73.反向输出一个链表
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    for i in range(int(len(ptr)/2)):
        ptr[i],ptr[len(ptr)-1-i]=ptr[len(ptr)-1-i],ptr[i]
    print(ptr)

#74.列表排序及连接
if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()
    print(a)
    print(a + b)
    a.extend(b)
    print(a)

#75.放松一下，算一道简单的题目
if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3:
            print(64 + i)

#76.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def jishu(n):
    m=0
    for i in range(int((n+1)/2)):
        m=m+1/(2*i+1)
    return m

def oushu(n):
    m=0
    for i in range(int(n/2)):
        m=m+1/(2*i+2)
    return m

a=int(input('输入一个数'))
if a % 2 ==0:
    print(oushu(a))
else:
    print(jishu(a))

#77.循环输出列表
if __name__ == '__main__':
    s = ["man","woman","girl","boy","sister"]
    for i in range(len(s)):
        print(s[i])

#78.找到年龄最大的人，并输出。请找出程序中有什么问题
if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print('%s,%d' % (m, person[m]))

#79.字符串排序
l = []
for i in range(3):
    l.append(input("int something:"))
l.sort()
print(l)

#80.海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
num = int(input("输入猴子的数目:"))
def fn(n):
    if n == num:
        return (4 * x)  # 最后剩的桃子的数目
    else:
        return (fn(n + 1) * 5 / 4 + 1)

x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x = x + 1

#简洁版
if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while (i < 5) :
        x = 4 * j
        for i in range(0,5) :
            if(x%4 != 0) :
                break
            else :
                i += 1
            x = (x/4) * 5 +1
        j += 1
    print (x)

#81.809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果
i=1
while 1:
    if (809*i>1000) and (809*i<10000) and (8*i>10) and 8*i<100 and 9*i>100 and 9*i<1000:
        print(i,809*i)
        break
    else:
        i=i+1

#82.八进制转换为十进制
n=input('输入一个数')
m=0
for i in range(len(n)):
    m=m+(8 ** (len(n)-i-1)*int(n[i]))
print(m)

#83.求0—7所能组成的奇数个数
m=4
s=4
for i in range(2,9):
    if i==2:
        m*=7
    if i>2:
        m*=8
    s=s+m
print(s)

#84.连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

#85.输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
a=int(input('输入一个数'))
if a % 2 ==0:
    print('请输入一个奇数')
    a = int(input('输入一个数'))

b=9
while 1:
    c=b/a
    if int(c)==c:
        break
    else:
        b=b*10+9
print(b,c)

#86.两个字符串连接程序
a = "acegikm"
b = "bdfhjlnpq"
c = a + b
print(c)

#87.回答结果（结构体变量传递)
if __name__ == '__main__':
    class student:
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a= student()
    a.x = 3
    a.c = 'a'
    f(a)
    print (a.x,a.c)

#88.读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
for i in range(7):
    a=int(input('输入一个数'))
    if a >50 or a<1:
        print('错误输入')
        a = int(input('输入一个数'))
    print('*'*a)

#89.某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
a=input('请输入一个四位数的数')
m=[]
for i in range(4):
    m.append((int(a[i])+5)%10)
m[0],m[3]=m[3],m[0]
m[1],m[2]=m[2],m[1]
print("".join('%s' %s for s in m))

#90.列表使用实例
testList = [10086, '中国移动', [1, 2, 4, 5]]
print(len(testList))
print(testList[1:])
testList.append('i\'m new here!')
print(len(testList))
print(testList[-1])
print(testList.pop(1))
print(len(testList))
print(testList)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]
print(col2even)

#91.时间函数举例1
if __name__ == '__main__':
    import time
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))

#92.时间函数举例2
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
    print(end - start)

#93.时间函数举例3
if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print (i)
    end = time.clock()
    print ('different is %6.3f' % (end - start))

#94.时间函数举例4,一个猜数游戏，判断一个人反应快慢
if __name__ == '__main__':
    import time
    import random

    play_it = input('do you want to play it.(\'y\' or \'n\')')
    while play_it == 'y':
        c = input('input a character:\n')
        i = random.randint(0, 2 ** 32) % 100
        print('please input number you guess:\n')
        start = time.clock()
        a = time.time()
        guess = int(input('input your guess:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little bigger')
                guess = int(input('input your guess:\n'))
        end = time.clock()
        b = time.time()
        var = (end - start) / 18.2
        print(var)
        if var < 15:
            print('you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        print('Congradulations')
        print('The number you guess is %d' % i)
        play_it = input('do you want to play it.')

#95.字符串日期转换为易读的日期格式
from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)

#96.计算字符串中子串出现的次数
if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print(ncount)

#97.从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
if __name__ == '__main__':
    from sys import stdout
    filename = input('输入文件名:\n')
    fp = open(filename,"w")
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()

#98.键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print (fp.read())
    fp.close()

#99.有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
if __name__ == '__main__':
    import string
    fp = open('test1.txt')
    a = fp.read()
    fp.close()

    fp = open('test2.txt')
    b = fp.read()
    fp.close()

    fp = open('test3.txt', 'w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()

#100.列表转换为字典
i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))