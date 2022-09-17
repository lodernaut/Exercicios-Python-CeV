def voto(n):
    from datetime import datetime
    idade = datetime.today().year - n
    if idade < 16:
        return f"{idade} anos, Voto! Negado."
    elif 16 <= idade < 18 or idade >= 70:
        return f"{idade} anos, Voto! Opcional."
    else:
        return f"{idade} anos, Voto! Obrigatório."


nascimento = int(input("nascimento: "))
print(voto(nascimento))
