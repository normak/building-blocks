#stock picker
#profit = price of purchase - price of sale
def stock_picker(stocks):
	max_profit = 0
	profits = []
	for i, price1 in enumerate(stocks):
		for j, price2 in enumerate(stocks):
			if ( j > i):
				profits.append([[i,j], (-price1) + price2])

	bestdays = None
	for i, profit in enumerate(profits):
		if (profits[i][1] > max_profit):
			bestdays= profits[i][0]
			max_profit = profits[i][1]
	return bestdays


nums = [17,3,6,9,15,8,6,1,10]

print stock_picker(nums)