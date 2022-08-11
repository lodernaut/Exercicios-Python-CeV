print('*.·:·.✧ ✦ ✧.·:·.* Bella Notte Company. *.·:·.✧ ✦ ✧.·:·.*')
total_compra = float(input('Valor total da compra: '))
print('Formas de Pagamento.')
print('À vista Dinheiro/PIX__[ 0 ]'
      '\nÀ vista Crédito_______[ 1 ]'
      '\n2x Crédito____________[ 2 ]'
      '\n3x Crédito____________[ 3 ]')
# P = porcento
# PDJ= porcento de juros
# à vista Dinheiro/Pix = 10%
# À Vista /1x Crédito = 5%
# 2x crédito = sem deconto
# 3x ou mais = 20% de juros.
dezP = total_compra - (total_compra *10 /100)
cincoP = total_compra - (total_compra *5 /100)
vintePDJ = total_compra + (total_compra *20 / 100)

opção = int(input('Qual opção de Pagamento? '))
if opção ==0:
    print(f'Total da Compra R${total_compra:.2f} com desconto À Vista Dinheiro/Pix 10% fica R${dezP:.2f}')
elif opção ==1:
    print(f'Total da Compra R${total_compra:.2f} com desconto 5% Crédito á vista/1x fica R${cincoP:.2f}')
elif opção ==2:
    print(f'Total da Compra R${total_compra:.2f} em 2x não tem desconto. valor de cada Parcela R${total_compra/2:.2f} // Valor total R${total_compra:.2f}')
elif opção ==3:
    quantidade_parcelas = int(input('Quantidade de parcelas: '))
    parceladoCjuros = total_compra + vintePDJ
    print(f'Total da Compra R${total_compra:.2f} Parcelado em {quantidade_parcelas}x tem 20% de juros cada parcela fica R${parceladoCjuros/quantidade_parcelas:.2f} valor final {parceladoCjuros:.2f}')
