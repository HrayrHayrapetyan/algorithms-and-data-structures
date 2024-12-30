def find_Max(ls,index,max):

    if index==len(ls):
        return max
    if max<ls[index]:
        max=ls[index]
    return find_Max(ls,index+1,max)


ls=[8,29,45,6,23,1,456,3,321,3,4,1,4567,1,2,3,4]
max=find_Max(ls,0,ls[0])
print(max)