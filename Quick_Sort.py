def partition(arr,l,h):
    pivot=arr[l]
    i=l+1
    j=h-1

    while i<=j:

        while i<=j and arr[i]<=pivot:
            i+=1

        while i<=j and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    arr[l],arr[j]=arr[j],arr[l]
    return j

def quickSort(arr,l,h):

    if l<h:
        j=partition(arr,l,h)
        quickSort(arr,l,j)
        quickSort(arr,j+1,h)

if __name__=='__main__':
     ls=[23,4,21,456,3,21,245,242,1212,4,2,1,2,2,23,4,567,89,431,0]
     quickSort(ls,0,len(ls))
     print(ls)