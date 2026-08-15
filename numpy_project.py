import numpy as np

#array creation
a = np.array([5,2,3,4])
b = np.array([2,3,4,5])
e = np.zeros((2,2))
g = np.ones((2,2))
print("Array(a) :",a)
print("Array(b) :",b)
print("Array(e) :",e)
print("Array(g) :",g)

#1.Array indexing
print("Array Indexing : ",a[0])
print("Array Indexing(negative):",a[-1])

#2.Array Slicing 
print("Array Slicing 1 : ",a[1:3])
print("Array Slicing 2 : ",a[2:4])

#3.Arithmetic operation
#Addition
c = a + b
print("Addition: ",c)

#Subraction
c = a - b
print("Subraction : ",c)

#Multiplication
c = a * b
print("Multiplication : ",c)

#Division
c = a / b
print("Division: ",c)

#Floor Division 
c = a // b
print("Floor Division : ",c)

#Modulas
c = a % b
print("Modulas : ",c)

#4.Reshaping Array
e = a.reshape(2,2)
print("Reshaping : ",e)

#5.Concatenating Array 
f = np.concatenate((a,b))
print("Concatenate : ",f)

#6.spliting array
print("Spliting : ",np.array_split(a,2))

#7.aggregate function
print("Sum of array : ",np.sum(a))
print("Mean of array : ",np.mean(a))
print("Max of array : ",np.max(a))
print("Min of array : ",np.min(a))

#8.sorting 
print("Sorting : ",np.sort(a))

#9.filtering data
x = a[a>1]
print("Filtering 1 : ",x)

y = a[a<=10]
print("Filtering 2 : ",y)

#10.Broadcasting
print("Broadcasting : ",a + 5)

#11.copying array
z = a.copy()
print("Copying : ",z)

#12.power 
print("Power ",a ** 2)

#13.comparsion 
print("Comparision : ",b > a)
print ("Checking equality : ",a == b)