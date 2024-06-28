import random
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

def random_partition(arr,l,h):
    r=random.randint(l,h-1)
    arr[r],arr[l]=arr[l],arr[r]
    return partition(arr,l,h)

def quickSort(arr,l,h):

    if l<h:
        j=random_partition(arr,l,h)
        quickSort(arr,l,j)
        quickSort(arr,j+1,h)

if __name__=='__main__':
     ls=[-23,4,21,2,3,4,5,6,2,2345,0,241,0]
     quickSort(ls,0,len(ls))
     print(ls)