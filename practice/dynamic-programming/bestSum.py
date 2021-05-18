def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    bestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if (remainderCombination != None):
            combination = remainderCombination + [num]
            if bestCombination == None or len(combination) < len(bestCombination):
                bestCombination = combination[:]

    return bestCombination


def bestSum(targetSum, numbers, dp={}):
    if targetSum in dp: return dp[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    bestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, dp=dp)
        if (remainderCombination != None):
            combination = remainderCombination + [num]
            if bestCombination == None or len(combination) < len(bestCombination):
                bestCombination = combination[:]

    dp[targetSum] = bestCombination
    return bestCombination

if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7])) # [7]
    print(bestSum(8, [2, 3, 5])) # [3, 5]
    print(bestSum(8, [1, 4, 5])) # [4, 4]
    print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]