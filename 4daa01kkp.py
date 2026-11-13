
def knapsack_01_rec(val, wt, cap, n):
    if n == 0 or cap == 0:
        return 0

    if wt[n-1] <= cap:
        include = val[n-1] + knapsack_01_rec(
            val, wt, cap-wt[n-1], n-1
        )
        exclude = knapsack_01_rec(
            val, wt, cap, n-1
        )
        return max(include, exclude)

    else:
        return knapsack_01_rec(val, wt, cap, n-1)


val = [20, 30, 50, 60, 100]
wt = [2, 3, 4, 5, 9]
cap = 10
n = len(val)

print("Maximum Profit:", knapsack_01_rec(val, wt, cap, n))
