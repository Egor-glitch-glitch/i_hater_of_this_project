n = int(input())

if 2 <= n <= 100:
    prices = list(map(int, input().split()))
    
    if len(prices) == n:
        valid_prices = True
        for price in prices:
            if not (0 <= price <= 10**9):
                valid_prices = False
                break
        
        if valid_prices:
            result = [-1] * n
            for i in range(n):
                for j in range(i + 1, n):
                    if prices[j] < prices[i]:
                        result[i] = j
                        break  
            print(' '.join(map(str, result)))
        else:
            print("Ошибка в ценах")
    else:
        print("Ошибка в количестве городов")