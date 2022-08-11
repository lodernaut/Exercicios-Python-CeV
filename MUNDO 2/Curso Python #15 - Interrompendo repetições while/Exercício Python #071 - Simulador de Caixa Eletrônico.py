print('='*30)
print('\033[51mCAIXA ELETRÔNICO.\033[m'.center(37))
print('Saque apenas notas de #R$5,00  #R$10,00 #R$20,00 #R$50,00 #R$100,00 #R$200,00')
saque = int(input('Valor a ser Sacado? '))
print('-'*30)
total = saque #EXEMPLO DO TOTAL O PROGRAMA VAI VERIFICAR QUANTAS VEZES SERÃO NECESSARIAS SACAR 200 PARA ELIMINAR A QUNTIDADE DE 200 E PARTIR PRA PROXIMA cédula.
ced = 200 #PROGRAMA IRÁ COMEÇAR VERIFICANDO SE NECESSITA USAR CÉDULA DE 200.
totced = 0 #CONTADOR DE QUANTAS CÉDULAS SERÁ ENTREGUE DE X CÉDULA. EXP: 640reais -> (3x 200ced) + (2x 20ced).
while True:
    if total >= ced:
        total -= ced # VERIFICANDO QUANTAS VEZES CONSEGUE TIRAR 200 DO TOTAL.
        totced += 1
    else: # "SENÃO" DER PRA TIRAR VAI VERIFICAR QUAL A CÉDULA ATUAL
        if totced >0: #só vai escrever se o total de cédulas for > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 200: #SE A CÉDULA ATUAL FOR IGUAL A 200 NÃO PODE TIRAR MAIS 200
             ced = 100 #PASSANDO PRA PRÓXIMA CÉDULA
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced ==10:
            ced = 5
        totced = 0 #TODA VEZ QUE MUDA DE NOTA O TOTAL DE CÉDULA VOLTA A 0(zero).
        if total ==0:
            break
print('-'*30)
print('\033[51mVOLTE SEMPRE.\033[m'.center(37))

