primeiro = int(input('Primeiro segmento: '))
segundo = int(input('Segundo segmento: '))
terceiro = int(input('Terceiro segmento: '))
if primeiro <=0 or segundo <=0 or terceiro <=0:
    print('Lados nulos ou negativos não sao aceitos.')
elif primeiro >= segundo+terceiro or segundo >= primeiro+terceiro or terceiro >= primeiro+segundo:
    print('Triângulo inexistente.')
elif primeiro == segundo and segundo == terceiro:
    print('Forma um triângulo Equilatero.')
elif primeiro == segundo or segundo == terceiro or terceiro == primeiro:
    print('forma um triângulo isoceles.')
else:
    print('Forma um triângulo escaleno')


