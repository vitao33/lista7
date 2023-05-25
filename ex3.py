população = int(input('informe a população:'))
taxa_de_crescimento = float(input('informe a taxa de crescimento da população:'))

for i in range(1, 16):
    população = população * (taxa_de_crescimento / 100) +  população

    print(f'{i} ano: {população:.2f} Cidadões ')






























