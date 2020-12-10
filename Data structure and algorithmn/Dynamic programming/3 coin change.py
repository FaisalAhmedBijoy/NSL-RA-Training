# -*- coding: utf-8 -*-
"""
Coin change
Current m :  3
Current m :  2
Current m :  1
Current m :  1
Current m :  1
Current m :  1
Current m :  2
Current m :  1
Current m :  1
Current m :  3
Current m :  2
Current m :  1
                              C({1,2,3}, 5)                     
                           /             \    
                         /                 \                  
             C({1,2,3}, 2)                 C({1,2}, 5)
            /       \                      /      \         
           /         \                    /         \   
C({1,2,3}, -1)  C({1,2}, 2)        C({1,2}, 3)    C({1}, 5)
               /    \             /     \           /     \
             /       \           /       \         /        \
    C({1,2},0)  C({1},2)   C({1,2},1) C({1},3)    C({1}, 4)  C({}, 5)
                   / \     / \        /\         /     \         
                  /   \   /   \     /   \       /       \  
                .      .  .     .   .     .   C({1}, 3) C({}, 4)
                                               / \ 
                                              /   \   
                                             .      .
4
"""
def count(coins,m,target):
    if target==0:
        return 1
    if target<0:
        return 0
    if m<=0 and target>=1:
        return 0
    print("Current m : ",m)
    return count(coins,m-1,target) + count(coins,m,target-coins[m-1])
coins=[1,2,3]
m=len(coins)
target=4
print(count(coins,m,target))

