candies = [2,3,5,1,3]
extraCandies = 3
maxValue = max(candies)
result =[]
for i in range(len(candies)):
    result.append(candies[i] + extraCandies >= maxValue)
print(result)
            