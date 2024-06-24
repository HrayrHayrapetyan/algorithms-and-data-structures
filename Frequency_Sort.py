class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        
        ls=list(di.items())
        l=len(ls)
        for i in range(l-1):
            for j in range(i+1,l):
                if ls[i][1]==ls[j][1] and ls[i][0]<ls[j][0] or ls[i][1]>ls[j][1]:
                        ls[i],ls[j]=ls[j],ls[i]
        sorted_dict=dict(ls)

        result=[[i]*j for i,j in sorted_dict.items()]
        return [item for row in result for item in row]
