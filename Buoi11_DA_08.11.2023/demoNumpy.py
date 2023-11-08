import numpy as np

# mang 1D
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Mang 2D
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Mang 3D
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                 [[9, 10, 11, 12], [13, 14, 15, 16]],
                 [[17, 18, 19, 20],[21, 22, 23, 24]]])

print(arr3)

# Zero
arr_zero = np.zeros((3, 4))


# One
arr_one = np.ones((2, 3, 4))
print(arr_one)

arr_one_float = np.ones((2, 3, 4), dtype=float)
print(arr_one_float)

# arange
arr_arange = np.arange(1, 7, 2)
print(arr_arange)

# full
arr_full = np.full((2, 3), 8)
print(arr_full)

# eye
arr_eye = np.eye(4, dtype=int)
print(arr_eye)

# random
arr_random = np.random.random((2,3))
print(arr_random)

# ARRAY INFORMATON ==> type, size, shape, so chieu
print(arr_eye.dtype)
print(arr_random.dtype)

print(arr_eye.shape)
print(arr_random.shape)

print(arr_eye.size)
print(arr_random.size)

print(arr_eye.ndim)
print(arr_random.ndim)

# ARRAY INDEXING
print(arr_random[0, 1])

print(arr2)
print(arr2[:2, 1:3])
print(arr2[1,:])
print(arr2[1:2,:])
print(arr2[:,1:2])
print("---------\n")
print(arr2[arr2>4])

# ARRAY MATH
x = np.array([[1, 2],[3, 4]], dtype=np.float64)
y = np.array([[5, 6],[7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))

print("---------\n")
print(x - y)
print(np.subtract(x, y))

print("---------\n")
print(x * y)
print(np.multiply(x, y))

print("---------\n")
print(x / y)
print(np.divide(x, y))

# Khai can
print("---------\n")
print(np.sqrt(x))

print("---------\n")
print(x)
print(y)
print(x.dot(y))
# print(np.dot(x,y))

# sum
print(x.sum())
print(np.sum(x))
print(x.sum(axis=0))
print(x.sum(axis=1))

#Max
print(x.max())
print(x.max(axis=0))
print(x.max(axis=1))

print(np.min(x))
print(np.min(x, axis=0))
print(np.min(x, axis=1))

# MEAN ==>Tinh trung binh
print(x.mean())
print(x.mean(axis=0))
print(x.mean(axis=1))

# MEDIAN ==> Trung vi
print(np.median(x))
print(np.median(x, axis=0))
print(np.median(x, axis=1))

# Nghich dao Ma tran
print(x.T)

t = np.array([[10, 2, 50],
              [-3, 0, 9],
              [11, 6, -20]], dtype=np.int16)

print(np.abs(t))

# Concat
print("---------\n")
print(np.concatenate([x, y], axis=0))
print("---------\n")
print(np.concatenate([x, y], axis=1))

# split 
print("---------\n")
h = np.array([10, 2, 50, -3, 0, 9, 11, 6], dtype=np.int64)
print(np.split(h, [2, 5]))

#  Sort
print(np.sort(h, axis=0))

# Count
print(np.count_nonzero(h))
print(np.count_nonzero(h > 3))
