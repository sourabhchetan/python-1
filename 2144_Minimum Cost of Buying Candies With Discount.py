class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)

        total = 

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total
