'''
n=int(input())
array=set(map(int,input().split()))
print(sum(array)/len(array))
'''
def average(array):
    # your code goes here
    avg=set(array)
    return sum(avg)/len(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)