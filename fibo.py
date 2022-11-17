def iterative_Fib(n):
  if(n==1):
      return [0]
  elif(n==2):
      return [0,1]
  else:
    arr = [0,1]
    for i in range(2,n):
       arr.append(arr[i-1] + arr[i-2])
    return arr
def utility(n, arr):
   if(len(arr) == n):
      return arr
   else:
     if(len(arr) == 0):
         return utility(n, [0])
     elif(len(arr) == 1):
         return utility(n, [0,1])
     else:
        arr.append(arr[-2]+arr[-1])
        return utility(n, arr) 
def recursive_Fib(n):
   return utility(n, [])
print(iterative_Fib(8)) 
print(recursive_Fib(8))