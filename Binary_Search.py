def binary_search(ls,item,left,right):
    if left<=right:
        mid=left+(right-left)//2

        if ls[mid]==item:
            return mid

        elif ls[mid]>item:
            return binary_search(ls,item,left,mid-1)

        elif ls[mid]<item:
            return binary_search(ls,item,mid+1,right)

    else:
        return -1

if __name__=='__main__':
    ls=[2,3,4,5,6,67,145]
    item=67
    index=binary_search(ls,45,0,len(ls))
    if index==-1:
        print('Not found')