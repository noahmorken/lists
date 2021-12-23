presidents = ['george washington', 'thomas jefferson', 'abraham lincoln', 'theodore roosevelt']
print(f"Good morning, {presidents[0].title()}.")
print(f"Good afternoon, {presidents[1].title()}.")
print(f"Good evening, {presidents[2].title()}.")
print(f"Good night, {presidents[3].title()}.")

print(f"\nAh, {presidents[2].title()} couldn't make it.\n")
presidents[2] = 'andrew jackson'
print(f"Good morning, {presidents[0].title()}.")
print(f"Good afternoon, {presidents[1].title()}.")
print(f"Good evening, {presidents[2].title()}.")
print(f"Good night, {presidents[3].title()}.")