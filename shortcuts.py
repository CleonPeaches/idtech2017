cities = ["City A", "City B", "City C"]

'''
Le bad way
i = 0
for city in cities:
    print(i, city)
    i += 1
'''

for i, city in enumerate(cities):
    print(i + 1, city)

print("\n" * 5)

x_list = [1,2,3]
y_list = [2,4,6]

'''
The bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)
'''

for x, y in zip(x_list, y_list):
    print(x, y)
    



