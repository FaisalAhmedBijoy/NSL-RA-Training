"""
Coin change: O(n2)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 1, 1], [1, 1, 1], [1, 2, 2], [1, 2, 3], [1, 3, 4]]
4

"""
def coin_count(coins,length,taget):
    #initialize the table 0
    table=[[0 for i in range(length)] for i in range(target+1)]
    print(table)
    
    #fill the 0 in target=0
    for i in range(length):
        table[0][i]=1
    print(table)
    for i in range(1,target+1):
        for j in range(length):
            x=table[i-coins[j]][j] if i-coins[j]>=0 else 0
            y=table[i][j-1] if j>=1 else 0
            
            table[i][j]=x+y
    print(table)
    return table[target][length-1]
            
coins=[1,2,3]
length=len(coins)
target=4
print(coin_count(coins,length,target))