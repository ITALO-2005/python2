import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print(f"Área do círculo: {area:.2f}")
print(f"Perímetro do círculo: {perimetro:.2f}")
