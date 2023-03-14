#Part A
weeks = 16
print(weeks,type(weeks))

classes = 5
print(classes,type(classes))

tuition = 6000
print(tuition,type(tuition))

classes_per_week = 3
print(classes_per_week,type(classes_per_week))

cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week,type(cost_per_week))

cost_per_class = (cost_per_week/classes_per_week)
print(cost_per_class,type(cost_per_class))

print("Cost per week:", cost_per_week)
print("The cost per class is:", cost_per_class,"\n\n")

#Part B
import random
random.randint(1,10)

random_num = [19,2,27,15,11]
random_select = random.choice(random_num)
print("The randomly selected number is:",random_select)