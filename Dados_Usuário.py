from datetime import datetime  # Importa a classe datetime do módulo datetime

# Obtém o ano atual
ano = datetime.now().year

# Solicita ao usuário que insira o ano de nascimento
nasc = int(input('Qual o ano do seu nascimento?'))

# Calcula a idade subtraindo o ano de nascimento do ano atual
idade = ano - nasc

# Define a idade média para o alistamento militar (18 anos)
média = 18

# Calcula o ano em que o usuário deveria se alistar, se necessário
cal1= média - idade 
cal2 = ano + cal1
cal3 = ano - cal1

# Verifica se o usuário precisa se alistar e fornece informações correspondentes
if idade == 18:
    print ('Você tem {} anos'.format(idade))
    print ('É a hora exata de você se alistar')
    print ('Seu alistamento ocorrerá no ano de {}'. format(ano))
elif idade < 18:
    print ('Você tem {} anos'.format(idade))
    print ('Ainda não é o momento de se alistar')
    print ('Seu alistamento ocorrerá no ano de {}'.format(cal3))
else:
    print ('Você tem {} anos'.format(idade))
    print ('Já passou o momento de você se alistar!')
    print ('Seu alistamento ocorreu no ano de {}'.format(cal2))
