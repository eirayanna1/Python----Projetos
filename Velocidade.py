vel = int(input("Qual a sua velocidade atual? "))

# Verifica se a velocidade está abaixo de 80 km/h
if vel < 80:
    print('Parabéns! Está dirigindo com cuidado!')
else:
    # Se a velocidade estiver acima de 80 km/h, emite uma mensagem de multa
    # A multa é calculada multiplicando a diferença entre a velocidade atual e 80 por 7
    # O valor da multa é impresso em vermelho e em negrito
    print("\033[1m" + "\033[31m" + "\033[47m" + 'Você está acima da velocidade e será multado. A multa será no valor de {} reais'.format((vel-80)*7) + "\033[0m")
