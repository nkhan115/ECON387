import numpy as np

#0
a = np.array([1, 2, 3, 1])
a = np.asmatrix(a)

b = np.array([[1, 0, 1, 5]]).T
b = np.asmatrix(b)

A = np.array([[1, 3, 5], [2, 4, 6], [7, 9, 11]])
A = np.asmatrix(A)

B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = np.asmatrix(B)

#1
x = np.array([[1, 3], [2, 4]])
y = np.array([[1, 0], [0, 1]])
z = np.array([[x, x], [y, y]])

#2
a @ a.T
np.add(b, a.T)
A @ A.T
A**3
A @ B

#3
A = np.random.randn(10, 5)
B = np.random.randn(5, 10)
C = A @ B
np.fill_diagonal(C, 1)

#4
D = np.tile(A, (2, 3))
E = np.tile(B, (3, 2))
F = D @ E
F[F <= 0.5] = 0

#5
np.reshape(D, (3, 10, 10))
np.reshape(E, (3, 10, 10))

#6
x = np.arange(100.0)
np.reshape(x, (10, 10))
np.reshape(x, (20, 5))
np.reshape(x, (10, 10, 1))

#7
x = np.reshape(np.arange(100.0), (5, 20))
x_1 = x.ravel()
x_2 = x.flatten()
x.flat

#8
x = np.array([[16, 10], [13, 11]])
y = 5
z = np.array([[16, 10], [13, 11], [12, 33]])

z_prime = z.T
Y = np.tile(y, (1, 3))
Y_1 = np.vstack((Y, Y))
m = np.hstack((np.vstack((x, z)), np.vstack((Y_1, np.vstack((z_prime, Y))))))

m_shape = np.shape(m)
m_dim = np.ndim(m)
print(m_shape)
print(m_dim)

#9
np.diag(np.diag(m))
np.linalg.eig(m)
np.linalg.matrix_rank(m)
np.linalg.det(m)
m_inverse = np.linalg.inv(m)
np.dot(m, m_inverse)
np.trace(m)