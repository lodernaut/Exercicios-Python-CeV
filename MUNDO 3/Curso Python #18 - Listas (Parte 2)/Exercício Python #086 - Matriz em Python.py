import tabulate
data = [('Item', 'Amount'), ('First label', 23), ('Second thing', 45), ('Third one', 55)]
tt = tabulate.Table()
for row in data:
    tt.append(row)
tt.do("rule add")
print(tt)