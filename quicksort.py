import time
import random
def partition(arr,low,high):
  i=(low-1)
  pivot=arr[high]
  for j in range(low,high):
    if arr[j]<=pivot:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[high]=arr[high],arr[i+1]
  return(i+1)
def quicksort(arr,low,high):
  if len(arr)==1:
    return arr
  if low<high:
    pi=partition(arr,low,high)
    quicksort(arr,low,pi-1)
    quicksort(arr,pi+1,high)
    
    
    
 begin1=time.time()
arr=random.sample(range(1,100),10)
n=len(arr)
quicksort(arr,0,n-1)
print("sorted array is:")
for i in range(n):
  print("%d"%arr[i])
time.sleep(1)
end1=time.time()
time1=end1-begin1
print(f"total runtime of the program is {time1}")


begin2=time.time()
arr=random.sample(range(1,100),15)
n=len(arr)
quicksort(arr,0,n-1)
print("sorted array is:")
for i in range(n):
  print("%d"%arr[i])
time.sleep(1)
end2=time.time()
time2=end2-begin2
print(f"total runtime of the program is {time2}")


begin3=time.time()
arr=random.sample(range(1,100),20)
n=len(arr)
quicksort(arr,0,n-1)
print("sorted array is:")
for i in range(n):
  print("%d"%arr[i])
time.sleep(1)
end3=time.time()
time3=end3-begin3
print(f"total runtime of the program is {time3}")


from matplotlib import pyplot as plt
x_values=[10,15,20]
y_values=[time1,time2,time3]
plt.ylabel("time in sec")
plt.xlabel("input")
plt.plot(x_values,y_values)
plt.show()
