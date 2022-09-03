def maior(*num):
    print("-"*62)
    print("Analisando os valores...")
    if len(num) == 0:
        print(" →\nNenhum valor foi informado.")
    elif len(num) == 1:
        print(f" →", ''.join(str(*num)))
        print(f"Foi informado {len(num)} valor. Maior valor: {''.join(str(*num))}")
    elif len(num) > 1:
        print("|", ', '.join(str(num) for num in num), "|", f"Foram informados | {len(num)} | valores ao todo.")
        print(f"O maior valor informado foi: {max(num)}")


maior(4, 5, 87, 5, 455, 11)
maior(0, 0)
maior(6)
maior(0)
maior()
