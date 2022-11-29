import random
punkty = []
y = 0
for i in range(15):
    punkty.append(round(random.uniform(0, 50), 2))
print(punkty)
print(min(punkty))
print(max(punkty))
