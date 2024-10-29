from module_fake_math import divide as fake_divide
from module_true_math import divide as true_divide

fake_result1 = fake_divide (10,5)
fake_result2 = fake_divide (5,0)
true_result3 = true_divide (16,4)
true_result4 = true_divide (4,0)

print (fake_result1)
print (fake_result2)
print (true_result3)
print (true_result4)