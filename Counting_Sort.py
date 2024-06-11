
def CountingSort(input_arr):
    m=max(input_arr)
    n=len(input_arr)

    counts=[0]*(m+1)

    for j in input_arr:
        counts[j]+=1

    for i in range(1,m+1):
        counts[i]+=counts[i-1]

    output_arr=[0]*n

    for i in range(n-1,-1,-1):
            output_arr[counts[input_arr[i]]-1]=input_arr[i]
            counts[input_arr[i]]-=1

    print(output_arr)

arr=[1,2,1,1,1,1,2,2,2,3,4,4,4,0,0,0,3,3,3,3,3,0,1]
CountingSort(arr)
