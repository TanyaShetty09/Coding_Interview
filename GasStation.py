def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        
        if remaining < 0:
            return False
        
        i = (i + 1) % n
    
    return True

def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1

n = int(input("Enter the number of gas stations: "))
print("Enter gas values:")
gas = list(map(int, input().split()))
print("Enter cost values:")
cost = list(map(int, input().split()))

result = gas_station(gas, cost)
if result != -1:
    print(f"The starting gas station index is: {result}")
else:
    print("There is no possible solution.")