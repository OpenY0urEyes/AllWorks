import random

my_list = []
for i in range(10):
    my_list.append(random.randint(0, 99))

print(my_list)


list1 = [[1,2,3,4],[1,2,3,5]]
list2 = [x[:] for x in list1]  
list2[0][3] = 100
print(f'list1:{list1}\t list2{list2}')