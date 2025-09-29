import numpy as np
images = np.random.randint(0, 256, (3, 4, 4))
# print(images)
print(images[0])
normalized_image = images / 255
print(normalized_image)
wieghts = np.array([[0.3, 0.5, 0.2]])
 
