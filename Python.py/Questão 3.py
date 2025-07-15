#Questão 3: Elabore um algoritmo que calcule o preço a pagar pelo fornecimento de energia elétrica e informe todos os dados importantes ao usuário. 
#O usuário deve entrar com a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
#O cálculo do preço a pagar deve ser feito de acordo com a tabela a seguir:

print ('\nDIGITE SEU TIPO DE INSTALAÇÃO: \n(R)Para residenciais ; (C)Para comercios ; (I)Para industrias:\n')
N = input('Tipo de instalação : ')
N1 = float(input('Digite seu consumo em KWh: '))

if N=="R" or "r": #Se caso houver um erro de digitação, o calculo prossiguirá.
    if N1<=500:
        PREÇO=0.40 #Nesse caso colocamos apenas o preço referente a faixa de calculo para a mutiplicação ao final do codigo. 
    else:
        PREÇO=0.65
elif N=="C" or "c" :
    if N1<=1000:
        PREÇO=0.55
    else:
        PREÇO=0.60
elif N=="D" or "d" :
    if N1<=5000:
        PREÇO=0.55
    else:
        PREÇO=0.60
else:
    PREÇO=0
    print('Erro, analise os dados colocados.')# se caso o usuario inserir o tipo de instalaçao errado, logo surgira essa mensagem.
    
VALOR=N1*PREÇO  # calculo do valor da conta, com os respectivos valores dos preços.

print ('Valor de sua conta: R$ {:.2f}.'.format(VALOR))
