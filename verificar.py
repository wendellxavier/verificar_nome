verificar = input('digite seu nome para nos verificar se começa com a letra que nos queremos: ')

if verificar.lower().startswith('w'):
    print(f'Seu nome começa com a letra "w"')
else:
    print(f'Seu nome não começa com a letra "w"')