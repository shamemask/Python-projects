import math

# расчет периметра и площади квадрата
square_side = input("Введите длину стороны квадрата: ")
square_side=int(square_side)
perimeter = square_side*4
print(f"Периметр квадрата со стороной {square_side} равен {perimeter}")
area = square_side*square_side
print(f"Площадь квадрата со стороной {square_side} равна {area}")
# расчет диагонали квадрата
diagonal = math.sqrt(2*square_side*square_side)
print(f"Диагональ квадрата со стороной {square_side} равна {diagonal}")

# расчет периметра и площади прямоугольника
rectangle_side1 = input("Введите длину первой стороны прямоугольника: ")
rectangle_side2 = input("Введите длину второй стороны прямоугольника: ")
rectangle_side1=int(rectangle_side1)
rectangle_side2=int(rectangle_side2)
perimeter = (rectangle_side1+rectangle_side2)*2
print(f"Периметр прямоугольника со сторонами {rectangle_side1} и {rectangle_side2} равен {perimeter}")
area = rectangle_side1*rectangle_side2
print(f"Площадь прямоугольника со сторонами {rectangle_side1} и {rectangle_side2} равна {area}")
# расчет диагонали прямоугольника
diagonal = math.sqrt(rectangle_side1*rectangle_side1+rectangle_side2*rectangle_side2)
print(f"Диагональ прямоугольника со сторонами {rectangle_side1} и {rectangle_side2} равна {diagonal}")

#Д.З. расчет площади треугольника по основанию и высоте
side = input("Введите длину основания треугольника: ")
side = int(side)
height = input("Введите длину высоты треугольника: ")
height = int(height)
area=(side*height)/2
print(f"Площадь треугольника с основанием {side} и высотой {height} равна {area}")

#Д.З. для продвинутых - расчет площади треугольника по трем сторонам
side1 = input("Введите длину первой стороны треугольника: ")
side2 = input("Введите длину второй стороны треугольника: ")
side3 = input("Введите длину третьей стороны треугольника: ")
side1=int(side1)
side2=int(side2)
side3=int(side3)
semiperimeter=(side1+side2+side3)/2
area = math.sqrt(semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))
print(f"Площадь треугольника со сторонами {side1}, {side2} и {side3} равна {area}")

