Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        
        size=len(A)
        b=[]
        c=[]
        for i in range(size-1):
            if (i+1) not in c:
                a=[]
                a.append(i+1)
                c.append(i+1)
                for j in range(i+1,size):
                    if (sorted(A[i])==sorted(A[j])):
                        a.append(j+1)
                        c.append(j+1)
                    
                b.append(a)
            
        
        if size not in c:
            b.append([size])
        
        return b
            
            
                
                
        
        
               
            
     
    
                    
            
