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

print("\nSome more presidents have decided to show up.\n")
presidents.insert(0, 'john adams')
presidents.insert(3, 'harry truman')
presidents.append('ronald reagan')
print(f"Good morning, {presidents[0].title()}.")
print(f"Good morning, {presidents[1].title()}.")
print(f"Good afternoon, {presidents[2].title()}.")
print(f"Good afternoon, {presidents[3].title()}.")
print(f"Good evening, {presidents[4].title()}.")
print(f"Good evening, {presidents[5].title()}.")
print(f"Good night, {presidents[6].title()}.")