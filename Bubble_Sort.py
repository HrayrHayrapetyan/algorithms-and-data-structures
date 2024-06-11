
def BubbleSort(arr):
        n=len(arr)
        for i in range(0,n):
                chlp=False
                for j in range(0,n-i-1):
                        if arr[j]>arr[j+1]:
                                arr[j],arr[j+1]=arr[j+1],arr[j]
                                chlp=True
                if not chlp:
                        break
        print(arr)


arr=[4,12,6,31,23,3,2124,-24,-212,0,43,214,24]
BubbleSort(arr)



