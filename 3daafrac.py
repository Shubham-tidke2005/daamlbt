n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    weight.append(int(input("Enter weight: ")))
    profit.append(int(input("Enter profit: ")))

capacity = int(input("Enter capacity: "))

ratio = []

for i in range(n):
    ratio.append((profit[i] / weight[i], weight[i], profit[i]))

ratio.sort(reverse=True)

total = 0

for r, w, p in ratio:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += r * capacity
        break

print("Maximum Profit:", total)
