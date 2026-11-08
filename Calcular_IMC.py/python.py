peso = float(input('Qual é o deu peso? (kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)

print('o Imc dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print ('Você está Abaixo do peso normal')

elif 18.5 <= imc < 25:
    print('Parabêns você está na faixa do peso normal')

elif 25 <= imc < 30:
    print('Você está SOBREPESO')

elif 30 <= imc <40:
    print('você esta obeso cuidado')
elif imc >= 40 :
    print('Você esta morbido, Procure um medico já!!!!!!!')