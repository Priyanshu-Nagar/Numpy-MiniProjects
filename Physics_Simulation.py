import numpy as np
velocity = np.array([3, 8, 5, 6, 7])
masses = np.array([10, 20, 30, 40, 50])
k_energy = 0.5 * masses * velocity**2
print("Kinetic Energy:", k_energy)
velocity = velocity.astype(float)
velocity[(2,)] = np.nan
print("Velocity with NaN:", velocity)
avg_velocity = np.nanmean(velocity)
print("Average Velocity", avg_velocity)
# print(np.isnan(velocity))
velocity[np.isnan(velocity)] = avg_velocity
print("Velocity after NaN replacement:", velocity)
velocity[(2,)] = np.inf
print("Velocity after NaN replace into inf:", velocity)
k_energy = 0.5 * masses * velocity**2
print("Kinetic Energy after inf velocity:", k_energy)
k_energy = np.append(k_energy, np.nan)
k_energy = k_energy.reshape(2, -1)
print("Kinetic Energies after reshaping :\n", k_energy)
print("Shape of Kinetic Energy:", k_energy.shape)