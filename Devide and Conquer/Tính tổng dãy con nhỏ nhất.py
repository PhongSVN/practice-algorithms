def pp1(arr):
    max = arr[1]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            if(sum>max):
                max = sum
    return max


arr = [2,3,-5,7,9,4]

print(pp1(arr))