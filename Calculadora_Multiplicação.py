import time

while True:
    num = int(input('Digite um número:'))

    while num < 0:
        print("Número negativo detectado. Digite um número válido.")
        num = int(input('Digite um número:'))
    
    for c in range(1, 11):
        mult = num * c
        time.sleep(1)
        print('-' * 10)
        print('{} x {} = {}'.format(num, c, mult))
    
    # Após imprimir a tabuada, saia do loop while
    break
