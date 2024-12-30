
def SelectionSort(arr):
        n=len(arr)
        for i in range(0,n-1):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[min_index],arr[i]=arr[i],arr[min_index]
        print(arr)

arr=[2,32,456,321,-234,0,3,2,3]
SelectionSort(arr)