import collections
def sortedSquares(A):
    ans=collections.deque()
    l,r=0,(len(A) - 1)
    while l<=r:
        left,right=abs(A[l]),abs(A[r])
        if left > right:
            ans.appendleft(left*left)
            l+=1
        else:
            ans.appendleft(right*right)
            r+=1
    return ans
print(sortedSquares([-4,-1,0,3,10]))