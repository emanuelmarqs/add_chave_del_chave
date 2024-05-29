pessoa = {
    'Nome':'Emanuel',
    'Idade':25,
    'Profissão':"Programador",
    'Empresa':'BaliPark',
    'Gênero':'Masculino',
    'Cidade':'Brasília'
}

#remover chave
del pessoa[input('Informe o nome da chave a ser deletada:')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')