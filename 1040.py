N1,N2,N3,N4 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
M = (N1*2+N2*3+N3*4+N4)/10 
if M >= 7.0:
    print(f'Media: {M:.1f}')
    print('Aluno aprovado.')
if M<5.0:
    print(f'Media: {M:.1f}')
    print('Aluno reprovado.')
if 5.0<=M<=6.9:
    print(f'Media: {M:.1f}')
    print('Aluno em exame.')
    EX = float(input())
    print(f'Nota do exame: {EX:.1F}')
    M2 = (EX + M)/2
    if M2>=5:
        print('Aluno aprovado.')
        print(f'Media final: {M2:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media Final: {M2:.1f}')