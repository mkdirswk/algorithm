"""
prices	            return
[498,501,470,489]	[2,1,1,0]
"""

prices = [498,501,470,489]

def solution(prices):
    count = 1
    maintance = []
    for i in range(len(prices)):
        if i != (len(prices) - 1):
            for j in range(i + 1,len(prices)):
                if prices[i] < prices[j]:
                    count += 1
                else:
                    maintance.append(count)
                    count = 1
                    break
        else:
            maintance.append(0)


    return maintance


print(solution(prices))
