v0 = float(input("Digite v0: "))
a = float(input("Digite a aceleração: "))
t = float(input("Digite o tempo: "))

velocidade = v0 + a * t

parte1 = v0 * t
parte2 = a * t * t / 2
distancia = parte1 + parte2

print(f"Velocidade = {velocidade}")
print(f"Distancia = {distancia} ({parte1} + {parte2})")