class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        b=[]
        arr_size=len(A)
        for i in range(0,arr_size-2):
            for j in range(i+1,arr_size-1):
                for k in range(j+1,arr_size):
                    sum=A[i]+A[j]+A[k]
                b.append(sum)
        size=len(b)
        max=9999999999999999999
        for i in range(0,size):
            m=abs(B-b[i])
            if m<max:
                max=m
                number=b[i]
        return number
        
        
        
