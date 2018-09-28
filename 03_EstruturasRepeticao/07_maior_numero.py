for i in range(0, 5):
    numero = int(raw_input('Informe um numero: '))
    if ('maior' in vars()):
        if (numero > maior):
            maior = numero
    else:
        maior = numero

print 'O maior numero que voce digitou e', maior

# Obrigado pelas soluções, tem me ajudado bastante!! 
# A minha versão dessa solução ficou assm:
num = []

for i in range(5):
    num.append(int(input('Numaros: ')))
    numero = sorted(num)
print(numero[-1])
