def merge(arr,left,mid,right):
    subArrayone=mid-left+1
    subArraytwo=right-mid

    leftArray=[0]*subArrayone
    rightArray=[0]*subArraytwo

    leftArrayindex=0
    rightArrayindex=0
    mergedArrayindex=left

    for i in range(subArrayone):
        leftArray[i]=arr[left+i]
    for j in range(subArraytwo):
        rightArray[j]=arr[mid+j+1]


    while leftArrayindex<subArrayone and rightArrayindex<subArraytwo:
        if leftArray[leftArrayindex]<=rightArray[rightArrayindex]:
            arr[mergedArrayindex]=leftArray[leftArrayindex]
            leftArrayindex+=1
        else:
            arr[mergedArrayindex]=rightArray[rightArrayindex]
            rightArrayindex+=1
        mergedArrayindex+=1

    while leftArrayindex<subArrayone:
        arr[mergedArrayindex]=leftArray[leftArrayindex]
        leftArrayindex+=1
        mergedArrayindex+=1

    while rightArrayindex<subArraytwo:
        arr[mergedArrayindex]=rightArray[rightArrayindex]
        rightArrayindex+=1
        mergedArrayindex+=1

def mergeSort(arr,begin,end):
    if begin>=end:
        return

    mid=begin+(end-begin)//2
    mergeSort(arr,begin,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,begin,mid,end)

if __name__=='__main__':
    arr=[45,31,234,1,23,4,5,678,1]
    arr_size=len(arr)
    mergeSort(arr,0,arr_size-1)
    print(arr)







