n = int(input("Enter n: "))
arr = [[0 for x in range(n)]for y in range(n)]
def isSafe(arr,x,y,n):
    #for row in range(x,-1,-1):
    # if(arr[row][y]==1):
    # return False
    row = x
    col = y 
    while(row>=0):
        if(arr[row][y]==1):
            return False
        row -= 1 
    row = x
    col = y 
    while(row>=0 and col>=0):
        if(arr[row][col]==1):
            return False
        row -= 1 
        col -= 1
    row = x
    col = y 
    while(row>=0 and col<n):
        if(arr[row][col]==1):
            return False
        row -= 1 
        col += 1
    return True
def nQueen(arr,x,n):
    if(x>=n):
        return True
    for col in range(n):
        if(isSafe(arr,x,col,n)):
            arr[x][col] = 1 
            if(nQueen(arr,x+1,n)):
                return True
            arr[x][col]=0 # backtracking
    return False
#return True
if(nQueen(arr,0,n)):
    for row in arr:
        print (row)
else:
    print("Failed") 