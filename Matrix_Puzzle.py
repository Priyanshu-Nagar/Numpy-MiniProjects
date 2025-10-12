import numpy as np

num = np.arange(1, 25)
print(num)
# np.random.seed(42)
num1 = np.random.permutation(num)
print(num1)
# print(num)
num2 = num1.reshape(4, 6)
print(num2)
# print(num1)
alt = num2[::2, ::2]
print(alt)
add_it = np.array([[10], [20], [30], [40]])
new_num = num2 + add_it
print(new_num)

new_num = new_num.astype(float)
# print(new_num)

three_num = new_num % 3 == 0
new_num[three_num] = np.nan
print(new_num)
sum_num = np.nansum(new_num)
print(sum_num)
