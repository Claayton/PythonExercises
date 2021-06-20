#exercicio043
massa = float(input('\033[36mDigite seu peso: \033[m'))
altura = float(input('\033[36mDigite sua altura: \033[m'))
imc = massa/(altura*altura)
if imc < 18.5:
    print('\033[33mVocê esta abaixo do peso seu burro\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[32mPARABÉNS! você está no peso ideal\033[m')
elif imc >= 25 and imc < 30:
    print('\033[35mATENÇÂO! você está no sobrepeso\033[m')
elif imc >= 30 and imc < 40:
    print('\033[35mCUIDADO! você está com obesidade\033[m')
else:
    print('\033[31mVAI FAZER UM REGIME GORDÃO! você está com obesidade mórbida\033[m')
print('\033[36mxD\033[m')
