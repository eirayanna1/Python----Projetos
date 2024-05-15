while True:
    sexo = input('Qual é o seu sexo? ').strip().upper()  # Solicita ao usuário que insira o sexo e converte para maiúsculas

    if sexo == 'F':
        print('Seu sexo é feminino')  # Se a entrada for 'F', imprime que o sexo é feminino
        break  # Encerra o loop
    elif sexo == 'M':
        print('Seu sexo é masculino')  # Se a entrada for 'M', imprime que o sexo é masculino
        break  # Encerra o loop
    else:
        print('Entrada inválida! Por favor, digite novamente.')  # Se a entrada não for 'F' nem 'M', solicita uma nova entrada
