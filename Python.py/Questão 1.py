#Problema 01:
#Elabore um algoritmo que leia 2 números e que pergunte qual operação se deseja realizar. O usuário 
#deve poder calcular soma(+), subtração(-), multiplicação (*) ou divisão (/). Exiba o resultado da 
#operação solicitada.



print ('Operações disponiveis: *Soma *subtração *multiplicação *divisão\n')
variavel=input("Digite a operação: ")
N1=float(input('Digite o primeiro numero: '))
N2=float(input('Digite o primeiro numero: '))

if variavel == 'soma':
    print('Resultado: %.2f'%(N1+N2))  #Se escrever soma no input, logo sera a soma de N1 + N2 com duas casas decimais. 
    
if variavel == 'subtração':
    print('Resultado: %.2f'%(N1-N2))  #Se escrever subtração no input, logo sera a subtraido de N1 - N2 com duas casas decimais. 
    
if variavel == 'multiplicação':
    print('Resultado: %.2f'%(N1*N2))  #Se escrever multiplicação no input, logo sera feita a multiplicação de N1 * N2 com duas casas decimais. 
    
elif variavel == 'divisão':
    if N2==0 or N1==0:
        print('Nenhum numero é divisivel por 0.')# se caso o usuario colocar 0 no N1 ou N2, logo surgira mensagem de erro.
    else:
        print('Resultado: %.2f'%(N1/N2))#se nenhum dos numeros for 0, logo sera realizado a operaçao de divisão.
else:
    print('Coloque uma operação valida.')  #se nenhuma das operaçoes citadas no enunciado for digitada no input, logo surgira uma mensagewm de erro.
