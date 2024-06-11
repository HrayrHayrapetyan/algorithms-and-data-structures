
def InsertionSort(arr):
        n=len(arr)
        for i in range(1,n):
                j=i-1
                x=arr[i]
                while j>-1 and arr[j]>x:
                    arr[j+1]=arr[j]
                    j-=1
                arr[j+1]=x

        print(arr)

arr=[1,24,2414,54,2,12,5,6,7,87,0,-245]
InsertionSort(arr)