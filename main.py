

import json

with open('clientes.json', 'r', encoding='utf-8') as arquivo:
    clientes = json.load(arquivo)
  

print('=' * 30 + '\n   CADASTRO DO CLIENTE   \n' + '=' * 30)

nome = str(input('Digite nome do cliente: '))
while nome == '' or nome.isdigit():
    print('ERRO DE DIGITAÇÃO!')
    nome = str(input(f'Digite nome novamente: '))

idade =int(input('Digite  idade do cliente: '))
while idade <=0 or idade>120:
    idade = int(input('Digite idade novamente: '))
if idade >= 18:
    classificação = ('cliente maior de idade')
else:
    classificação = ('cliente menor de idade')

    
altura =float(input(  'Digite altura do cliente: '))
while altura <=0 or altura > 3:
    print('Erro no sistema!')
    altura  = float(input('Digite altura novamente: '))

cliente_ativo =input('cliente_ativo? (s/n)').lower()
while cliente_ativo!= 's' and cliente_ativo!= 'n':
    print('resposta invalida!')
    cliente_ativo = input('cliente_ativo? (s/n)').lower()
    
if cliente_ativo == 's':
    cliente_ativo = True
else:
    cliente_ativo = False

if cliente_ativo:
    status = (' cliente está ativado ')
else:
    status = (' cliente está inativo ')


print('=' * 30 + '\n   DADOS DO CLIENTE   \n' + '=' * 30)
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Altura: {altura} m ')
print(f'clssificação: {classificação}')
print(f'status: {status}')


