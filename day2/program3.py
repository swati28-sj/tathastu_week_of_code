n=int(input())
for i in range(n*2-1):
    if(i<n):
        print(' '*i+'*'+' '*((n-1-i)*2)+'*')
    else:
        print(' '*((2*n-2)-i)+'*'+' '*2*(i-n+1)+'*')
