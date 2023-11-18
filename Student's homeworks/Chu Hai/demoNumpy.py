import numpy as np
#mang 1 chieu
arr1= np.array([1,2,3,4,5])
print (arr1)
 
 #mang 2 chieu
arr2= np.array([[1,2,3],[4,5,6]])
print(arr2)
#mang 3 chieu

import numpy as np

arr3 = np.array([[[1,2,3,4], [5,6,7,8]],
                [[9,10,11,12], [13,14,15,16]],
                [[17,18,19,20], [21,22,23,24]]])
print(arr3)

#zẻo
arri=zero = np.zeros((3,4))

#mt số 1
arr_one = np.ones((2,3,4))
print(arr_one)

#khác 
arr_one_float = np.ones((2,3,4), dtype=float)
print(arr_one_float)

#hàm arange ( bước nhảy)
 #arr_arande=np.arange(1,7,2) # => in ra [1,3,5]

#full 
#arr_full= np.full((2,3),8) #=> in ra 2 hàng 3 cột điền toàn 8

#eye ma trận đường chéo chính
arr_eye= np.eye(4,dtype=int)
print(arr_eye)
#ma trận ramdom
arr_random=np.random.random((2,3))
print(arr_random)

#lấy giá trị của ma trận dtype, shape(loại ma trận),size, só chiều (ndim)

print(arr_eye.dtype)
print(arr_random.dtype)

print(arr_random.shape)
print(arr_eye.shape)

print(arr_random.size)
print(arr_eye.size)

print(arr_random.ndim)
print(arr_eye.ndim)

####################
print(arr2)
print(arr2[1:,:3])
print(arr2[:2,:3])
print("------------\n")
print(arr2[arr2>2])
print("------------\n")


# toán ma trận
x=np.array([[1,2,],[3,4]], dtype=np.float64)
y= np.array([[5,6,],[7,8]], dtype=np.float64)
print(x+y)
print(np.add(x,y))

print("------------\n")
print(x-y)
print(np.subtract(x,y))

print("------------\n")
print(x*y)
print(np.multiply(x,y))

print("------------\n")
print(x/y)
print(np.divide(x,y))
#khai căn mt
print("------------\n")
print(np.sqrt(x))

#hàm tích vô hướng 2 mt
print(np.dot(x,y)) #hoac print(x.dot(y))

# sum
print(x.sum())
print(np.sum(x))
#tổng theo trục
print(x.sum(axis=0))
print(x.sum(axis=1))

#hàm max,min (có cả theo trục) 0,1 thôi ko có trục 2
print(x.max(axis=0))
print(x.max(axis=1))

print(x.min(axis=0))
print(x.min(axis=1))

#Mean giá trị trung bình
print(x.mean())
print(x.mean(axis=0))
print(x.mean(axis=1))
#median tính trung vị ma trận

print(np.median(x))
print(np.median(x, axis=0))
print(np.median(x, axis=1))

#nghịch đảo ma trận
print(x.T)

t= np.array([[10,2,50],
             [-3,0,9],
             [11,6,-20]], dtype=np.int16)
print(np.abs(t))

#concat
print(np.concatenate([x,y], axis=1))

