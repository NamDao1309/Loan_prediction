import numpy as np

# Khoi tao mang 
# 1D
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

#2D
arr2 = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(arr2)

#3D
arr3 = np.array([[[1, 2, 3],[4, 5, 6]],
                 [[7, 8, 9],[10, 11, 12]],
                 [[13, 14, 15],[16, 17, 18]]
                 ])

print(arr3)

# Khơi tạo các mảng khác nhau
# zeros
arr_zero = np.zeros((3,4), dtype=float)
print(arr_zero)

# ones
arr_ones = np.ones((2, 3, 4), dtype=np.int64)
print(arr_ones)

# arrange
arr_arange = np.arange(1, 8, 2)
print(arr_arange)

# full
arr_full = np.full((2, 3), 5)
print(arr_full)

# eye
arr_eye = np.eye(4, dtype=float)
print(arr_eye)

# random
arr_random = np.random.random((2, 3))
print(arr_random)

# array information
#dtype
print(arr_full.dtype)

#shape
print(arr_full.shape)

# size
print(arr_full.size)

#ndim
print(arr_full.ndim)
