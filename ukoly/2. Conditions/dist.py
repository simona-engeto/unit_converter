coordinates_x_for_a = abs(int(input('Give coordinates X for point A: ')))
coordinates_y_for_a = abs(int(input('Give coordinates Y for point A: ')))
coordinates_x_for_b = abs(int(input('Give coordinates X for point B: ')))
coordinates_y_for_b = abs(int(input('Give coordinates Y for point B: ')))


distance_x = round(coordinates_x_for_b - coordinates_x_for_a)

distance_y = round(coordinates_y_for_b - coordinates_y_for_a)

distance = distance_x * distance_x + distance_y * distance_y

import math
round(math.sqrt(distance),2)
print('Point A, X Coordinate: ', coordinates_x_for_a)
print('Point A, Y Coordinate: ', coordinates_y_for_a)
print('Point X, B Coordinate: ', coordinates_x_for_b)
print('Point Y, B Coordinate: ',coordinates_y_for_b)
print("The distance between the points A and B is : ", round(math.sqrt(distance),2))