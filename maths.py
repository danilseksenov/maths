import numpy as np

#teht 1.1
a = 2.493
b = 0.911

print(np.degrees(a))
print(np.degrees(b))

#teht 1.2
c = 137.7
d = 62.3
print(np.radians(c))
print(np.radians(d))

#teht 1.3
degrees = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]

in_radians = [np.radians(degrees)]
print(in_radians)

#teht 2.1
a = 1.6 #m
b = 2.3 #m

hypotenuse = np.hypot(a,b)
print(hypotenuse)
