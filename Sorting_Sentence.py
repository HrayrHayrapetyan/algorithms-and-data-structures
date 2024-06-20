class Solution:
        def sortSentence(self, s: str) -> str:
            splitted=s.split()
            for i in range(0,len(splitted)-1):
                for j in range(i+1,len(splitted)):
                    if splitted[i][len(splitted[i])-1]>splitted[j][len(splitted[j])-1]:
                        splitted[i],splitted[j]=splitted[j],splitted[i]
            for i in range(0,len(splitted)):
                splitted[i]=splitted[i][:-1]
            result=' '.join(splitted)
            return  result

if __name__=='__main__':
        sl=Solution()
        print(sl.sortSentence('is2 sentence4 this1 a3'))

