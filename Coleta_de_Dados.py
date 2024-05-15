pessoas = 0  # Inicializa o contador de pessoas com mais de 18 anos
masculino = 0  # Inicializa o contador de homens cadastrados
feminino_menos_20 = 0  # Inicializa o contador de mulheres com menos de 20 anos cadastradas

while True:
    print('CADASTRE UMA PESSOA!')
    idade = int(input('Qual é a sua idade? '))  # Solicita a idade da pessoa

    if idade > 18:
        pessoas += 1  # Incrementa o contador de pessoas com mais de 18 anos

    sexo = input('Qual é o seu sexo? (M/F) ').strip().upper()  # Solicita o sexo da pessoa

    if sexo == 'M':
        masculino += 1  # Incrementa o contador se o sexo for masculino
    
    if sexo == 'F' and idade < 20:
        feminino_menos_20 += 1  # Incrementa o contador se o sexo for feminino e a idade for menor que 20 anos

    continuar = input('Deseja continuar? (S/N) ').strip().upper()  # Pergunta se deseja continuar o cadastro

    print(f'Você tem {idade} anos')

    if sexo not in ['M', 'F']:
        print('Resposta incorreta')  # Imprime uma mensagem se a resposta do sexo estiver incorreta
    elif sexo == 'M':
        print('Você é um homem')  # Imprime uma mensagem se o sexo for masculino
    else:
        print('Você é uma mulher')  # Imprime uma mensagem se o sexo for feminino

    if continuar != 'S':
        break  # Encerra o loop se a resposta não for 'S'

# Após o término do cadastro, imprime as estatísticas coletadas
print(f'O TOTAL DE PESSOAS COM MAIS DE 18 ANOS É {pessoas}')
print(f'AO TODO TEMOS {masculino} HOMENS CADASTRADOS')
print(f'TEMOS {feminino_menos_20} MULHERES COM MENOS DE 20 ANOS')
