A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
at = (A*C)/2
pi = 3.14159
ac = pi*C**2
atr = ((A+B)*C)/2
aq = B*B
ar = A*B
print('TRIANGULO:', f'{at:.3f}')
print('CIRCULO:', f'{ac:.3f}')
print('TRAPEZIO:', f'{atr:.3f}')
print('QUADRADO:', f'{aq:.3f}')
print('RETANGULO:', f'{ar:.3f}')