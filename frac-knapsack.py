# item = (name, profit, weight)
items = [('A',60,10),('B',100,20),('C',120,30), ('D', 1000, 10)]
max_wt = 50
def fractional_knapsack(items, max_wt):
 #finding the profit/weight ratio 
    ratios = []
    for i in items:
        ratios.append((i[0], i[1], i[2], i[1]/i[2]))
    ratios.sort(key=lambda tup: tup[3], reverse = True)
    ans = {}
    optimal_profit = 0
    for item in ratios:
        if(item[2] < max_wt):
            max_wt -= item[2]
            ans[item[0]]=1
            optimal_profit += item[1]
        else:
            fraction = max_wt/item[2]
            ans[item[0]] = fraction
            max_wt = 0
            optimal_profit += fraction*item[1]
            break
    return {"ans":ans, "optimal_profit":optimal_profit}
 
 
 
 
print(fractional_knapsack(items, max_wt))