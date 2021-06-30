#Problem Set 3
#Nasif Khan

#Consider the code
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(37)
plt.style.use('ggplot')
T = 200
alpha1 = 0.8
alpha2 = 0.15
u = np.random.randn(T)
y = np.zeros(T)
for t in range(1, T):
    y[t] = alpha1*y[t-1] + alpha2*y[t-2] + u[t]
y = y[100:] # keep the last 100 periods

#(0)
#The loop starts from index one since our data is a time period, starting at 0 wouldn't make sense.
t=1
while t<=100:
    y[t]= alpha1*y[t-1] + alpha2*y[t-2] + u[t]
    t+= 1

y = y[100: ]
print(y)
print(len(y))

#(1)
x = np.arange(15)
odd = [] # empty list for odd numbers
even = [] # empty list for even numbers

for num in x:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

#(2)
from string import ascii_lowercase
letters = set(ascii_lowercase)
vowel = set()
consonant = set()

for let in letters:
    if let in ('a', 'e', 'i', 'o', 'u'):
        vowel.add(i)
    else:
        constant.add(i)

#(3)
x = np.linspace(0, 10, 100)
sinx = np.sin(x)
cosx = np.cos(x)
plt.plot(x, sinx,linestyle = 'solid',  label = 'sinx')
plt.plot(x , cosx , linestyle = 'dashed', color="b", label = 'cosx')
plt.title('sine and cosine functions')
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')

#(4)
x = np.linspace(0, 10, 100)
sinx = np.sin(x)
cosx = np.cos(x)
plt.plot(x , sinx, color = '5', linestyle = "None" , markeredgecolor = "black", markersize = 5, label = 'sinx')
plt.plot(x , cosx, color ="5",linestyle = "None" , markeredgecolor = "black", markersize = 5, label = 'cosx')
plt.title('sine and cosine functions')
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')

#(5)
x = ['Python','Java', 'Javascript', 'C#','C','PHP','R','Obj-C','Swift','Matlab','Kotlin','Typescript','Go','VBA','Ruby']
y = [30.17, 17.18, 8.21, 6.76, 6.71, 6.13, 3.81, 3.56, 1.82, 1.8, 1.76, 1.74, 1.34, 1.22, 1.13]
plt.barh(x,y, color = 'm')
plt.gca().invert_yaxis()
plt.title('PYPL Popularity of Programming Languages')
plt.xlabel('Share Percents')

#(6)
x = ['Python','Java', 'Javascript', 'C#','C','PHP','R','Obj-C','Swift','Matlab','Kotlin','Typescript','Go','VBA','Ruby']
y = [30.17, 17.18, 8.21, 6.76, 6.71, 6.13, 3.81, 3.56, 1.82, 1.8, 1.76, 1.74, 1.34, 1.22, 1.13]
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=x, autopct='%1.1f%%', counterclock=False,startangle=-200)
plt.title('PYPL Popularity of Programming Languages')
