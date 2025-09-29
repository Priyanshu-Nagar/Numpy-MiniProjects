import numpy as np
data = np.random.randint(9000, 15000, (5, 7))
# print("", data)
morethan_10000 = np.all(data > 10000, axis=1)
print("more than 10k:\n", data[morethan_10000])
# print(np.all(data > 10000, axis=1))
print("---------")
data = data.astype(float)
less_than_10000 = data < 10000
data[less_than_10000] = np.nan
print("nan means holiday:\n", data)
avg_daily_steps = np.nanmean(data, axis=1)
print("---------")
avg_daily_steps = avg_daily_steps.astype(int) 
print("Average of daily steps:\n", avg_daily_steps)
print("---------")
weekly_steps = np.nansum(data, axis=1, dtype=int, keepdims=True)
print("Total weekly steps:\n", weekly_steps)
# print(weekly_steps.shape)
print("---------")
goal = np.array([70000, 60000, 65000, 70000, 85000])
goal = goal.reshape((5, 1))
goal_met = weekly_steps >= goal
print("goal met or not:\n", goal_met)


