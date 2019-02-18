"""
prices	            return
[498,501,470,489]	[2,1,1,0]
"""

prices = [498,501,470,489]

def solution(prices):
    count = 1
    maintance = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j] and j != len(prices) - 1:
                maintance.append(count)
                count = 1
                continue
            elif i == len(prices) - 1:
                count = 0
            else:
                count += 1


    return maintance


print(solution(prices))
