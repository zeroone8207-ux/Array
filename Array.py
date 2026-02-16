#membuat array
import array as arr
a = arr.array('i', [1,2,3])
print("new created array : ", end=" ")
for i in range(0, 3):
  print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("new created array :", end=" ")
for i in range(0, 3):
  print(b[i], end=" ")

#Menahmbahkan elemen array
import array as arr
a = arr.array('i', [1,2,3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
  print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion :", end=" ")
for i in (a):
  print(i, end=" ")
print()
b = arr.array('d', [5.56, 7.62, 12.7])
print("Array before append :", end=" ")
for i in range(0, 3):
  print(b[i], end=" ")
print()
b.append(14.5)
print("Array after append :", end=" ")
for i in (b):
  print(i, end=" ")
print()

#mengakses elemen array
import array as arr
a = arr.array('i', [1,2,3,4,5,6])
print("Accessed element  :", a[0])
print("Accessed element  :", a[3])
b = arr.array('d', [5.56, 7.62, 12.7])
print("Accessed element  :", b[1])
print("Accessed element  :", b[2])

#menghapus elemen array
import array
arr = array.array('i', [1,2,3,1,5])
print("new array :", end=" ")
for i in range(0, 5):
  print(arr[i], end=" ")

print("\r")
print("popped element :", end=" ")
print(arr.pop(2))
print("array after popping :", end=" ")
for i in range(0, 4):
  print(arr[i], end=" ")

print("\r")
arr.remove(1)
print("array after removal :", end=" ")
for i in range(0, 3):
  print(arr[i], end=" ")

#pemotongan elemen array
import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("initial array :")
for i in (a):
  print(i, end=" ")
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
Sliced_array = a[5:]
print("\nSlicing elements from 5th elements to last : ")
print(Sliced_array)
Sliced_array = a[:]
print("\nPrinting all elements using slice operation : ")
print(Sliced_array)

#mengubah elemen array
import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("initial array :", end=" ")
for i in range(0, 6):
  print(arr[i], end=" ")

print("\r")
arr[2] = 6
print("Array after update :", end=" ")
for i in range(0, 6):
  print(arr[i], end=" ")
print()
arr[4] = 8
print("Array after update :", end=" ")
for i in range(0, 6):
  print(arr[i], end=" ")

#operasi array
import array
arr = array.array('i', [1, 2, 3, 4, 2, 5, 2])

#menghitung elemen array
count = arr.count(2)
print("Number of occurrences of 2 :", count)

#membalik elemen array
print("Original array :", *arr)
arr.reverse()
print("Reversed array :", *arr)

#extend dalam array
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
print("Before extend operation :", end=" ")
for i in range(0, 5):
  print(a[i], end=" ")
print()
a.extend([6, 7, 8, 9, 10])
print("\nAfter extend operation :", end=" ")
for i in range(0, 10):
  print(a[i], end=" ")
print()

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Before extend operation :", end=" ")

for i in range(0, 6):
  print(a[i], end=" ")
print()
a.extend([7, 8, 9, 10, 11, 12])
print("\n After extend operation", end=" ")

for i in range(0, 12):
  print(a[i], end=" ")
print()
b = arr.array('d', [5.56, 7.62, 7.92, 12.7, 14.5, 20.0])
print("\n Before extend operation", end=" ")

for i in range(0, 6):
  print(b[i], end=" ")
print()
b.extend([2.5 , 2.6 , 2.7 , 2.8])
print("\n After extend operation", end=" ")

for i in range(0,9+1):
  print(b[i],end=" ")
print()
