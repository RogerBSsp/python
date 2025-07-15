#Questão1:Elabore um algoritmo para aprovar um empréstimo bancário para compra de um imóvel. O usuário deve informar o valor do imóvel a ser adquirido,
#o salário bruto e a quantidade de meses que deseja pagar o empréstimo.O valor da prestação mensal não pode ser superior a 30 % do salário bruto
#e a quantidade de meses não pode ser superior a 240 meses. O valor da prestação deve ser calculado como o valor do imóvel a ser adquirido,
#dividido pelo número de meses informados pelo usuário.Informe o usuário se o empréstimo foi aprovado ou não.Em caso de aprovação apresente as condições, 
#valor da prestação e o número de meses solicitado. Em caso de não aprovação informe ao usuário qual o salário necessário para adquirir o imóvel com a 
##aprovação ou não, mostre também ao usuário todas as informações que julgar necessária para o entendimento da situação do empréstimo.

print('* FORMULARIO DE FINANCIAMENTO IMOBILIÁRIO *\n')


VM=float(input('Digite o valor do imóvel: '))
SB=float(input('Digite o valor do seu salário bruto: '))
QM=float(input('Digite a quantidade de parcelas: '))

VP=VM/QM     #VP = valor da parcela
VP30=(SB/100)*30# Valor da parcela atualizada
SB1=(SB*(VM/QM))/VP30 # \Salário atualizada
QM1=VM/VP30 # parcelas atualizada
    
if QM > 240:
    print('Quantidade maxima de parcelas 240, favor voltar e digitar quantidade de parcelas menor')# caso o usuario digite parcelas maior que 240

elif QM1>240:
    print('financiamento não aprovado!!!!\nAumente seu salário em R${:.2f}, para o seu financiamento ser aprovado. '.format(SB1))# caso a quantidade de meses atualizado exceda 240 meses
    
elif VP >= VP30:
    print('financiamento não aprovado!!!!\nVocê precisa aumentar seu salario para: R${:.2f} em {:.0f} vezes OU Aumentar as parcelas para {:.0f} vezes de R${:.2f}.'.format(SB1,QM,QM1,SB))#Valor do salario atualizado e meses at
    
else:
    QM1=VM/QM
    print('Seu financiamento foi aprovado!!!!\nValor das prestações:R$ {:.2f} em {:.0f} parcelas.'.format(QM1,QM))#calculo de das parcelas e valor do financiamento aprovado
            

