def plus_Minus(arr):
    pos_arr, neg_arr, zero_arr = 0, 0, 0
  
    # This for loop separates the +ve, -ve and zero values and counts
    for i in range(0, n):
        if arr[i] > 0:
            pos_arr += 1
        elif arr[i] < 0:
            neg_arr += 1
        elif arr[i] == 0:
            zero_arr += 1

    print(format(float(pos_arr)/float(len(arr)) , '.6f'))
    print(format(float(neg_arr)/float(len(arr)), '.6f'))
    print(format(float(zero_arr)/float(len(arr)), '.6f'))

if __name__ == '__main__':
    # Size of array n
    n = int(input())
    
    # array/list contains n number of elements
    arr = list(map(int, input().split()))

    plus_Minus(arr)
