import numpy as np

#(0)
def least_sq_regression(x,y):


    x_bar = np.mean(x)
    y_bar = np.mean(y)
    b1 = 0
    b2 = 0
    size = len(x)
    size2 = len(y) #might not need this

    for i in range(0, size-1):
        b1 += ((x[i]-x_bar)*(y[i]-y_bar))
        b2 += ((x[i]-x_bar)**2)

    b1_hat = b1/b2
    b0_hat = y_bar - (b1_hat*x_bar)

    return b0_hat, b1_hat

#1


np.random.seed(37)


#2
tmp1 = np.zeros(5000)
#(a)
x = np.random.randn(1000)
#(b)
e = np.random.randn(1000)
#(c)
y = 0.5 + (1.8*x) + e
#(d)
least_sq_regression(x, y)
#(e)
tmp1 = b1_hat

#3
temp_mean = np.mean(tmp1)
#It is similar but not exact

#4
tmp1 = np.zeros(5000)
x = np.random.randn(1000)
e = np.random.randn(1000)
y = (-.5) + e
least_sq_regression(x, y)
#They are still similar but relatively off

#5
print(np.mean(tmp1))
#It is further away due to a minimized MLE estimate
