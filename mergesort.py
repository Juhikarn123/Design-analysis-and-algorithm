import random
def mergeSort(myList):
  if len(myList)>1:
    mid=len(myList) //2
    left=myList[:mid]
    right=myList[mid:]
    mergeSort(left)
    mergeSort(right)
    i=0
    j=0
    k=0
    while i<len(left)and j<len(right):
      if left[i]<=right[j]:
        myList[k]=left[i]
        i+=1
      else:
        myList[k]=right[j]
        j+=1
      k+=1
    while i<len(left):
          myList[k]=left[i]
          i+=1
          k+=1
    while j<len(right):
           myList[k]=right[j]
           j+=1
           k+=1
            
            
           
 



import time
begin1=time.time()
myList=random.sample(range(1,100),10)
mergeSort(myList)
print("the sorted array is")
print(myList)
time.sleep(1)
end1=time.time()
time1=end1-begin1
print(f"total runtime of the program is {time1}")


import time
begin2=time.time()
myList=random.sample(range(1,100),15)
mergeSort(myList)
print("the sorted array is")
print(myList)
time.sleep(1)
end2=time.time()
time2=end2-begin2
print(f"total runtime of the program is {time2}")


import time
begin3=time.time()
myList=random.sample(range(1,100),20)
mergeSort(myList)
print("the sorted array is")
print(myList)
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