while True: 
    print('=' * 30 +'\n      SISTEMA      \n'+'=' * 30)
    print(' 1 - Cadastrar clientes\n  2 - Listar clientes\n  3 - Buscar clientes\n  4 - Excluir clientes\n  5 - Alterar cliente\n  6 - Relatório de clientes\n  7 - Sair')

    opcao = int(input('Escolha uma opção: '))
    while opcao!= 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7:
        print('opção é invalida')
        opcao = int(input('Escolha uma opção: '))

   
    if opcao ==1:
        print('=' * 30 +'\n      CADASTRAR CLIENTE      \n'+'=' * 30)
        print('Cadastrando novo cliente...')

        nome = str(input('Digite nome do cliente: '))
        while nome == '' or nome.isdigit():
         print('ERRO DE DIGITAÇÃO!')
         nome = str(input(f'Digite nome novamente: '))

        idade = int(input('Digite idade do cliente: '))
        while idade <= 0 or idade> 120:
            idade = int(input('Digite idade do cliente: '))
        if idade >= 18:
            classificacao = ('Cliente maior de idade')
        else:
            classificacao = ('Cliente menor de idade')

        altura = float(input('Digite altura do cliente: '))

        while altura <=0 or altura> 3:
            print(f'ERRO NO SISTEMA!')
            altura = float(input('Digite a altura do cliente novamente: '))


        cliente_ativo = input('cliente ativo? (s/n): ').lower() == 's'
        if cliente_ativo:
            status = ('Cliente ativado')
        else:
            status = ('cliente inativado')
        print(f'Nome: {nome}')
        print(f'Idade:{idade} anos')
        print(f'Altura:{altura}  m')
        print(f'status: {status}')
        print(f'classificacao: {classificacao}')

        cliente = {'id': len(clientes) + 1,
             'nome': nome,
            'idade': idade,
            'altura': altura,
            'classificação': classificação,
            'status': status
}
        clientes.append(cliente)

        with open('clientes.json', 'w', encoding='utf-8') as arquivo:
         json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

        print(len(clientes))
       
    elif opcao == 2:
        print('=' * 30 +'\n      LISTAR CLIENTES      \n'+'=' * 30)
        if not clientes:
            print(f'Não há clientes cadastrados!')
        else:
            print(f'Clientes cadastrados:{len(clientes)}')
            for cliente in clientes:
                print(f'Nome: {cliente['nome']}')
                print(f'Idade: {cliente['idade']}')
                print(f'Altura: {cliente['altura']}')
                print(f'Classificação: {cliente['classificação']}')
                print(f'Status: {cliente['status']}')
       
    elif opcao == 3:
        print('=' * 30 +'\n      BUSCAR CLIENTE      \n'+'=' * 30)
        nome_busca = input('nome do cliente: ').lower()
        encontrado = False

        for cliente in clientes:
            if cliente['nome'].lower() == nome_busca:
                print(f'Nome: {cliente['nome']}')
                print(f'Idade: {cliente['idade']}')
                print(f'Altura: {cliente['altura']}')
                print(f'Classificação: {cliente['classificação']}')
                print(f'Status: {cliente['status']}')
                encontrado = True
                break

        if not encontrado:
            print('cliente não encontrado! ')
       

    elif opcao == 4:
        print('=' * 30 +'\n      EXCLUIR CLIENTE      \n'+'=' * 30)
        nome_excluir = input(f'Nome do cliente: ').lower()
        encontrado = False

        for cliente in clientes:
            if cliente['nome'].lower() == nome_excluir:
                clientes.remove(cliente)
                with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(clientes, arquivo, ensure_ascii=False, indent=4)
                encontrado = True
                print('Cliente removido com sucesso!')
                break

        if not encontrado:
            print('Cliente não encontrado')
        
    elif opcao == 5:
        print('=' * 30 +'\n      ALTERAR CLIENTE      \n'+'=' * 30)
        nome_alterar = input('Digite o nome do cliente: ').lower()
        for cliente in clientes:
            if cliente['nome'].lower() == nome_alterar:
                print('cliente encontrado!')
                print('1 - Alterar nome\n2 - Alterar idade\n3 - Alterar altura\n4 - Alterar status\n5 - Sair')
                opcao_alterar = int(input('Escolha uma opção: '))
                if opcao_alterar == 1:  
                    novo_nome = input('Digite o novo nome: ')
                    while novo_nome == '' or novo_nome.isdigit():
                        print('ERRO DE DIGITAÇÃO!')
                        novo_nome = input('Digite o novo nome novamente: ')
                    cliente['nome'] = novo_nome
                    with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                     json.dump(clientes, arquivo, ensure_ascii=False, indent=4)
                    print('Nome alterado com sucesso!')
                elif opcao_alterar == 2:
                    nova_idade = int(input('Digite a nova idade: '))
                    while nova_idade <= 0 or nova_idade > 120:
                        print('Erro! A idade deve estar entre 1 e 120 anos.')
                        nova_idade = int(input('Digite a nova idade: '))
                    cliente['idade'] = nova_idade
                  
                    print('Idade alterada com sucesso!')
                elif opcao_alterar == 3:
                    nova_altura = float(input('Digite a nova altura: '))
                    while nova_altura <= 0 or nova_altura > 3:
                        print('Erro! A altura deve estar entre 0 e 3 metros.')
                        nova_altura = float(input('Digite a nova altura novamente: '))
                    cliente['altura'] = nova_altura
                    with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)
                    print('Altura alterada com sucesso!')
                elif opcao_alterar == 4:
                    novo_status = input('Digite o novo status (s/n): ').lower()
                    while novo_status != 's' and novo_status != 'n':
                        print('Resposta inválida!')
                        novo_status = input('Digite o novo status (s/n): ').lower()
                    if novo_status == 's':
                        cliente['status'] = 'Cliente ativado'
                    else:
                        cliente['status'] = 'Cliente inativado'
                    print('Status alterado com sucesso!')
                elif opcao_alterar == 5:
                    print('Saindo da alteração de cliente.')
                else:
                    print('Opção inválida!')

                    with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)
                        
        print('=' * 30 +'\n      RELATÓRIO DE CLIENTE      \n'+'=' * 30)
        maiores = 0
        menores = 0
        for cliente in clientes:
            if cliente['idade'] >= 18:
                maiores += 1
            else:
                menores += 1
        print('Maiores de idade:', maiores)
        print('Menores de idade:', menores)

    elif opcao == 7:
        print('Saindo do sistema...')
        break

        

   
   


